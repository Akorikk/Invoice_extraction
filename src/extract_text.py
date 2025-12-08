import pdfplumber
import os

from .utils import log


def extract_text_pdf(pdf_path: str) -> str:
    """Extract text using pdfplumber (preferred)."""
    try:
        pages = []
        with pdfplumber.open(pdf_path) as pdf:
            for p in pdf.pages:
                text = p.extract_text() or ""
                pages.append(text)
        return "\n".join(pages).strip()
    except Exception as e:
        log(f"[ERROR] pdfplumber failed for {pdf_path}: {e}")
        return ""


def extract_text(pdf_path: str, min_len: int = 80) -> str:
    """
    Extract text with pdfplumber. If too short, OCR fallback can be added.
    """
    text = extract_text_pdf(pdf_path)
    if len(text) < min_len:
        log(f"[WARN] Weak text extraction for {pdf_path}.")
        # OCR fallback can be implemented later
    return text
