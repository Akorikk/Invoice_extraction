#!/bin/bash

# Create folders
mkdir -p data/raw_invoices
mkdir -p data/processed
echo "[]" > data/labels_manual.json

mkdir -p outputs
mkdir -p notebooks
mkdir -p src
mkdir -p tests
mkdir -p app

# Create empty files
touch notebooks/demo.ipynb
touch outputs/invoices.csv
touch outputs/line_items.csv

touch src/__init__.py
touch src/config.py
touch src/extract_text.py
touch src/extract_structured.py
touch src/normalize.py
touch src/database.py
touch src/pipeline.py
touch src/evaluation.py
touch src/utils.py
touch src/regex_fallback.py

touch tests/test_extract_text.py
touch tests/test_normalization.py
touch tests/test_regex_fallback.py

touch app/streamlit_app.py

touch run_pipeline.py
touch requirements.txt
touch README.md

echo "Project folder structure created successfully!"
