VENV = .venv
BIN = $(VENV)/bin
PYTHON = $(BIN)/python
PIP = $(BIN)/pip

.DEFAULT_GOAL := help

.PHONY: install
install: 
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

.PHONY: run
run: install 
	$(PYTHON) src/app.py

.PHONY: typecheck
typecheck: install 
	$(BIN)/mypy src/

.PHONY: lint
lint: install 
	$(BIN)/flake8 src/

.PHONY: format
format: install 
	$(BIN)/black src/

.PHONY: check-requirements
check-requirements: install 
	$(BIN)/deptry src/

.PHONY: check
check: typecheck lint check-requirements 
	@echo "Все проверки пройдены успешно!"

.PHONY: clean
clean: 
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .mypy_cache

.PHONY: help
help: 
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'