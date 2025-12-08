import os

# Base directories
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_INVOICE_DIR = os.path.join(DATA_DIR, "raw_invoices")
PROCESSED_DIR = os.path.join(DATA_DIR, "processed")

OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
DB_PATH = os.path.join(OUTPUT_DIR, "invoices.db")

# Manual labels for evaluation
LABELS_PATH = os.path.join(DATA_DIR, "labels_manual.json")

# LLM model configuration
LLM_MODEL_NAME = "gpt-4o-mini"   # change depending on provider
TEMPERATURE = 0.0
