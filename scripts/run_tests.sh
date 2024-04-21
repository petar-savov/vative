#!/bin/bash

# Stop the script on any error
set -e

LINE_LENGTH=140

echo "Running static type checking with mypy..."
mypy vative/ tests/

echo "Running linting checks"
ruff check vative/ tests/ --line-length=$LINE_LENGTH
pylint vative/ tests/ --rcfile=.pylintrc

echo "Checking code formatting with black..."
black vative/ tests/ --check --line-length=$LINE_LENGTH

echo "Running tests with pytest..."
pytest .

echo "All checks completed."
