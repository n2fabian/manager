<!-- markdownlint-disable-file -->
# Implementation Details: Agentic Workflow Transformation

**Details Date**: 2026-02-19  
**Plan Reference**: `.copilot-tracking/plans/2026-02-19/agentic-workflow-transformation-plan.instructions.md`  
**Research Reference**: `.copilot-tracking/research/2026-02-19/agentic-workflow-transformation-research.md`

---

## Context References

**Plan**: Agentic workflow transformation implementation  
**Research**: Comprehensive analysis of current state and requirements  
**Instructions Files**: 
- `.github/agents/band-manager-agent.md`
- `.github/agents/rpi-agent.agent.md`

---

## Phase 1: Development Environment Setup

### Step 1.1: Create `.devcontainer/devcontainer.json` (Lines 1-50)

**File**: `.devcontainer/devcontainer.json`  
**Operation**: CREATE

**Content**:
```json
{
  "name": "Band Manager Agent Workspace",
  "image": "mcr.microsoft.com/devcontainers/python:1-3.11-bullseye",
  "features": {
    "ghcr.io/devcontainers/features/github-cli:1": {},
    "ghcr.io/devcontainers/features/git:1": {}
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "GitHub.copilot",
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-python.black-formatter",
        "yzhang.markdown-all-in-one",
        "DavidAnson.vscode-markdownlint"
      ],
      "settings": {
        "python.defaultInterpreterPath": "/usr/local/bin/python",
        "python.linting.enabled": true,
        "python.linting.pylintEnabled": true,
        "python.formatting.provider": "black",
        "editor.formatOnSave": true,
        "files.trimTrailingWhitespace": true
      }
    }
  },
  "forwardPorts": [5000],
  "postCreateCommand": "pip install --user -r requirements.txt",
  "remoteUser": "vscode"
}
```

**Success Criteria**: File is valid JSON, devcontainer builds successfully

---

### Step 1.2: Create `requirements.txt` (Lines 51-100)

**File**: `requirements.txt`  
**Operation**: CREATE

**Content**:
```txt
# Web Framework
Flask>=3.0.0
WTForms>=3.0.0
MarkupSafe>=2.1.0

# API & Web Requests
requests>=2.31.0
beautifulsoup4>=4.12.0

# Google API Integration (for future MCP implementations)
google-api-python-client>=2.0.0
google-auth-httplib2>=0.2.0
google-auth-oauthlib>=1.2.0

# Utilities
python-dotenv>=1.0.0
markdown>=3.5.0

# Testing
pytest>=7.4.0
pytest-cov>=4.1.0

# Optional: Advanced Scraping (commented out by default)
# selenium>=4.15.0
```

**Success Criteria**: All packages install successfully, no dependency conflicts

---

### Step 1.3: Create `.env.example` (Lines 101-120)

**File**: `.env.example`  
**Operation**: CREATE

**Content**:
```bash
# Flask Configuration
SECRET_KEY=your-secret-key-here-change-in-production

# Google Drive MCP (Future)
# GOOGLE_DRIVE_CREDENTIALS_PATH=/path/to/credentials.json
# GOOGLE_DRIVE_TOKEN_PATH=/path/to/token.json

# Gmail MCP (Future)
# GMAIL_CREDENTIALS_PATH=/path/to/gmail-credentials.json
# GMAIL_TOKEN_PATH=/path/to/gmail-token.json

# Instagram API (Future)
# INSTAGRAM_ACCESS_TOKEN=your-access-token-here

# Database (Future)
# DATABASE_URL=sqlite:///band_manager.db

# Development Settings
# FLASK_ENV=development
# FLASK_DEBUG=1
```

**Success Criteria**: File is clear, documents all environment variables

---

### Step 1.4: Update `.gitignore` (Lines 121-140)

**File**: `.gitignore`  
**Operation**: EDIT (append)

**Add to existing**:
```
# Environment files
.env

# Python virtual environments
venv/
env/
ENV/
.venv

# Devcontainer
.devcontainer/.build/

# API credentials
credentials.json
token.json
gmail-credentials.json
gmail-token.json

# Website build output (for future)
website/_site/
website/.jekyll-cache/
```

**Success Criteria**: .env and credentials are properly ignored

---

## Phase 2: FUTURE_ROADMAP Expansion

### Step 2.1: Backup existing FUTURE_ROADMAP.md (Lines 141-145)

**Operation**: No file creation, just awareness

**Success Criteria**: Original content is preserved in Git history

---

### Step 2.2-2.5: Expand FUTURE_ROADMAP.md (Lines 146-550)

**File**: `docs/FUTURE_ROADMAP.md`  
**Operation**: EDIT (append sections)

**New Sections to Add**:

1. **Phase 5: Agentic Workflow Tools** (after Phase 4)
   - Overview of agentic tools ecosystem
   - Form tools library expansion
   - MCP tools (Google Drive, Email)
   - Web scraping tools (Instagram, Backstage Pro, General)
   - Financial tracking tool details
   - Email automation
   - Social media monitoring
   - Calendar & scheduling
   - Press kit generator
   - Contract management

2. **Phase 6: Web Presence & Band Websites** (after Phase 5)
   - GitHub Pages hosting strategy
   - Netlify CMS integration
   - Template selection and customization
   - Admin interface design
   - Backend access and analytics
   - Deployment workflows

3. **Implementation Priorities** (at end before Keeping It Simple section)
   - Tier 1: High Priority (form tools, MCPs, financial tracking)
   - Tier 2: Medium Priority (social media, calendar, press kit)
   - Tier 3: Long-term (multi-agent orchestration, RAG enhancement)

**Success Criteria**: 
- All requested features are documented
- Structure is consistent with existing phases
- Priority levels are clear
- Implementation estimates are reasonable

---

## Phase 3: MCP Tool Framework

### Step 3.1: Create MCP directory and base class (Lines 551-600)

**Files**:
1. `mcps/README.md`
2. `mcps/base_mcp.py`
3. `mcps/__init__.py`

**mcps/README.md**:
```markdown
# Model Context Protocol (MCP) Tools

This directory contains MCP tool implementations for external service integrations.

## Available MCPs

- **Google Drive MCP** (`google_drive_mcp.py`): Access shared storage for band documents
- **Email MCP** (`email_mcp.py`): Send automated emails via Gmail API

## Usage

[... installation and usage instructions ...]
```

**mcps/base_mcp.py**:
```python
"""Base class for MCP implementations."""

class BaseMCP:
    """Base class for Model Context Protocol tools."""
    
    def __init__(self, credentials_path=None):
        self.credentials_path = credentials_path
        self.authenticated = False
    
    def authenticate(self):
        """Authenticate with the external service."""
        raise NotImplementedError("Subclasses must implement authenticate()")
    
    def execute(self, action, params):
        """Execute an MCP action."""
        raise NotImplementedError("Subclasses must implement execute()")
```

**Success Criteria**: Framework is clear and extensible

---

### Step 3.2-3.3: Create MCP skeletons (Lines 601-750)

**Files**:
1. `mcps/google_drive_mcp.py`
2. `mcps/email_mcp.py`

**google_drive_mcp.py** (skeleton with method stubs):
```python
"""Google Drive MCP for band document management."""

from .base_mcp import BaseMCP

class GoogleDriveMCP(BaseMCP):
    """Google Drive integration for shared storage access."""
    
    def __init__(self, credentials_path):
        super().__init__(credentials_path)
        # TODO: Initialize Google Drive API client
    
    def authenticate(self):
        """Authenticate with Google Drive API."""
        # TODO: Implement OAuth2 flow
        pass
    
    def upload_file(self, file_path, folder_id=None):
        """Upload a file to Google Drive."""
        # TODO: Implement file upload
        pass
    
    def download_file(self, file_id, destination):
        """Download a file from Google Drive."""
        # TODO: Implement file download
        pass
    
    def create_share_link(self, file_id):
        """Create a shareable link for a file."""
        # TODO: Implement link generation
        pass
    
    def list_files(self, folder_id=None):
        """List files in a folder."""
        # TODO: Implement file listing
        pass
```

**email_mcp.py** (similar skeleton structure)

**Success Criteria**: Skeletons provide clear API contract for future implementation

---

## Phase 4: Web Scraper Framework

### Step 4.1-4.3: Create scraper framework (Lines 751-900)

**Files**:
1. `tools/scrapers/README.md`
2. `tools/scrapers/base_scraper.py`
3. `tools/scrapers/instagram_scraper.py`
4. `tools/scrapers/backstage_scraper.py`
5. `tools/scrapers/__init__.py`

**base_scraper.py**:
```python
"""Base class for web scrapers with rate limiting and ethics."""

import time
import requests
from bs4 import BeautifulSoup

class BaseScraper:
    """Base scraper with rate limiting and robots.txt respect."""
    
    def __init__(self, base_url, rate_limit=1.0):
        self.base_url = base_url
        self.rate_limit = rate_limit  # seconds between requests
        self.last_request = 0
    
    def fetch(self, endpoint):
        """Fetch a URL with rate limiting."""
        # TODO: Check robots.txt
        # TODO: Implement rate limiting
        # TODO: Make request
        pass
    
    def parse(self, html):
        """Parse HTML with BeautifulSoup."""
        return BeautifulSoup(html, 'html.parser')
```

**instagram_scraper.py** (skeleton):
```python
"""Instagram scraper for band discovery."""

from .base_scraper import BaseScraper

class InstagramScraper(BaseScraper):
    """Scrape Instagram for band information."""
    
    def __init__(self):
        super().__init__("https://www.instagram.com", rate_limit=2.0)
    
    def search_hashtag(self, tag):
        """Search for posts by hashtag."""
        # TODO: Implement hashtag search
        # NOTE: May require Instagram API instead of scraping
        pass
    
    def get_profile(self, username):
        """Get profile information for a user."""
        # TODO: Implement profile fetching
        pass
```

**backstage_scraper.py** (skeleton):
```python
"""Backstage Pro scraper for venue and event discovery."""

from .base_scraper import BaseScraper

class BackstageScraper(BaseScraper):
    """Scrape Backstage Pro for venues and events."""
    
    def __init__(self):
        super().__init__("https://www.backstagepro.com", rate_limit=1.5)
    
    def get_venues(self, city=None, genre=None):
        """Find venues matching criteria."""
        # TODO: Implement venue search
        pass
    
    def get_events(self, date_range=None):
        """Find events in date range."""
        # TODO: Implement event search
        pass
```

**Success Criteria**: Framework establishes clear patterns, emphasizes ethical scraping

---

## Phase 5: Band Website Mockup

### Steps 5.1-5.7: Create website structure (Lines 901-1400)

**Directory Structure**:
```
website/
├── README.md
├── DEPLOYMENT.md
├── _config.yml
├── index.html
├── music.html
├── shows.html
├── media.html
├── contact.html
├── admin/
│   └── config.yml
├── _layouts/
│   └── default.html
├── _includes/
│   ├── header.html
│   ├── footer.html
│   └── nav.html
├── assets/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
│       └── .gitkeep
└── _data/
    └── shows.yml
```

**Key Files**:

**website/README.md**:
- Overview of Combine Harvester band website
- Technology stack (Jekyll, GitHub Pages, Netlify CMS)
- Local development instructions
- Deployment instructions reference

**website/_config.yml**:
```yaml
title: Combine Harvester
description: Heavy metalcore from North Rhine-Westphalia, Germany
url: "https://n2fabian.github.io"
baseurl: "/manager/website"  # Adjust for actual deployment

# Build settings
markdown: kramdown
theme: minima  # Or custom theme

# Collections (for blog posts, shows, etc.)
collections:
  shows:
    output: true
    permalink: /shows/:title/

# Defaults
defaults:
  - scope:
      path: ""
      type: "shows"
    values:
      layout: "show"
```

**website/index.html** (simplified):
```html
---
layout: default
title: Home
---

<section class="hero">
  <h1>Combine Harvester</h1>
  <p>Chuggy breakdowns. Catchy riffs. Existential crisis.</p>
  <a href="{{ site.baseurl }}/music.html" class="cta">Listen Now</a>
</section>

<section class="bio">
  <h2>About</h2>
  <p>Combine Harvester is a modern metalcore band from North Rhine-Westphalia, Germany...</p>
</section>
```

**website/admin/config.yml** (Netlify CMS):
```yaml
backend:
  name: git-gateway
  branch: main

media_folder: "website/assets/images"
public_folder: "/assets/images"

collections:
  - name: "shows"
    label: "Shows"
    folder: "website/_shows"
    create: true
    fields:
      - { label: "Date", name: "date", widget: "datetime" }
      - { label: "Venue", name: "venue", widget: "string" }
      - { label: "City", name: "city", widget: "string" }
      - { label: "Ticket Link", name: "ticket_link", widget: "string", required: false }
```

**website/DEPLOYMENT.md**:
- Step 1: Enable GitHub Pages
- Step 2: Configure custom domain (optional)
- Step 3: Set up Netlify CMS
- Step 4: Add content via admin panel
- Step 5: Verify deployment

**Success Criteria**: 
- Website structure is complete
- Jekyll builds successfully locally
- Netlify CMS is configured
- Deployment guide is clear and actionable

---

## Phase 6: Documentation Updates

### Step 6.1-6.3: Update documentation (Lines 1401-1600)

**Files to Update**:
1. `README.md`
2. `GETTING_STARTED.md` (if exists, otherwise skip)
3. `CONTRIBUTING.md` (create new)

**README.md additions**:
- Section on devcontainer usage
- Link to expanded FUTURE_ROADMAP
- Mention new tool frameworks (MCPs, scrapers)
- Reference to band website mockup

**CONTRIBUTING.md** (new file):
```markdown
# Contributing to Band Manager Agent

## Adding New MCPs

1. Create new file in `mcps/` directory
2. Inherit from `BaseMCP` class
3. Implement required methods
4. Add tests
5. Update `mcps/README.md`

## Adding New Scrapers

1. Create new file in `tools/scrapers/` directory
2. Inherit from `BaseScraper` class
3. Respect rate limits and robots.txt
4. Add documentation
5. Update `tools/scrapers/README.md`

## Adding New Tools

[... similar guidelines ...]
```

**Success Criteria**: Documentation is complete, consistent, and helpful

---

## Discrepancy References

**Planning Log**: `.copilot-tracking/plans/logs/2026-02-19/agentic-workflow-transformation-log.md`

- None expected; implementation follows research and plan closely

---

## Per-Step Success Criteria

**Phase 1**: Devcontainer builds, requirements install, env configured  
**Phase 2**: FUTURE_ROADMAP is comprehensive and well-structured  
**Phase 3**: MCP framework is clear and extensible  
**Phase 4**: Scraper framework emphasizes ethics and provides patterns  
**Phase 5**: Website is deployment-ready with admin interface  
**Phase 6**: Documentation is complete and helpful

---

## Dependencies

**Phase 1**: Must complete first (provides dependencies for other phases)  
**Phase 2**: Depends on Phase 1 (references new tools)  
**Phases 3, 4, 5**: Can run in parallel after Phase 1  
**Phase 6**: Depends on all previous phases (documents everything)

---

*Details Created: 2026-02-19*  
*Status: Ready for Implementation*
