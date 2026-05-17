lint:
	uv run ruff check src/ tests/
	uv run mypy src/

test:
	uv run pytest tests/ -v --cov=src

check: lint test