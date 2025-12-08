import re

def basic_regex_extract(text: str) -> dict:
    """Very basic extraction when LLM fails."""

    lines = [l.strip() for l in text.splitlines() if l.strip()]

    vendor = lines[0] if lines else None

    date_match = re.search(r"\b(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})\b", text)
    date = date_match.group(1) if date_match else None

    total_match = re.search(r"(?:Total|INVOICE TOTAL)\D*(\d+\.\d{2})", text, re.IGNORECASE)
    total = float(total_match.group(1)) if total_match else None

    return {
        "invoice_number": None,
        "invoice_date": date,
        "vendor_name": vendor,
        "total_amount": total,
        "line_items": []
    }
