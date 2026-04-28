from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path

from app.scraper.base import Listing


@dataclass(frozen=True)
class ProductThreshold:
    search_term: str
    threshold: float


class SQLiteStorage:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def initialize(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS products (
                    search_term TEXT PRIMARY KEY,
                    threshold REAL NOT NULL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS seen_listings (
                    listing_id TEXT PRIMARY KEY,
                    marketplace TEXT NOT NULL,
                    search_term TEXT NOT NULL,
                    title TEXT NOT NULL,
                    price REAL NOT NULL,
                    link TEXT NOT NULL,
                    timestamp TEXT,
                    seen_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            conn.commit()

    def sync_products(self, products: dict[str, float]) -> None:
        with self._connect() as conn:
            for search_term, threshold in products.items():
                conn.execute(
                    """
                    INSERT INTO products(search_term, threshold)
                    VALUES(?, ?)
                    ON CONFLICT(search_term) DO UPDATE SET threshold = excluded.threshold
                    """,
                    (search_term, threshold),
                )
            conn.commit()

    def add_product(self, search_term: str, threshold: float) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO products(search_term, threshold)
                VALUES(?, ?)
                ON CONFLICT(search_term) DO UPDATE SET threshold = excluded.threshold
                """,
                (search_term, threshold),
            )
            conn.commit()

    def remove_product(self, search_term: str) -> int:
        with self._connect() as conn:
            cursor = conn.execute("DELETE FROM products WHERE search_term = ?", (search_term,))
            conn.commit()
            return cursor.rowcount

    def get_products(self) -> list[ProductThreshold]:
        with self._connect() as conn:
            rows = conn.execute("SELECT search_term, threshold FROM products ORDER BY search_term ASC").fetchall()
        return [ProductThreshold(search_term=row["search_term"], threshold=row["threshold"]) for row in rows]

    def has_seen(self, listing_id: str) -> bool:
        with self._connect() as conn:
            row = conn.execute("SELECT 1 FROM seen_listings WHERE listing_id = ?", (listing_id,)).fetchone()
        return row is not None

    def mark_seen(self, listing: Listing) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                INSERT OR IGNORE INTO seen_listings(
                    listing_id,
                    marketplace,
                    search_term,
                    title,
                    price,
                    link,
                    timestamp
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    listing.listing_id,
                    listing.marketplace,
                    listing.search_term,
                    listing.title,
                    listing.price,
                    listing.link,
                    listing.timestamp,
                ),
            )
            conn.commit()
