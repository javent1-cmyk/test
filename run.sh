#!/bin/bash
set -e

echo "Running ingestion..."
python src/ingestion.py

echo "Running transformations..."
python src/transformations.py

echo "Running MLlib model..."
python src/ml_model.py

echo "Pipeline complete."
