# Variables
PYTHON_RUN_SCRIPT = run.py
VENV_DIR ?= .venv
PYTHON_FILES = app/

# Default Target
all: run

# Install dependencies and set up the virtual environment
install:
	@echo ">>> Installing dependencies using uv..."
	@uv pip sync pyproject.toml
	@echo ">>> Setup complete. Dependencies installed."

# Run the application
run:
	@echo ">>> Running application: $(PYTHON_MAIN)"
	@uv run python $(PYTHON_RUN_SCRIPT)

## Lint code using Ruff
lint: 
	@echo ">>> Linting code with Ruff..."
	@uv run ruff check $(PYTHON_FILES)

## Format code using Ruff
format: 
	@echo ">>> Formatting code with Ruff..."
	@uv run ruff format $(PYTHON_FILES)

## Check code formatting and linting without making changes
check: 
	@echo ">>> Checking code formatting and linting with Ruff..."
	@uv run ruff check $(PYTHON_FILES)
	@uv run ruff format --check $(PYTHON_FILES)

## Remove cache files
clean: 
	@echo ">>> Cleaning cache files..."
	@find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete


requirements:
	@echo ">>> Generating requirements.txt..."
	@uv pip compile pyproject.toml --generate-hashes -o requirements.txt

.PHONY: all install run lint format check clean requirements
