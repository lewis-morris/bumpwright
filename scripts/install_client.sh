#!/usr/bin/env bash
set -Eeuo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/install_client.sh [--source SPEC] [--method auto|pipx|venv|user] [--prefix DIR] [--python PYTHON] [--force]

Install the bumpwright CLI on a client machine.

Defaults:
  --source   Current repository checkout when run from this repo, otherwise "bumpwright".
  --method   auto, which prefers pipx and falls back to an isolated venv.
  --prefix   ~/.local/share/bumpwright-client for venv installs.
  --python   python3

Examples:
  scripts/install_client.sh
  scripts/install_client.sh --source /path/to/bumpwright
  scripts/install_client.sh --source git+https://github.com/arched-dev/bumpwright.git
  scripts/install_client.sh --method venv --prefix /opt/bumpwright-client
  scripts/install_client.sh --method user

Environment:
  BUMPWRIGHT_INSTALL_SOURCE   Default install source.
  BUMPWRIGHT_INSTALL_METHOD   Default method.
  BUMPWRIGHT_INSTALL_PREFIX   Default venv prefix.
  BUMPWRIGHT_INSTALL_PYTHON   Default Python executable.
USAGE
}

die() {
  echo "install-client: $*" >&2
  exit 1
}

info() {
  echo "install-client: $*"
}

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "${script_dir}/.." && pwd)"

if [[ -f "${repo_root}/pyproject.toml" ]]; then
  default_source="${repo_root}"
else
  default_source="bumpwright"
fi

source_spec="${BUMPWRIGHT_INSTALL_SOURCE:-${default_source}}"
method="${BUMPWRIGHT_INSTALL_METHOD:-auto}"
prefix="${BUMPWRIGHT_INSTALL_PREFIX:-${HOME}/.local/share/bumpwright-client}"
python_bin="${BUMPWRIGHT_INSTALL_PYTHON:-python3}"
force=0

while (($#)); do
  case "$1" in
    --source)
      [[ $# -ge 2 ]] || die "--source requires a package spec, path, or git URL"
      source_spec="$2"
      shift 2
      ;;
    --method)
      [[ $# -ge 2 ]] || die "--method requires auto, pipx, venv, or user"
      method="$2"
      shift 2
      ;;
    --prefix)
      [[ $# -ge 2 ]] || die "--prefix requires a directory"
      prefix="$2"
      shift 2
      ;;
    --python)
      [[ $# -ge 2 ]] || die "--python requires an executable"
      python_bin="$2"
      shift 2
      ;;
    --force)
      force=1
      shift
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

case "$method" in
  auto|pipx|venv|user) ;;
  *) die "--method must be auto, pipx, venv, or user" ;;
esac

command -v "$python_bin" >/dev/null 2>&1 || die "Python executable not found: ${python_bin}"

install_with_pipx() {
  command -v pipx >/dev/null 2>&1 || return 1
  info "installing with pipx from ${source_spec}"
  if [[ "$force" -eq 1 ]]; then
    pipx install --force "$source_spec"
  else
    pipx install "$source_spec"
  fi
}

install_with_user_pip() {
  info "installing with ${python_bin} -m pip --user from ${source_spec}"
  "$python_bin" -m pip install --user --upgrade "$source_spec"
}

install_with_venv() {
  local bin_dir link_dir exe
  info "installing isolated venv at ${prefix} from ${source_spec}"
  "$python_bin" -m venv "$prefix"
  bin_dir="${prefix}/bin"
  "${bin_dir}/python" -m pip install --upgrade pip
  "${bin_dir}/python" -m pip install --upgrade "$source_spec"

  link_dir="${HOME}/.local/bin"
  mkdir -p "$link_dir"
  exe="${bin_dir}/bumpwright"
  [[ -x "$exe" ]] || die "installed CLI not found at ${exe}"
  ln -sfn "$exe" "${link_dir}/bumpwright"
  info "linked ${link_dir}/bumpwright -> ${exe}"
}

if [[ "$method" == "pipx" ]]; then
  install_with_pipx || die "pipx is not installed"
elif [[ "$method" == "venv" ]]; then
  install_with_venv
elif [[ "$method" == "user" ]]; then
  install_with_user_pip
else
  if ! install_with_pipx; then
    info "pipx unavailable; falling back to venv install"
    install_with_venv
  fi
fi

if command -v bumpwright >/dev/null 2>&1; then
  info "installed command: $(command -v bumpwright)"
  bumpwright --version 2>/dev/null || bumpwright --help >/dev/null
else
  info "bumpwright installed, but it is not on PATH"
  info "add ${HOME}/.local/bin to PATH if using the venv installer"
fi

info "installation complete"
