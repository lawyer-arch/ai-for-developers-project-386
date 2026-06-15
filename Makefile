.PHONY: install compile-spec lint test dev migrate clean

install:
	uv sync
	cd spec && npm install

compile-spec:
	cd spec && npm run compile

lint:
	cd backend && ruff check .
	cd backend && ruff format --check .
	cd backend && mypy .

test:
	cd backend && pytest -v

dev:
	cd backend && uvicorn app.main:app --reload

migrate:
	cd backend && alembic upgrade head

clean:
	rm -rf backend/scheduling.db
	rm -rf spec/node_modules
	rm -rf spec/tsp-output
	rm -rf backend/.mypy_cache
	rm -rf backend/.pytest_cache
	rm -rf backend/__pycache__
	find backend -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
