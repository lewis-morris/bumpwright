#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ARTIFACTS_DIR="${ROOT_DIR}/.artifacts"
mkdir -p "${ARTIFACTS_DIR}"
cd "${ROOT_DIR}"

export COVERAGE_FILE="${ARTIFACTS_DIR}/.coverage"
export UV_CACHE_DIR="${ARTIFACTS_DIR}/.uv-cache"
mkdir -p "${UV_CACHE_DIR}"
rm -f "${COVERAGE_FILE}" "${ROOT_DIR}/.coverage"
rm -rf "${ARTIFACTS_DIR}/htmlcov"
printf "\n=== Python coverage ===\n"
uv run --no-sync pytest --cov=bumpwright --cov-report=term-missing "$@"
uv run --no-sync coverage html || true
uv run --no-sync coverage xml || true
uv run --no-sync coverage json || true
uv run --no-sync coverage lcov || true
echo "Coverage artifacts, when produced, are under .artifacts/."
