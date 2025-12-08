import json
from .utils import log
from .regex_fallback import basic_regex_extract

# If using OpenAI
# from openai import OpenAI
# client = OpenAI()


def call_llm(invoice_text: str) -> dict:
    """
    Replace this with your actual LLM provider call.
    """

    # Example prompt structure
    prompt = f"""
    You are an intelligent invoice parser. Extract structured metadata in JSON:

    {{
      "invoice_number": "",
      "invoice_date": "",
      "vendor_name": "",
      "total_amount": "",
      "line_items": [
        {{
            "description": "",
            "quantity": "",
            "unit_price": "",
            "line_total": ""
        }}
      ]
    }}

    ONLY return valid JSON. 
    Here is the invoice text:
    -------------------------
    {invoice_text}
    """

    # Example placeholder
    raise NotImplementedError("Implement LLM call here.")


def extract_structured(text: str) -> dict:
    """LLM extraction with fallback."""
    try:
        data = call_llm(text)
        return data
    except Exception as e:
        log(f"[LLM FAILED] Using regex fallback — {e}")
        return basic_regex_extract(text)
