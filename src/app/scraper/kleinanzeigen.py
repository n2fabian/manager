from __future__ import annotations

import hashlib
import logging
from urllib.parse import quote_plus, urljoin

from bs4 import BeautifulSoup

from .base import Listing, MarketplaceScraper
from .http_client import can_fetch_url
from .price import normalize_price

logger = logging.getLogger(__name__)


class KleinanzeigenScraper(MarketplaceScraper):
    name = "kleinanzeigen"

    def __init__(self, session, user_agent: str, base_url: str = "https://www.kleinanzeigen.de") -> None:
        self.session = session
        self.user_agent = user_agent
        self.base_url = base_url.rstrip("/")

    def search(self, term: str) -> list[Listing]:
        url = f"{self.base_url}/s-suchanfrage.html?keywords={quote_plus(term)}"
        if not can_fetch_url(self.session, url, self.user_agent):
            logger.warning("Skipping Kleinanzeigen query because robots.txt disallows %s", url)
            return []

        response = self.session.get(url, timeout=20)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        listings: list[Listing] = []
        cards = soup.select("article")

        for card in cards:
            link_element = card.select_one("a[href]")
            if not link_element:
                continue
            href = link_element.get("href", "").strip()
            if not href or "/s-anzeige/" not in href:
                continue

            title = link_element.get_text(" ", strip=True)
            price_text = card.get_text(" ", strip=True)
            price = normalize_price(price_text)
            if price is None:
                continue

            link = urljoin(f"{self.base_url}/", href)
            digest = hashlib.sha256(link.encode("utf-8")).hexdigest()
            listings.append(
                Listing(
                    listing_id=f"kleinanzeigen:{digest}",
                    marketplace=self.name,
                    search_term=term,
                    title=title,
                    price=price,
                    link=link,
                    timestamp=None,
                )
            )

        return listings
