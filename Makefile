## Development helpers

.PHONY: lint format test cov docs

lint:
	ruff check .

format:
	black .
	isort .
	ruff check . --fix --exit-non-zero-on-fix

test:
	pytest -q

cov:
	pytest --cov=bumpwright --cov-report=term-missing

docs:
	$(MAKE) -C docs html

