# Repository Guidelines

## Project Structure & Modules
- `bumpwright/`: core package.
  - `cli/`: CLI entry points (`__main__.py`, `bump.py`, `decide.py`, `history.py`).
  - `analysers/`: analyzers for OpenAPI, gRPC, web routes, migrations.
  - `templates/`: Jinja2 templates (e.g., `changelog.md.j2`).
- `tests/`: pytest suite (`test_*.py`, `conftest.py`).
- `docs/`: Sphinx documentation and assets.
- `pyproject.toml`: build metadata and tool configs (ruff, black, isort, pytest).
- `bumpwright.toml`: example configuration used in guides/tests.

## Build, Test, and Development Commands
- Install (dev/test): `pip install -e .[dev,test]`
- Lint: `ruff check .`
- Format: `black . && isort .`
- Tests (quiet): `pytest`
- Tests + coverage: `pytest --cov=bumpwright --cov-report=term-missing`
- Run CLI: `bumpwright --help` or `python -m bumpwright.cli --help`
- Example: `bumpwright bump --dry-run` or `bumpwright decide --format json`

## Coding Style & Naming Conventions
- Python 3.11+ with type hints.
- Formatting: Black (line length 127) and isort (Black profile).
- Linting: Ruff (`E,F,W,PL`; see `pyproject.toml`).
- Naming: modules `snake_case`, classes `PascalCase`, functions/vars `snake_case`.
- Keep public API stable; changes must go through `bumpwright/public_api.py` review.

## Testing Guidelines
- Framework: pytest; place tests under `tests/` as `test_<topic>.py`.
- Add focused unit tests and, where applicable, CLI integration tests.
- Use existing fixtures in `tests/conftest.py`; prefer deterministic, file-based samples.
- Include coverage for new/changed code; exercise error paths and edge cases.

## Commit & Pull Request Guidelines
- Commits: follow Conventional Commits (e.g., `feat:`, `fix:`, `chore:`; scopes like `feat(cli): ...`).
- PRs: include concise description, linked issues (`Closes #123`), CLI before/after output if behavior changes, and docs updates when needed.
- Checks: run `ruff`, `black`, `isort`, and `pytest` locally before submitting.

## Security & Configuration Tips
- Do not commit secrets; keep local config out of VCS.
- For CI examples and workflow patterns, see `docs/_static/workflows/`.
