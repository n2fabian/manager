from __future__ import annotations

import re

PRICE_PATTERN = re.compile(r"(\d{1,3}(?:[\.\s]\d{3})*(?:,\d{1,2})?|\d+(?:,\d{1,2})?)")


def normalize_price(raw: str) -> float | None:
    if not raw:
        return None

    lowered = raw.lower()
    if "zu verschenken" in lowered or "gratis" in lowered:
        return 0.0

    match = PRICE_PATTERN.search(raw)
    if not match:
        return None

    number = match.group(1).replace(" ", "").replace(".", "").replace(",", ".")
    try:
        return float(number)
    except ValueError:
        return None
