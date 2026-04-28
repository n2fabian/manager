from __future__ import annotations

import logging

from app.notifier.base import Notifier
from app.scraper.base import MarketplaceScraper
from app.storage.sqlite_storage import SQLiteStorage

logger = logging.getLogger(__name__)


class DealMonitor:
    def __init__(
        self,
        scrapers: list[MarketplaceScraper],
        storage: SQLiteStorage,
        notifier: Notifier | None = None,
    ) -> None:
        self.scrapers = scrapers
        self.storage = storage
        self.notifier = notifier

    def run_once(self) -> int:
        deals_found = 0
        products = self.storage.get_products()
        if not products:
            logger.warning("No products configured. Add products with CLI or PRICE_THRESHOLDS env.")
            return 0

        for product in products:
            for scraper in self.scrapers:
                try:
                    listings = scraper.search(product.search_term)
                except Exception as error:  # noqa: BLE001
                    logger.exception("Scraper %s failed for '%s': %s", scraper.name, product.search_term, error)
                    continue

                for listing in listings:
                    if listing.price > product.threshold:
                        continue
                    if self.storage.has_seen(listing.listing_id):
                        continue

                    self.storage.mark_seen(listing)
                    deals_found += 1
                    logger.info(
                        "Deal found: %s | %.2f€ <= %.2f€ | %s",
                        listing.search_term,
                        listing.price,
                        product.threshold,
                        listing.link,
                    )
                    if self.notifier:
                        try:
                            self.notifier.send_deal(listing, product.threshold)
                        except Exception as error:  # noqa: BLE001
                            logger.exception("Failed to send notification for %s: %s", listing.link, error)
        return deals_found
