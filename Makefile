PYTHON=python3

.PHONY: setup test spec-check

setup:
	@echo "Installing dev dependencies..."
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install pytest jsonschema

test:
	$(PYTHON) -m pytest -q

spec-check:
	@echo "(Optional) Run spec validation scripts here."
