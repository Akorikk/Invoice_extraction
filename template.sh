#!/bin/bash

mkdir -p data/raw_invoices
mkdir -p data/processed

mkdir -p outputs
mkdir -p notebooks
mkdir -p src
mkdir -p tests
mkdir -p app

echo "[]" > data/labels_manual.json

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

touch notebooks/invoice_pipeline_demo.ipynb

touch run_pipeline.py
touch requirements.txt
touch README.md

echo "Fresh project created!"
