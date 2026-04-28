from __future__ import annotations

from abc import ABC, abstractmethod

from app.scraper.base import Listing


class Notifier(ABC):
    @abstractmethod
    def send_deal(self, listing: Listing, threshold: float) -> None:
        raise NotImplementedError
