import os
import sqlite3

from .config import RAW_INVOICE_DIR, DB_PATH
from .extract_text import extract_text
from .extract_structured import extract_structured
from .normalize import normalize_date, to_float
from .database import init_db, insert_invoice, insert_line_items
from .utils import log


def process_invoice(file_name: str):
    path = os.path.join(RAW_INVOICE_DIR, file_name)
    text = extract_text(path)

    raw = extract_structured(text)

    invoice = {
        "file_name": file_name,
        "invoice_number": raw.get("invoice_number"),
        "invoice_date": normalize_date(raw.get("invoice_date")),
        "vendor_name": raw.get("vendor_name"),
        "total_amount": to_float(raw.get("total_amount")),
    }

    items = []
    for li in raw.get("line_items", []):
        items.append({
            "description": li.get("description", ""),
            "quantity": to_float(li.get("quantity")),
            "unit_price": to_float(li.get("unit_price")),
            "line_total": to_float(li.get("line_total")),
        })

    return invoice, items


def run_pipeline():
    init_db()
    conn = sqlite3.connect(DB_PATH)

    files = [f for f in os.listdir(RAW_INVOICE_DIR) if f.lower().endswith(".pdf")]

    for f in files:
        log(f"[PROCESSING] {f}")
        invoice, items = process_invoice(f)

        invoice_id = insert_invoice(conn, invoice)
        insert_line_items(conn, invoice_id, items)

    conn.close()
    log("[DONE] Pipeline executed successfully.")
