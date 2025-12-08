import json
import sqlite3
import pandas as pd

from .config import DB_PATH, LABELS_PATH
from .utils import log


def evaluate():
    with open(LABELS_PATH, "r") as f:
        labels = {x["file_name"]: x for x in json.load(f)}

    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM invoices", conn)
    conn.close()

    metrics = {"invoice_number": [], "invoice_date": [], "vendor_name": [], "total_amount": []}

    for _, row in df.iterrows():
        file = row["file_name"]
        if file not in labels:
            continue

        gold = labels[file]

        for key in metrics:
            predicted = str(row[key]).strip()
            actual = str(gold[key]).strip()
            metrics[key].append(int(predicted == actual))

    results = {k: sum(v) / len(v) if v else 0 for k, v in metrics.items()}

    log("[EVALUATION]")
    for k, v in results.items():
        print(f"{k}: {v:.2f}")

    return results
