"""Base class for web scrapers with ethical scraping patterns."""

import time
import requests
from urllib.robotparser import RobotFileParser
from bs4 import BeautifulSoup


class BaseScraper:
    """
    Base scraper class with rate limiting and robots.txt respect.
    
    All scrapers should inherit from this class to ensure ethical
    scraping practices are followed.
    """
    
    def __init__(self, base_url, rate_limit=1.0, user_agent=None):
        """
        Initialize the base scraper.
        
        Args:
            base_url (str): Base URL of the site to scrape
            rate_limit (float): Minimum seconds between requests (default: 1.0)
            user_agent (str, optional): Custom user agent string
        """
        self.base_url = base_url.rstrip('/')
        self.rate_limit = rate_limit
        self.last_request_time = 0
        self.session = requests.Session()
        
        # Set user agent
        self.user_agent = user_agent or (
            "BandManagerBot/1.0 (Educational/Research Purpose; "
            "+https://github.com/n2fabian/manager)"
        )
        self.session.headers.update({'User-Agent': self.user_agent})
        
        # Initialize robots.txt parser
        self.robots_parser = RobotFileParser()
        self.robots_url = f"{self.base_url}/robots.txt"
        self._load_robots_txt()
    
    def _load_robots_txt(self):
        """Load and parse robots.txt file."""
        try:
            self.robots_parser.set_url(self.robots_url)
            self.robots_parser.read()
        except Exception as e:
            print(f"Warning: Could not load robots.txt: {e}")
            # If robots.txt can't be loaded, be conservative
            self.robots_parser = None
    
    def _can_fetch(self, url):
        """
        Check if URL can be fetched according to robots.txt.
        
        Args:
            url (str): URL to check
            
        Returns:
            bool: True if fetching is allowed, False otherwise
        """
        if self.robots_parser is None:
            # If robots.txt couldn't be loaded, allow (but log warning)
            print(f"Warning: Proceeding without robots.txt check for {url}")
            return True
        
        return self.robots_parser.can_fetch(self.user_agent, url)
    
    def _wait_for_rate_limit(self):
        """Wait to respect rate limiting."""
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time
        
        if time_since_last_request < self.rate_limit:
            wait_time = self.rate_limit - time_since_last_request
            time.sleep(wait_time)
        
        self.last_request_time = time.time()
    
    def fetch(self, endpoint):
        """
        Fetch a URL with rate limiting and robots.txt checking.
        
        Args:
            endpoint (str): Endpoint to fetch (relative to base_url)
            
        Returns:
            str: HTML content of the page
            
        Raises:
            ValueError: If robots.txt disallows fetching
            requests.RequestException: If request fails
        """
        # Construct full URL
        if endpoint.startswith('http'):
            url = endpoint
        else:
            url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        # Check robots.txt
        if not self._can_fetch(url):
            raise ValueError(
                f"Fetching {url} is disallowed by robots.txt"
            )
        
        # Wait for rate limit
        self._wait_for_rate_limit()
        
        # Make request
        response = self.session.get(url, timeout=30)
        response.raise_for_status()
        
        return response.text
    
    def parse(self, html):
        """
        Parse HTML with BeautifulSoup.
        
        Args:
            html (str): HTML content to parse
            
        Returns:
            BeautifulSoup: Parsed HTML tree
        """
        return BeautifulSoup(html, 'html.parser')
    
    def extract_text(self, soup, selector):
        """
        Extract text from HTML using CSS selector.
        
        Args:
            soup (BeautifulSoup): Parsed HTML
            selector (str): CSS selector
            
        Returns:
            str: Extracted text, or None if not found
        """
        element = soup.select_one(selector)
        return element.get_text(strip=True) if element else None
    
    def extract_all_text(self, soup, selector):
        """
        Extract text from all matching elements.
        
        Args:
            soup (BeautifulSoup): Parsed HTML
            selector (str): CSS selector
            
        Returns:
            list: List of extracted text strings
        """
        elements = soup.select(selector)
        return [el.get_text(strip=True) for el in elements]
    
    def extract_attribute(self, soup, selector, attribute):
        """
        Extract attribute value from HTML element.
        
        Args:
            soup (BeautifulSoup): Parsed HTML
            selector (str): CSS selector
            attribute (str): Attribute name to extract
            
        Returns:
            str: Attribute value, or None if not found
        """
        element = soup.select_one(selector)
        return element.get(attribute) if element else None
