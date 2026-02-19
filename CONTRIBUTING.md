# Contributing to Band Manager Agent

Thank you for your interest in contributing to the Band Manager Agent system! This document provides guidelines for adding new tools, MCPs, scrapers, and other contributions.

## Getting Started

1. **Fork the repository**
2. **Clone your fork**: `git clone https://github.com/YOUR-USERNAME/manager.git`
3. **Set up development environment**: See README.md for instructions
4. **Create a branch**: `git checkout -b feature/your-feature-name`
5. **Make your changes**
6. **Test your changes**
7. **Submit a pull request**

## Development Environment

### Using Dev Container (Recommended)

1. Install [Docker](https://www.docker.com/) and [VS Code](https://code.visualstudio.com/)
2. Install the "Dev Containers" VS Code extension
3. Open repository in VS Code
4. Select "Reopen in Container"
5. All dependencies installed automatically

### Manual Setup

```bash
# Install Python 3.11+
python --version

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Configure .env with your settings
```

## Adding New MCPs (Model Context Protocol Tools)

MCPs integrate with external services (Google Drive, Gmail, etc.).

### 1. Create New MCP File

Create a new file in `mcps/` directory:

```bash
touch mcps/my_service_mcp.py
```

### 2. Inherit from BaseMCP

```python
"""My Service MCP for band management."""

from .base_mcp import BaseMCP


class MyServiceMCP(BaseMCP):
    """
    Integration with My Service for band management.
    
    Prerequisites:
        - My Service API enabled
        - OAuth 2.0 credentials
        - my-service-python-client installed
    
    Example:
        >>> service = MyServiceMCP('credentials.json')
        >>> service.authenticate()
        >>> service.do_something()
    """
    
    def __init__(self, credentials_path):
        """Initialize My Service MCP."""
        super().__init__(credentials_path)
        # Initialize your service client
    
    def authenticate(self):
        """Authenticate with My Service API."""
        # Implement authentication
        # Set self.authenticated = True on success
        pass
    
    def execute(self, action, params):
        """Execute an action."""
        self._ensure_authenticated()
        # Route actions to specific methods
        pass
```

### 3. Add to __init__.py

```python
# mcps/__init__.py
from .my_service_mcp import MyServiceMCP

__all__ = [..., 'MyServiceMCP']
```

### 4. Update requirements.txt

Add any new dependencies:

```txt
my-service-python-client>=1.0.0
```

### 5. Document Your MCP

Update `mcps/README.md`:
- Add to "Available MCPs" section
- Include usage example
- Document prerequisites
- Add troubleshooting tips

### 6. Write Tests

```python
# tests/test_mcps.py
def test_my_service_mcp():
    mcp = MyServiceMCP('fake-credentials.json')
    assert mcp is not None
    # Add more tests
```

## Adding New Scrapers

Web scrapers must follow ethical guidelines. See `tools/scrapers/README.md` for ethical considerations.

### 1. Create Scraper File

```bash
touch tools/scrapers/my_site_scraper.py
```

### 2. Inherit from BaseScraper

```python
"""My Site scraper for band information."""

from .base_scraper import BaseScraper


class MySiteScraper(BaseScraper):
    """
    Scrape My Site for band-related information.
    
    IMPORTANT: Review My Site's terms of service before using.
    """
    
    def __init__(self):
        """Initialize scraper with rate limiting."""
        super().__init__("https://mysite.com", rate_limit=2.0)
    
    def get_data(self, query):
        """
        Fetch data from My Site.
        
        Args:
            query (str): Search query
            
        Returns:
            list: Results
        """
        # Implementation
        pass
```

### 3. Follow Ethical Guidelines

**Required**:
- Respect robots.txt
- Implement rate limiting (minimum 1-2 seconds between requests)
- Handle errors gracefully
- Use official API if available
- Include documentation about terms of service

**Prohibited**:
- Scraping personal or private data
- Overwhelming servers with requests
- Bypassing authentication or paywalls
- Violating terms of service

### 4. Add to __init__.py

```python
# tools/scrapers/__init__.py
from .my_site_scraper import MySiteScraper

__all__ = [..., 'MySiteScraper']
```

### 5. Document Your Scraper

Update `tools/scrapers/README.md`:
- Add to "Available Scrapers" section
- Document legal/ethical considerations
- Include usage examples
- Note any limitations

## Adding New Tools

General-purpose tools go in the `tools/` directory.

### Guidelines

1. **Single Responsibility**: Each tool should do one thing well
2. **Documentation**: Include docstrings and README
3. **Dependencies**: Minimize dependencies, add to requirements.txt
4. **Error Handling**: Handle errors gracefully
5. **Testing**: Include tests for critical functionality

### Example Structure

```
tools/
└── my_tool/
    ├── README.md           # Tool documentation
    ├── __init__.py         # Package initialization
    ├── main.py             # Main tool code
    └── tests/              # Unit tests
        └── test_main.py
```

## Code Style

### Python

Follow PEP 8 style guidelines:

```bash
# Format code with black
black mcps/ tools/

# Check style with pylint
pylint mcps/ tools/
```

**Key points**:
- Use 4 spaces for indentation
- Max line length: 88 characters (black default)
- Use docstrings for all classes and public methods
- Type hints encouraged but not required

### Markdown

- Use ATX-style headers (`#`, `##`, `###`)
- One sentence per line (easier Git diffs)
- Include code fences with language tags
- Keep lines under 120 characters when possible

## Documentation

### Docstrings

Use Google-style docstrings:

```python
def my_function(arg1, arg2):
    """
    Brief description of function.
    
    Longer description if needed.
    
    Args:
        arg1 (str): Description of arg1
        arg2 (int): Description of arg2
        
    Returns:
        bool: Description of return value
        
    Raises:
        ValueError: Description of when this is raised
        
    Example:
        >>> my_function("test", 42)
        True
    """
    pass
```

### README Files

Each major directory should have a README.md explaining:
- Purpose of the directory
- How to use the tools/modules
- Examples
- Prerequisites
- Troubleshooting

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_mcps.py

# Run with coverage
pytest --cov=mcps --cov=tools
```

### Writing Tests

- Place tests in `tests/` directory
- Name test files `test_*.py`
- Name test functions `test_*`
- Use fixtures for common setup
- Mock external API calls

## Security

### Credentials

**Never commit credentials to Git!**

- Store API keys and tokens in `.env` file
- `.env` is already in `.gitignore`
- Use `.env.example` as a template
- Document required environment variables

### Sensitive Data

- Do not log credentials
- Do not include credentials in error messages
- Use service accounts when possible
- Implement least-privilege access

## Pull Request Process

1. **Update documentation**: README, docstrings, etc.
2. **Add tests**: Cover new functionality
3. **Run linters**: Ensure code passes style checks
4. **Update CHANGELOG**: Note your changes
5. **Create PR**: With clear description of changes
6. **Respond to feedback**: Address reviewer comments

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring

## Testing
How did you test your changes?

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] No credentials committed
- [ ] Ethical guidelines followed (if applicable)
```

## Questions or Issues?

- **Bug reports**: Open an issue with "Bug:" prefix
- **Feature requests**: Open an issue with "Feature:" prefix
- **Questions**: Open an issue with "Question:" prefix
- **Security issues**: Email directly, do not open public issue

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT License for code, band content remains copyrighted).

---

Thank you for contributing to Band Manager Agent! 🤘

*Last Updated: 2026-02-19*
