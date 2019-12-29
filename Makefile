ifeq ($(origin .RECIPEPREFIX), undefined)
  $(error This Make does not support .RECIPEPREFIX. Please use GNU Make 4.0 or later)
endif
.RECIPEPREFIX = >

PYTHONPATH := $(shell pwd)

MIGRATE_START_VERSION = 'c056ef9b223e'
MIGRATE_END_VERSION = 'c056ef9b223e'
MIGRATE_OUTPUT_FILE = 'second'

dev-env:
> pip install pipenv
> pipenv install --dev

lock:
> pipenv lock

lint:
> @echo "Running black..."
> @black .

> @echo ""

> @echo "Running mypy..."
> @mypy --ignore-missing-imports .

check:
> @pytest --cov=auth tests/

migration:
> @PYTHONPATH=$(PYTHONPATH) alembic revision --autogenerate

migrate-script:
> @PYTHONPATH=$(PYTHONPATH) alembic upgrade ${MIGRATE_START_VERSION}:${MIGRATE_END_VERSION} --sql > ./migrations/sql/${MIGRATE_OUTPUT_FILE}.sql