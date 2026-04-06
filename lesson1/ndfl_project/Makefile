VENV = .venv
BIN = $(VENV)/bin

install:
	python3 -m venv $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install build twine mypy black pytest


build: clean install
	$(BIN)/python3 -m build


publish: build
	$(BIN)/python3 -m twine upload --repository testpypi dist/*

clean:
	rm -rf $(VENV) build/ dist/ src/*.egg-info .mypy_cache .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +