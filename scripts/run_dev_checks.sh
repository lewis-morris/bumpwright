#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ARTIFACTS_DIR="${ROOT_DIR}/.artifacts"
mkdir -p "${ARTIFACTS_DIR}"
cd "${ROOT_DIR}"

OUT_FILE="${ARTIFACTS_DIR}/dev_issues.md"
: > "${OUT_FILE}"

log() {
  printf '%s\n' "$1" | tee -a "${OUT_FILE}" >/dev/null
}

run_tool() {
  local name="$1"
  shift
  local tmp
  tmp="$(mktemp)"
  set +e
  "$@" >"${tmp}" 2>&1
  local status=$?
  set -e
  log "- ${name}: exit ${status}"
  log ""
  log "## ${name}"
  log ""
  log '```text'
  cat "${tmp}" | tee -a "${OUT_FILE}" >/dev/null
  log '```'
  log ""
  rm -f "${tmp}"
  return "${status}"
}

failures=0
log "# Dev Issues"
log ""
log "Run timestamp (UTC): $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
log ""

run_tool "type checks" "${ROOT_DIR}/scripts/run_type_checks.sh" || failures=$((failures + 1))
run_tool "security checks" "${ROOT_DIR}/scripts/run_security_checks.sh" || failures=$((failures + 1))
run_tool "tests" "${ROOT_DIR}/scripts/run_tests.sh" || failures=$((failures + 1))

if [[ "${failures}" -eq 0 ]]; then
  log "Done. All checks passed."
else
  log "Done. ${failures} check group(s) failed."
fi

echo "Report written to ${OUT_FILE}"
exit "${failures}"
