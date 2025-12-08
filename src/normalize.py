from datetime import datetime

def normalize_date(s: str):
    if not s:
        return None

    formats = ["%m/%d/%Y", "%d/%m/%Y", "%Y-%m-%d", "%m-%d-%Y", "%d-%m-%Y"]
    for f in formats:
        try:
            return datetime.strptime(s, f).strftime("%Y-%m-%d")
        except:
            pass
    return s


def to_float(x):
    if x is None:
        return None
    try:
        return float(str(x).replace("$", "").replace(",", ""))
    except:
        return None
