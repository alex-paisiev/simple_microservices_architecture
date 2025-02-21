#!/bin/bash

# Activate the virtual environment
source .venv/bin/activate

echo "Running tests..."
# Run the tests
pytest -vv