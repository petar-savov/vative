#!/bin/bash

# Stop the script on any error
set -e

# Run pytest for testing
echo "Running tests with pytest..."
pytest

# Run mypy for static type checking
echo "Running static type checking with mypy..."
mypy vative/ tests/

# Check for linting issues with pylint
echo "Checking for linting issues with pylint..."
flake8 vative/ tests/ --max-line-length=127

# Verify code formatting with black
echo "Checking code formatting with black..."
black vative/ tests/ --check --line-length=127 

echo "All checks completed."
