mkdir -p data/raw_invoices
mkdir -p data/labeled_samples
mkdir -p src
mkdir -p notebooks
mkdir -p output/extracted_json

touch src/ocr.py
touch src/extractor_llm.py
touch src/extractor_layoutlm.py
touch src/parser.py
touch src/schema.py
touch src/database.py
touch src/pipeline.py

touch notebooks/evaluation.ipynb
touch notebooks/demo.ipynb

touch invoice-extraction/output/database.sqlite

touch requirements.txt
touch app.py