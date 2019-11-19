dev-env:
	pip install pipenv
	pipenv install --dev

lock:
	pipenv lock

lint:
	@echo "Running black..."
	@black .

	@echo ""

	@echo "Running mypy..."
	@mypy --ignore-missing-imports .
