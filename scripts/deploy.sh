#!/usr/bin/env bash
set -Eeuo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/deploy.sh [--dry-run] [--base REF] [--head REF] [--remote NAME] [--branch NAME]

Runs local verification, applies the bumpwright release bump, commits/tags it,
and pushes the release commit and tag. The existing GitHub workflow publishes
packages when the pushed tag matches v*.

Options:
  --dry-run       Run checks and preview the bump without committing, tagging, or pushing.
  --base REF      Base ref passed to bumpwright.
  --head REF      Head ref passed to bumpwright. Defaults to HEAD.
  --remote NAME   Git remote to push to. Defaults to origin.
  --branch NAME   Branch to push. Defaults to the current branch.
  -h, --help      Show this help.

Environment:
  SKIP_INSTALL=1  Do not install/update local dev dependencies before checks.
USAGE
}

die() {
  echo "deploy: $*" >&2
  exit 1
}

repo_root="$(git rev-parse --show-toplevel 2>/dev/null)" || die "not inside a git repository"
cd "$repo_root"

dry_run=0
base_ref="${BUMPWRIGHT_BASE:-}"
head_ref="${BUMPWRIGHT_HEAD:-HEAD}"
remote="${BUMPWRIGHT_DEPLOY_REMOTE:-origin}"
branch="${BUMPWRIGHT_DEPLOY_BRANCH:-$(git branch --show-current)}"

while (($#)); do
  case "$1" in
    --dry-run)
      dry_run=1
      shift
      ;;
    --base)
      [[ $# -ge 2 ]] || die "--base requires a ref"
      base_ref="$2"
      shift 2
      ;;
    --head)
      [[ $# -ge 2 ]] || die "--head requires a ref"
      head_ref="$2"
      shift 2
      ;;
    --remote)
      [[ $# -ge 2 ]] || die "--remote requires a name"
      remote="$2"
      shift 2
      ;;
    --branch)
      [[ $# -ge 2 ]] || die "--branch requires a name"
      branch="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      die "unknown argument: $1"
      ;;
  esac
done

[[ -n "$branch" ]] || die "cannot infer current branch; pass --branch"

if [[ "$dry_run" -eq 0 ]] && [[ -n "$(git status --porcelain)" ]]; then
  die "working tree must be clean before deploy"
fi

python -m pip install --upgrade pip >/dev/null
if [[ "${SKIP_INSTALL:-0}" != "1" ]]; then
  python -m pip install -e ".[dev,test]" build >/dev/null
fi

python -m ruff check .
python -m pytest
python -m build

ref_args=()
if [[ -n "$base_ref" ]]; then
  ref_args+=(--base "$base_ref")
fi
if [[ -n "$head_ref" ]]; then
  ref_args+=(--head "$head_ref")
fi

if [[ "$dry_run" -eq 1 ]]; then
  python -m bumpwright.cli bump --format md --changelog - --dry-run "${ref_args[@]}"
  exit 0
fi

python -m bumpwright.cli bump --format md --changelog CHANGELOG.md "${ref_args[@]}" --commit --tag

new_tag="$(git describe --tags --exact-match HEAD 2>/dev/null)" || die "release tag was not created at HEAD"
git push "$remote" "HEAD:$branch"
git push "$remote" "$new_tag"

echo "Deployed $new_tag via $remote/$branch"
