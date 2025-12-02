ifneq (,$(wildcard ./.env))
	include .env
endif

ENVIRONMENT = dev-ga

.PHONY: help install-git-precommit-hook setup-env add-hosts unit-tests-run docker-build docker-delete docker-prune docker-up docker-down start stop install uninstall

help: ## Available commands
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/:.*##\s*/##/g' | awk -F'##' '{ printf "%-14s %s\n", $$1, $$2 }'

install-precommit-hook: # if host machines has python3, install and confgure pre-commit
	command -v python3 >/dev/null 2>&1
	@echo Python 3 is installed
	pip install pre-commit
	pre-commit install

setup-env: ## Setup environment file
ifeq (, $(shell which envsubst))
	$(error "No envsubst in $(PATH), consider doing apt-get install gettext-base (https://command-not-found.com/envsubst)")
endif
		envsubst < .env.example > .env

docker.build: ## Docker build in detached mode
	@docker compose up --build -d

docker.delete: ## Docker delete images, volumes and its dependencies
	@docker compose down --volumes

docker.prune: ## Docker image prune
	@docker image prune --force

docker.up: ## Docker compose up
	@docker compose up

docker.down: ## Docker compose down
	@docker compose down

start: docker.up ## Start application

stop: docker.down ## Stop application

install: setup-env docker.build install-precommit-hook ## Install application

uninstall: docker.delete docker.prune ## Uninstall application and its dependencies (images, volumes, networks)

recreate: uninstall install ## Recreate application

poetry-install: ## Reinstall Poetry dependencies locally
	poetry lock
	poetry install

lint: ## Run Lint
	@pre-commit run --all-files

unit-test: ## Make Unit test
	@python -m coverage run -m pytest -s tests/unit && python -m coverage report && coverage html
