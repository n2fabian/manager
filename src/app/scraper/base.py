from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Listing:
    listing_id: str
    marketplace: str
    search_term: str
    title: str
    price: float
    link: str
    timestamp: str | None = None


class MarketplaceScraper(ABC):
    name: str

    @abstractmethod
    def search(self, term: str) -> list[Listing]:
        raise NotImplementedError
