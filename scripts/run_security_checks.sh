#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ARTIFACTS_DIR="${ROOT_DIR}/.artifacts"
mkdir -p "${ARTIFACTS_DIR}"
cd "${ROOT_DIR}"

failures=0

printf "\n=== Bandit static security scan ===\n"
if uv run --no-sync bandit --version >/dev/null 2>&1; then
  if ! uv run --no-sync bandit -q -r bumpwright -x tests --severity-level medium; then
    failures=$((failures + 1))
  fi
else
  echo "bandit is not installed. Install dev dependencies with: uv pip install -e '.[dev,test]'"
  failures=$((failures + 1))
fi

printf "\n=== pip-audit dependency scan ===\n"
if uv run --no-sync pip-audit --version >/dev/null 2>&1; then
  if ! uv run --no-sync pip-audit; then
    failures=$((failures + 1))
  fi
else
  echo "pip-audit is not installed. Install dev dependencies with: uv pip install -e '.[dev,test]'"
  failures=$((failures + 1))
fi

exit "${failures}"
