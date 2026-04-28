from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


@dataclass(frozen=True)
class AppConfig:
    search_terms: list[str]
    price_thresholds: dict[str, float]
    check_interval_minutes: int
    discord_webhook_url: str | None
    database_path: Path
    user_agent: str
    marketplaces: list[str]


def _parse_search_terms(raw: str | None) -> list[str]:
    if not raw:
        return ["Synology DS220+", "Synology DS218+"]
    return [term.strip() for term in raw.split(",") if term.strip()]


def _parse_thresholds(raw: str | None) -> dict[str, float]:
    if not raw:
        return {"Synology DS220+": 220.0, "Synology DS218+": 180.0}

    try:
        parsed = json.loads(raw)
        if isinstance(parsed, dict):
            return {str(k).strip(): float(v) for k, v in parsed.items()}
    except json.JSONDecodeError:
        pass

    output: dict[str, float] = {}
    for pair in raw.split(","):
        if ":" not in pair:
            continue
        name, threshold = pair.split(":", 1)
        name = name.strip()
        if not name:
            continue
        output[name] = float(threshold.strip())
    return output


def _parse_marketplaces(raw: str | None) -> list[str]:
    if not raw:
        return ["ebay", "kleinanzeigen"]
    return [marketplace.strip().lower() for marketplace in raw.split(",") if marketplace.strip()]


def load_config() -> AppConfig:
    load_dotenv()

    search_terms = _parse_search_terms(os.getenv("SEARCH_TERMS"))
    price_thresholds = _parse_thresholds(os.getenv("PRICE_THRESHOLDS"))
    check_interval = int(os.getenv("CHECK_INTERVAL", "15"))
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    database_path = Path(os.getenv("DB_PATH", "data/deal_sniper.db"))
    user_agent = os.getenv(
        "USER_AGENT",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    )
    marketplaces = _parse_marketplaces(os.getenv("MARKETPLACES"))

    return AppConfig(
        search_terms=search_terms,
        price_thresholds=price_thresholds,
        check_interval_minutes=max(1, check_interval),
        discord_webhook_url=webhook_url,
        database_path=database_path,
        user_agent=user_agent,
        marketplaces=marketplaces,
    )
