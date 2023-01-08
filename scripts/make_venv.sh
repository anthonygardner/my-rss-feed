#!/usr/bin/env bash

REPO_ROOT="$(pwd)"

echo "Creating a Python virtual environment..."
python3 -m venv $REPO_ROOT/.venv

source .venv/bin/activate

echo "Installing requirements..."
pip install --upgrade pip
pip install -r requirements.txt

deactivate
echo "Done!"