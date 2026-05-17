## Development helpers

.PHONY: lint format test cov docs

lint:
	uv run --no-sync ruff check .

format:
	uv run --no-sync black .
	uv run --no-sync isort .
	uv run --no-sync ruff check . --fix --exit-non-zero-on-fix

test:
	uv run --no-sync pytest -q

cov:
	uv run --no-sync pytest --cov=bumpwright --cov-report=term-missing

docs:
	uv run --no-sync sphinx-build -b html docs docs/_build/html
