# Python Rest API Template

Python repository to use as a template to build Rest API, Integrations and more

## Steps to Install the Project

1. Be sure you have [Poetry](https://python-poetry.org/docs/) installed
2. Run on terminal `poetry install`
3. Run `poetry shell` to activate the virtual environment that is created
4. Run `install-precommit-hook`
5.

## Recommended Steps - Vs Code

1. Sync VS Code with Poetry Virtualenv: `Ctrl + Shift + P (Linux) -> Select Python Interpreter -> Enter Interpreter path -> /$YOUR_PATH/pypoetry/virtualenvs/accounting-service-qBE57-es-py3.10`
2. Go to VS Code Test Explorer -> Configure Python Tests -> Select `pytest` -> Select `tests`

## Useful Commands

- Get requirements.txt from poetry: `poetry export --without-hashes --format=requirements.txt > requirements.txt`
- Update Local Dependencies: `make poetry-install`
