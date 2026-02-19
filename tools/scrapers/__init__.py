"""Web scrapers for band management."""

from .base_scraper import BaseScraper
from .instagram_scraper import InstagramScraper
from .backstage_scraper import BackstageScraper

__all__ = ['BaseScraper', 'InstagramScraper', 'BackstageScraper']
