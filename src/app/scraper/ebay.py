from __future__ import annotations

import hashlib
import logging
from urllib.parse import quote_plus
from xml.etree import ElementTree

from .base import Listing, MarketplaceScraper
from .http_client import can_fetch_url
from .price import normalize_price

logger = logging.getLogger(__name__)


class EbayScraper(MarketplaceScraper):
    name = "ebay"

    def __init__(self, session, user_agent: str, domain: str = "www.ebay.de") -> None:
        self.session = session
        self.user_agent = user_agent
        self.domain = domain

    def search(self, term: str) -> list[Listing]:
        url = f"https://{self.domain}/sch/i.html?_nkw={quote_plus(term)}&LH_ItemCondition=3000&_rss=1"
        if not can_fetch_url(self.session, url, self.user_agent):
            logger.warning("Skipping eBay query because robots.txt disallows %s", url)
            return []

        response = self.session.get(url, timeout=20)
        response.raise_for_status()

        root = ElementTree.fromstring(response.content)
        listings: list[Listing] = []

        for item in root.findall("./channel/item"):
            title = (item.findtext("title") or "").strip()
            link = (item.findtext("link") or "").strip()
            description = (item.findtext("description") or "").strip()
            timestamp = (item.findtext("pubDate") or "").strip() or None
            price = normalize_price(description) or normalize_price(title)
            if price is None or not link:
                continue

            digest = hashlib.sha256(link.encode("utf-8")).hexdigest()
            listings.append(
                Listing(
                    listing_id=f"ebay:{digest}",
                    marketplace=self.name,
                    search_term=term,
                    title=title,
                    price=price,
                    link=link,
                    timestamp=timestamp,
                )
            )

        return listings
