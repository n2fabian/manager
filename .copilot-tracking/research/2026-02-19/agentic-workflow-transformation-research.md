<!-- markdownlint-disable-file -->
# Agentic Workflow Transformation Research

**Research Date**: 2026-02-19  
**Topic**: Transform repository into base for agentic workflows  
**Researcher**: RPI Agent  

---

## 📋 Scope & Requirements

### User Requirements
Based on the problem statement, the following capabilities need to be implemented:

1. **Devcontainer for autonomous agent work**
   - Support Python-based agent workflows
   - Pre-configured development environment
   - GitHub Copilot integration
   - Tools for form UI and agent development

2. **Expanded FUTURE_ROADMAP.md**
   - Include agentic workflow improvements
   - Add tools similar to the form tool created yesterday
   - Serve as basis for roadmap and PBIs for future agent sessions

3. **MCP Tools for Shared Storage**
   - Google Drive integration for band documents
   - Shared storage access for collaboration

4. **Web Browsing/Scraping Tools**
   - Instagram crawler for band discovery
   - Backstage Pro crawler for venues, festivals, events
   - General web scraping capability for industry information

5. **Band Website for Combine Harvester** (if confident)
   - Free hosting (GitHub Pages)
   - Template-based with admin UI
   - Non-technical content management
   - Backend access for full control
   - Request tracking capability

6. **Financial Tracking Tool** (future scope)
   - Track band finances
   - Income and expense monitoring
   - Integration with existing financial tracking templates

### Success Criteria
- ✅ Devcontainer is functional and supports agent workflows
- ✅ FUTURE_ROADMAP.md is comprehensive and actionable
- ✅ Future scope includes all requested capabilities
- ✅ If website created: deployed, functional, and accessible
- ✅ All changes are minimal and focused on requirements

---

## 🔍 Research Findings

### Current State Analysis

#### Repository Structure
- **Type**: Markdown-based band management system
- **Primary Language**: Python (minimal - single Flask app)
- **Data Storage**: Markdown files, JSON configs
- **Version Control**: Git-based
- **Agents**: 2 configured (Band Manager, RPI Agent)
- **Tools**: Simple form UI (Flask + WTForms)

#### Existing Infrastructure
- No devcontainer or Docker configuration
- No package management (no requirements.txt)
- No CI/CD pipelines
- No external API integrations
- No database backend
- No MCP implementations

#### Current Capabilities
✅ **Working Well**:
- Form-based data collection (simple_form_ui.py)
- Agent configuration system
- Markdown template library
- Workflow documentation
- Task tracking
- Git-based version control

❌ **Missing for Agentic Workflows**:
- Development container setup
- Python dependency management
- External API integrations
- Web scraping capabilities
- Shared storage access (Google Drive, etc.)
- Automated data collection
- Website hosting/deployment

---

## 🏗️ Devcontainer Requirements

### Base Requirements
- **Python**: 3.11+ (for modern async support and type hints)
- **Flask**: Web framework (already in use)
- **WTForms**: Form handling (already in use)
- **Git**: Version control integration

### Additional Tools Needed
- **requests**: For API calls and web requests
- **beautifulsoup4**: Web scraping capability
- **selenium** (optional): Advanced web scraping with JavaScript
- **google-api-python-client**: Google Drive MCP integration
- **python-dotenv**: Environment variable management
- **markdown**: Markdown processing
- **pytest**: Testing framework

### Devcontainer Configuration
```json
{
  "name": "Band Manager Agent Workspace",
  "image": "mcr.microsoft.com/devcontainers/python:3.11",
  "features": {
    "ghcr.io/devcontainers/features/github-cli:1": {}
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "github.copilot",
        "ms-python.python",
        "ms-python.vscode-pylance"
      ]
    }
  },
  "forwardPorts": [5000],
  "postCreateCommand": "pip install -r requirements.txt"
}
```

---

## 📚 FUTURE_ROADMAP Expansion Topics

### Agentic Workflow Tools (Tier 1 - High Priority)

#### 1. **Form Tools Library**
- Expand beyond simple_form_ui.py
- Create reusable form components
- Multi-step wizards for different workflows
- Templates: venue contact forms, show booking forms, financial entry forms

#### 2. **MCP Tools for Shared Storage**

**Google Drive MCP**:
- Purpose: Access band documents, contracts, press photos, recordings
- Capabilities:
  - Upload/download files
  - Share links with venues
  - Organize by band/event
  - Search across documents
- Implementation: google-api-python-client with OAuth2
- Security: Token storage in .env, not committed to Git

**Dropbox MCP** (alternative/additional):
- Similar capabilities to Google Drive
- May be preferred for some collaborators

#### 3. **Web Scraping/Browsing Tools**

**Instagram Band Discovery**:
- Purpose: Find bands, track followers, analyze engagement
- Capabilities:
  - Search by hashtags (#metalcore, #livemusic)
  - Extract band profiles
  - Monitor follower growth
  - Identify potential tour partners
- Implementation: Instagram Graph API or selenium-based scraping
- Limitations: Rate limiting, authentication requirements

**Backstage Pro Crawler**:
- Purpose: Discover venues, festivals, events
- Capabilities:
  - Scrape venue databases
  - Extract contact information
  - Track event calendars
  - Identify booking opportunities
- Implementation: requests + BeautifulSoup
- Ethics: Respect robots.txt, rate limiting

**General Web Scraper**:
- Purpose: Flexible information gathering
- Use cases:
  - Venue capacity from websites
  - Festival lineups
  - Ticket sale sites
  - Music news and reviews
- Implementation: Modular scraper with configurable targets

#### 4. **Financial Tracking Tool**

**Enhanced Financial System**:
- Purpose: Comprehensive band finance management
- Features:
  - Income tracking (shows, merch, streaming, grants)
  - Expense tracking (equipment, travel, production, marketing)
  - Category-based reporting
  - Tax preparation assistance
  - Profit/loss statements
  - Band-specific budgets
  - Integration with existing financial-tracking.md template
- Implementation: Flask web UI + SQLite database
- Export: CSV, PDF reports for accountants

#### 5. **Email Automation MCP**

**Email Integration**:
- Purpose: Send venue outreach, follow-ups, confirmations
- Capabilities:
  - Gmail API integration
  - Template-based email generation
  - Scheduled sending
  - Response tracking
  - Attachment support (tech riders, EPKs)
- Implementation: Gmail API with OAuth2
- Templates: Use existing venue-email-template.md

### Agentic Workflow Tools (Tier 2 - Medium Priority)

#### 6. **Social Media Monitoring**
- Track mentions, hashtags, engagement
- Spotify for Artists API integration
- Instagram Insights API
- Facebook Page Analytics

#### 7. **Calendar & Scheduling**
- Show calendar with Google Calendar integration
- Automated reminders (load-in, soundcheck, doors)
- Travel time calculations
- Conflict detection

#### 8. **Press Kit Generator**
- Automated EPK (Electronic Press Kit) creation
- PDF generation from markdown
- Asset management (photos, logos, music)
- Version control for different venues/events

#### 9. **Contract Management**
- Template library for different agreement types
- Digital signature integration (DocuSign API)
- Version tracking
- Expiration alerts

### Infrastructure & System Improvements (Tier 3)

#### 10. **Database Migration**
- SQLite for local development
- PostgreSQL for production (if needed)
- Migration scripts from markdown to DB
- Maintain backward compatibility

#### 11. **RAG System**
- Vector database (ChromaDB, Pinecone)
- Semantic search across all documents
- Natural language queries
- Context-aware recommendations

#### 12. **Multi-Agent Orchestration**
- Specialized agents per domain (booking, finance, promo)
- Agent coordination protocols
- Shared memory/context
- Autonomous task delegation

#### 13. **API Gateway**
- Centralized API for all external integrations
- Rate limiting and caching
- Error handling and retry logic
- Monitoring and logging

---

## 🌐 Band Website for Combine Harvester

### Requirements Analysis

**Hosting Options**:
- ✅ **GitHub Pages**: Free static hosting, custom domains, HTTPS
- Alternative: Netlify, Vercel (also free tiers)

**Technology Stack**:
- **Frontend**: HTML/CSS/JavaScript (static site)
- **CMS**: Headless CMS or custom admin panel
- **Backend**: GitHub Pages (static) + optional API (Netlify Functions, Vercel Serverless)

**Admin Interface Options**:

**Option 1: Forestry.io / Netlify CMS** (Recommended)
- Static site generator integration
- Non-technical content editing
- Markdown-based content
- Git-backed (version control)
- Free tier available

**Option 2: Custom Flask Admin**
- Flask backend for admin panel
- SQLite for content storage
- API endpoint for frontend
- Deployed on free hosting (PythonAnywhere, Heroku free tier)

**Option 3: GitHub-based CMS**
- Edit markdown files via GitHub web UI
- Automated rebuilds with GitHub Actions
- No separate admin panel needed
- Simplest but requires GitHub account access

### Recommended Approach

**Static Site + Netlify CMS**:
1. Static site generator (Jekyll, Hugo, or 11ty)
2. GitHub Pages for hosting
3. Netlify CMS for admin interface
4. Custom domain: combineharvester.band (approx. $12/year)

**Content Structure**:
- Home page (hero image, bio, latest news)
- Music page (Spotify embed, streaming links)
- Shows page (upcoming and past shows)
- Media page (photos, videos, press)
- Contact page (booking form, social links)

**Admin Capabilities**:
- Add/edit/delete pages
- Upload images
- Manage show dates
- Update bio and news
- Switch page sections on/off
- Customize colors/fonts (limited)

**Backend Access**:
- Full Git repository access
- Direct HTML/CSS editing
- Custom JavaScript for analytics
- Request tracking via Google Analytics or Plausible

### Website Template Options

**Free Templates for Bands**:
1. **HTML5 UP**: Free responsive HTML5 templates
2. **Jekyll Themes**: Specifically for GitHub Pages
3. **Colorlib**: Free band/music website templates
4. **Creative Tim**: Free Bootstrap templates

**Recommended Template**: "Spectral" by HTML5 UP
- Clean, modern design
- Music-focused layout
- Mobile responsive
- Easy customization
- Free license

### Implementation Confidence Level

**Confidence: HIGH (90%)**
- GitHub Pages is well-documented and reliable
- Static site generators are mature technology
- Netlify CMS integration is straightforward
- Template customization is manageable
- Deployment process is automated

**Risks**:
- Learning curve for non-technical users (mitigated by CMS)
- Limited dynamic features (no user accounts, comments)
- Custom functionality requires JavaScript

**Decision**: ✅ **PROCEED** with creating mock-up and deployment guide

---

## 🔧 Technical Implementation Approaches

### 1. Devcontainer Setup

**Files to Create**:
- `.devcontainer/devcontainer.json`: Container configuration
- `.devcontainer/Dockerfile` (optional): Custom image build
- `requirements.txt`: Python dependencies
- `.env.example`: Environment variable template

**Dependencies to Include**:
```
# Web Framework
Flask>=3.0.0
WTForms>=3.0.0
MarkupSafe>=2.1.0

# API & Web
requests>=2.31.0
beautifulsoup4>=4.12.0
google-api-python-client>=2.0.0
google-auth-httplib2>=0.2.0
google-auth-oauthlib>=1.2.0

# Utilities
python-dotenv>=1.0.0
markdown>=3.5.0

# Testing
pytest>=7.4.0
pytest-cov>=4.1.0

# Optional Advanced Scraping
selenium>=4.15.0
```

### 2. FUTURE_ROADMAP.md Update Strategy

**Structure**:
- Keep existing phases (Phase 1-4)
- Add new "Phase 5: Agentic Workflow Tools"
- Expand Phase 2 (SQL) with financial tool details
- Expand Phase 3 (RAG) with search capabilities
- Add Phase 6 for web presence (band website)

**Format**:
- Maintain consistent markdown structure
- Use tables for tool comparisons
- Include implementation estimates
- Add priority levels (High/Medium/Low)
- Link to example implementations

### 3. MCP Tool Architecture

**Design Pattern**:
```python
# Base MCP class
class BaseMCP:
    def __init__(self, credentials_path):
        self.auth = self.authenticate(credentials_path)
    
    def authenticate(self, path):
        # OAuth2 or API key handling
        pass
    
    def execute(self, action, params):
        # Execute MCP action
        pass

# Google Drive MCP
class GoogleDriveMCP(BaseMCP):
    def upload_file(self, file_path, folder_id):
        pass
    
    def download_file(self, file_id, destination):
        pass
    
    def share_link(self, file_id):
        pass

# Usage
drive = GoogleDriveMCP("credentials.json")
drive.upload_file("tech-rider.pdf", "band-documents")
link = drive.share_link(file_id)
```

### 4. Web Scraper Architecture

**Modular Design**:
```python
# Base scraper
class BaseScraper:
    def __init__(self, base_url, rate_limit=1.0):
        self.base_url = base_url
        self.rate_limit = rate_limit
    
    def fetch(self, endpoint):
        # Respect robots.txt and rate limits
        pass
    
    def parse(self, html):
        # BeautifulSoup parsing
        pass

# Instagram scraper
class InstagramScraper(BaseScraper):
    def search_hashtag(self, tag):
        pass
    
    def get_profile(self, username):
        pass

# Backstage Pro scraper
class BackstageScraper(BaseScraper):
    def get_venues(self, city=None, genre=None):
        pass
    
    def get_events(self, date_range):
        pass
```

### 5. Band Website Implementation

**Project Structure**:
```
website/
├── _config.yml              # Jekyll configuration
├── index.html               # Home page
├── music.html               # Music/releases
├── shows.html               # Show calendar
├── media.html               # Photos/videos
├── contact.html             # Contact form
├── admin/
│   └── config.yml          # Netlify CMS config
├── _layouts/
│   └── default.html        # Base template
├── _includes/
│   ├── header.html
│   ├── footer.html
│   └── show-listing.html
├── assets/
│   ├── css/
│   ├── js/
│   └── images/
└── _data/
    ├── shows.yml           # Show data
    └── social.yml          # Social links
```

**Deployment**:
1. Push to GitHub repository
2. Enable GitHub Pages in settings
3. Configure custom domain (optional)
4. Add Netlify CMS via admin/config.yml
5. Deploy and test

---

## 📊 Implementation Priorities

### Must Have (This Session)
1. ✅ Devcontainer configuration
2. ✅ requirements.txt
3. ✅ Expanded FUTURE_ROADMAP.md with all requested features
4. ✅ .env.example for credential management

### Should Have (This Session)
5. ✅ Band website mockup and deployment guide
6. ✅ MCP tool structure/framework
7. ✅ Web scraper base classes

### Nice to Have (Future Sessions)
8. ⏳ Actual MCP implementations (Google Drive)
9. ⏳ Working web scrapers (Instagram, Backstage)
10. ⏳ Financial tracking web UI
11. ⏳ Full band website deployment

---

## 🎯 Selected Approach & Rationale

### Devcontainer: Python 3.11 + Flask + Tools
**Rationale**: Matches existing tech stack, supports all planned tools, widely compatible

### FUTURE_ROADMAP: Expanded with 6 Phases
**Rationale**: Preserves existing structure, adds new capabilities systematically

### MCP Tools: Framework + Examples
**Rationale**: Provides structure for future implementation, doesn't over-commit

### Band Website: Jekyll + Netlify CMS + GitHub Pages
**Rationale**: Free, well-documented, non-technical friendly, backend accessible

### Scrapers: Base classes + Interface definitions
**Rationale**: Establishes pattern, allows future implementation without coupling

---

## 🚀 Next Steps

### Phase 2: Plan
1. Create implementation plan with phases
2. Define file changes and additions
3. Establish success criteria per change
4. Validate plan against research

### Phase 3: Implement
1. Create devcontainer configuration
2. Create requirements.txt
3. Update FUTURE_ROADMAP.md
4. Create MCP tool framework
5. Create band website mockup/guide
6. Update .gitignore
7. Create .env.example

### Phase 4: Review
1. Test devcontainer builds successfully
2. Validate requirements.txt installs correctly
3. Review FUTURE_ROADMAP for completeness
4. Check all files for quality

### Phase 5: Discover
1. Identify follow-up work items
2. Suggest next implementations
3. Prioritize by user value

---

## 📝 Research Questions Answered

✅ **Q: What devcontainer configuration is needed?**  
A: Python 3.11 base with Flask, web scraping tools, Google API clients

✅ **Q: How should FUTURE_ROADMAP be expanded?**  
A: Add Phase 5 for agentic tools, expand existing phases with specific implementations

✅ **Q: Is band website feasible?**  
A: Yes, high confidence using GitHub Pages + Jekyll + Netlify CMS

✅ **Q: What MCP tools are needed?**  
A: Google Drive for storage, Email for communication, scrapers for data collection

✅ **Q: How to track finances?**  
A: Expand existing template into Flask UI + SQLite backend

---

## 🔗 References

### Documentation Files Reviewed
- `/README.md`: Repository overview and current capabilities
- `/docs/FUTURE_ROADMAP.md`: Existing future plans
- `/tools/simple_form_ui.py`: Existing form tool pattern
- `/.github/agents/band-manager-agent.md`: Agent configuration
- `/.github/agents/rpi-agent.agent.md`: RPI Agent workflow

### External Resources
- GitHub Pages: https://pages.github.com/
- Netlify CMS: https://www.netlifycms.org/
- Jekyll: https://jekyllrb.com/
- Google Drive API: https://developers.google.com/drive
- BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/
- Flask: https://flask.palletsprojects.com/

---

*Research Complete: 2026-02-19*  
*Status: Ready for Planning Phase*
