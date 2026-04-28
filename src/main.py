from __future__ import annotations

import argparse
import logging

from apscheduler.schedulers.blocking import BlockingScheduler

from app.config.settings import AppConfig
from app.config import load_config
from app.monitor import DealMonitor
from app.notifier import DiscordNotifier
from app.scraper import EbayScraper, KleinanzeigenScraper
from app.scraper.http_client import build_http_session
from app.storage import SQLiteStorage


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )


def build_monitor(config: AppConfig):
    session = build_http_session(config.user_agent)
    scrapers = []
    if "ebay" in config.marketplaces:
        scrapers.append(EbayScraper(session=session, user_agent=config.user_agent))
    if "kleinanzeigen" in config.marketplaces:
        scrapers.append(KleinanzeigenScraper(session=session, user_agent=config.user_agent))

    notifier = DiscordNotifier(config.discord_webhook_url, session=session) if config.discord_webhook_url else None
    storage = SQLiteStorage(config.database_path)
    storage.initialize()
    products: dict[str, float] = {}
    for term in config.search_terms:
        if term in config.price_thresholds:
            products[term] = config.price_thresholds[term]
        else:
            logging.warning("Skipping search term without threshold: %s", term)
    for term, threshold in config.price_thresholds.items():
        products.setdefault(term, threshold)
    storage.sync_products(products)

    return DealMonitor(scrapers=scrapers, storage=storage, notifier=notifier), storage


def cmd_run() -> None:
    config = load_config()
    monitor, _storage = build_monitor(config)
    scheduler = BlockingScheduler()
    scheduler.add_job(monitor.run_once, "interval", minutes=config.check_interval_minutes, max_instances=1)

    logging.info("Starting deal monitor with interval=%s min", config.check_interval_minutes)
    monitor.run_once()
    scheduler.start()


def cmd_check_once() -> None:
    config = load_config()
    monitor, _storage = build_monitor(config)
    deals = monitor.run_once()
    logging.info("Check completed. Deals found: %s", deals)


def cmd_add_product(term: str, threshold: float) -> None:
    config = load_config()
    _monitor, storage = build_monitor(config)
    storage.add_product(term, threshold)
    logging.info("Added/updated product threshold: %s <= %.2f€", term, threshold)


def cmd_remove_product(term: str) -> None:
    config = load_config()
    _monitor, storage = build_monitor(config)
    removed = storage.remove_product(term)
    if removed:
        logging.info("Removed product: %s", term)
    else:
        logging.info("Product not found: %s", term)


def cmd_list_products() -> None:
    config = load_config()
    _monitor, storage = build_monitor(config)
    products = storage.get_products()
    if not products:
        logging.info("No products configured.")
        return
    for product in products:
        logging.info("%s <= %.2f€", product.search_term, product.threshold)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Deal sniper for second-hand marketplaces")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("run", help="Run continuous monitoring")
    subparsers.add_parser("check-once", help="Run one monitoring cycle")

    add_parser = subparsers.add_parser("add-product", help="Add or update a product threshold")
    add_parser.add_argument("term", type=str)
    add_parser.add_argument("threshold", type=float)

    remove_parser = subparsers.add_parser("remove-product", help="Remove a product threshold")
    remove_parser.add_argument("term", type=str)

    subparsers.add_parser("list-products", help="List configured product thresholds")

    return parser.parse_args()


def main() -> None:
    configure_logging()
    args = parse_args()
    command = args.command or "run"

    if command == "run":
        cmd_run()
    elif command == "check-once":
        cmd_check_once()
    elif command == "add-product":
        cmd_add_product(args.term, args.threshold)
    elif command == "remove-product":
        cmd_remove_product(args.term)
    elif command == "list-products":
        cmd_list_products()
    else:
        raise SystemExit(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
