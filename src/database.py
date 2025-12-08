import sqlite3
from .config import DB_PATH
from .utils import log

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS invoices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_name TEXT,
        vendor_name TEXT,
        invoice_number TEXT,
        invoice_date TEXT,
        total_amount REAL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS line_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        invoice_id INTEGER,
        description TEXT,
        quantity REAL,
        unit_price REAL,
        line_total REAL,
        FOREIGN KEY(invoice_id) REFERENCES invoices(id)
    )
    """)

    conn.commit()
    conn.close()
    log("[DB] Initialized.")


def insert_invoice(conn, inv: dict) -> int:
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO invoices (file_name, vendor_name, invoice_number, invoice_date, total_amount)
        VALUES (?, ?, ?, ?, ?)
    """, (
        inv["file_name"],
        inv["vendor_name"],
        inv["invoice_number"],
        inv["invoice_date"],
        inv["total_amount"]
    ))
    conn.commit()
    return cur.lastrowid


def insert_line_items(conn, invoice_id, items):
    cur = conn.cursor()
    for li in items:
        cur.execute("""
        INSERT INTO line_items (invoice_id, description, quantity, unit_price, line_total)
        VALUES (?, ?, ?, ?, ?)
        """, (invoice_id, li["description"], li["quantity"], li["unit_price"], li["line_total"]))
    conn.commit()
