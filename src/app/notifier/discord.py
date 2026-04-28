from __future__ import annotations

import requests

from app.scraper.base import Listing

from .base import Notifier


class DiscordNotifier(Notifier):
    def __init__(self, webhook_url: str, session: requests.Session | None = None) -> None:
        self.webhook_url = webhook_url
        self.session = session or requests.Session()

    def send_deal(self, listing: Listing, threshold: float) -> None:
        content = (
            "🔥 Deal found!\n"
            f"Product: {listing.search_term}\n"
            f"Price: {listing.price:.2f}€ (threshold: {threshold:.2f}€)\n"
            f"Title: {listing.title}\n"
            f"Marketplace: {listing.marketplace}\n"
            f"Link: {listing.link}"
        )
        response = self.session.post(self.webhook_url, json={"content": content}, timeout=15)
        response.raise_for_status()
