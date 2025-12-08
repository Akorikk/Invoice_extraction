
mkdir -p data/raw_invoices
mkdir -p data/labeled_samples
mkdir -p src
mkdir -p notebooks
mkdir -p output/extracted_json

touch src/__init__.py
touch src/config.py 
touch src/extract_text.py 
touch src/extract_structured.py  
touch src/normalize.py
touch src/database.py
touch src/pipeline.py
touch src/evaluation.py
touch src/utils.py

mkdir -p tests
touch tests/test_extract_text.py
touch tests/test_normalization.py
touch tests/test_regex_fallback.py

mkdir -p outputs
touch outputs/invoices.db
touch outputs/invoices.csv
touch outputs/line_items.csv

touch notebooks/evaluation.ipynb
touch notebooks/demo.ipynb

touch invoice-extraction/output/database.sqlite

touch requirements.txt
touch run_pipeline.py
touch app.py
