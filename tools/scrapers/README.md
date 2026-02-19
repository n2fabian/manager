# Web Scrapers for Band Management

This directory contains web scraping tools for discovering bands, venues, events, and other music industry information.

## ⚠️ Important: Ethical Scraping Guidelines

Before using any scraper, please review these ethical guidelines:

### Legal & Ethical Considerations

1. **Respect robots.txt**: Always check and honor robots.txt files
2. **Rate Limiting**: Implement delays between requests (minimum 1-2 seconds)
3. **Terms of Service**: Review and comply with website terms of service
4. **Public Data Only**: Only scrape publicly available information
5. **No Personal Data**: Do not store sensitive or personal information
6. **Attribution**: Give credit to data sources when appropriate
7. **Server Load**: Avoid overwhelming servers with requests

### Best Practices

- Use official APIs whenever available (preferred over scraping)
- Cache results to minimize repeat requests
- Handle errors gracefully and log failures
- Rotate user agents if necessary (but don't impersonate browsers maliciously)
- Consider reaching out to site owners for permission

## Available Scrapers

### Instagram Scraper (`instagram_scraper.py`)

**Purpose**: Discover bands, track growth, identify promotional opportunities

**Status**: Skeleton implementation - requires Instagram Graph API or careful scraping implementation

**Capabilities** (when implemented):
- Search by hashtags (#metalcore, #livemusic, etc.)
- Extract band profiles
- Monitor follower counts
- Analyze engagement rates

**Recommendation**: Use Instagram Graph API instead of scraping for reliability and compliance

### Backstage Pro Scraper (`backstage_scraper.py`)

**Purpose**: Discover venues, festivals, and booking opportunities

**Status**: Skeleton implementation - requires terms of service review

**Capabilities** (when implemented):
- Search venues by city and genre
- Extract contact information
- Track event calendars
- Export to contact management

**Important**: Check Backstage Pro terms of service before implementing

### Base Scraper (`base_scraper.py`)

**Purpose**: Base class with ethical scraping patterns

**Features**:
- Rate limiting
- robots.txt checking
- Error handling
- Logging

## Usage

### Prerequisites

```bash
pip install requests beautifulsoup4
# For advanced scraping with JavaScript:
# pip install selenium
```

### Example: Using Base Scraper

```python
from tools.scrapers import BaseScraper

class MyCustomScraper(BaseScraper):
    def __init__(self):
        super().__init__("https://example.com", rate_limit=2.0)
    
    def scrape_page(self, endpoint):
        html = self.fetch(endpoint)
        soup = self.parse(html)
        # Extract data from soup
        return data

scraper = MyCustomScraper()
data = scraper.scrape_page("/bands")
```

### Example: Instagram Scraper (API-based - Recommended)

```python
# This approach uses Instagram Graph API (requires business account)
from tools.scrapers import InstagramScraper

# Initialize with access token
instagram = InstagramScraper(access_token='YOUR_TOKEN')

# Search for bands by hashtag
bands = instagram.search_hashtag('metalcore', limit=50)

# Get profile information
profile = instagram.get_profile('combineharvester_band')
print(f"Followers: {profile['followers']}")
```

## Configuration

Create a `.env` file with necessary credentials:

```bash
# Instagram
INSTAGRAM_ACCESS_TOKEN=your_access_token_here

# Other API keys as needed
```

## Testing

```bash
# Test base scraper
pytest tests/test_scrapers.py::test_base_scraper

# Test specific scraper
pytest tests/test_scrapers.py::test_instagram_scraper
```

## Troubleshooting

### "Blocked by robots.txt" error

- Respect the robots.txt file
- Consider reaching out to site owner
- Use official API if available

### Rate limiting / 429 errors

- Increase delay between requests
- Implement exponential backoff
- Reduce scraping frequency

### "Access denied" / 403 errors

- Check if scraping is allowed by terms of service
- May need to add proper user agent
- Site may have anti-scraping measures

## Legal Disclaimer

Web scraping may be subject to legal restrictions in your jurisdiction. This framework is provided for educational purposes and legitimate use cases only. Users are responsible for:

- Complying with applicable laws
- Respecting website terms of service
- Obtaining necessary permissions
- Using data ethically and responsibly

**When in doubt, use official APIs instead of scraping.**

## Resources

- [Web Scraping Best Practices](https://www.scrapehero.com/web-scraping-best-practices/)
- [Instagram Graph API](https://developers.facebook.com/docs/instagram-api)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Robots.txt Specification](https://www.robotstxt.org/)

## Contributing

See `CONTRIBUTING.md` for guidelines on adding new scrapers.

---

*Last Updated: 2026-02-19*
