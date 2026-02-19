# 🤘 Band Manager Agent Repository

**Agent-Powered Management System for Near's 2 Far & Combine Harvester**

> *"Managing bands like a beast, with the precision of a double bass pedal."*  
> — Fabi

---

## Welcome to Your Band Management HQ

This repository is your AI-powered command center for managing all aspects of your metal bands. Built with GitHub Copilot in mind, this system helps you handle everything from booking shows to tracking merch sales, all while keeping that metal spirit alive.

### 🎸 Bands Under Management
- **Near's 2 Far** - Metal
- **Combine Harvester** - Metal

**Manager**: Fabian Wohlgemuth (Fabi) - Drums & Vocals

---

## 🚀 Quick Start

### Development Environment Setup

**Using Dev Container (Recommended)**:
1. Install [VS Code](https://code.visualstudio.com/) and [Docker](https://www.docker.com/)
2. Install the "Dev Containers" extension in VS Code
3. Open this repository in VS Code
4. Click "Reopen in Container" when prompted (or use Command Palette: "Dev Containers: Reopen in Container")
5. Container will build automatically with Python, Flask, and all dependencies

**Manual Setup**:
1. Install Python 3.11+
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and configure as needed

### For First-Time Setup
1. Clone this repo to your local machine
2. Set up development environment (see above)
3. Explore the structure below
4. Fill in band-specific information in `/wiki/bands/`
5. Add your contacts to `/wiki/contacts/`
6. Use templates in `/docs/templates/` for outreach
7. Start booking shows and crushing it! 🤘

### Key Files to Start With
- **📧 Venue Email Template**: `/docs/templates/venue-email-template.md`
- **🎤 Tech Rider**: `/docs/templates/tech-rider.md`
- **📋 Band Info**: `/wiki/bands/nears-2-far.md` & `/wiki/bands/combine-harvester.md`
- **📞 Contacts**: `/wiki/contacts/venues.md`
- **🗺️ Roadmap**: `/docs/FUTURE_ROADMAP.md` - See planned features and tools

---

## 📁 Repository Structure

```
manager/
├── .devcontainer/
│   └── devcontainer.json           # Dev container configuration
│
├── .github/
│   └── agents/
│       ├── band-manager-agent.md   # Main agent instructions
│       └── rpi-agent.agent.md      # RPI orchestrator agent
│
├── config/
│   └── agent-config.json           # Agent configuration
│
├── mcps/                           # Model Context Protocol tools
│   ├── base_mcp.py                 # Base class for MCPs
│   ├── google_drive_mcp.py         # Google Drive integration (skeleton)
│   └── email_mcp.py                # Email automation (skeleton)
│
├── tools/                          # Utilities and tools
│   ├── simple_form_ui.py           # Flask form for data collection
│   └── scrapers/                   # Web scraping tools
│       ├── base_scraper.py         # Base scraper with ethical guidelines
│       ├── instagram_scraper.py    # Band discovery (skeleton)
│       └── backstage_scraper.py    # Venue/event discovery (skeleton)
│
├── website/                        # Combine Harvester band website
│   ├── _config.yml                 # Jekyll configuration
│   ├── _layouts/                   # Page layouts
│   ├── assets/                     # CSS, JS, images
│   ├── admin/                      # Netlify CMS
│   └── *.html                      # Site pages
│
├── wiki/                           # Knowledge base
│   ├── bands/                      # Band information
│   ├── contacts/                   # CRM
│   └── events/                     # Event documentation
│
├── docs/                           # Documentation
│   ├── FUTURE_ROADMAP.md           # Planned features and integrations
│   ├── templates/                  # Reusable templates
│   └── workflows/                  # Process documentation
│
├── tasks/                          # Task tracking
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variable template
└── README.md                       # You are here
```

---

## 🎯 Core Capabilities

### 1. 🎪 Show Booking & Venue Relations
- Professional email templates for venue outreach
- Tech rider generation
- Booking workflow documentation
- Venue relationship tracking

**Start here**: `/docs/templates/venue-email-template.md`

### 2. 👕 Merch Management
- Inventory tracking system
- Sales monitoring
- Vendor contact management
- Restock alerts

**Start here**: `/docs/templates/merch-inventory.md`

### 3. 💰 Financial Tracking
- Income/expense monitoring
- Monthly financial reports
- Tax preparation support
- Cashflow visibility

**Start here**: `/docs/templates/financial-tracking.md`

### 4. 📣 Music Promotion
- Social media strategy
- Fan engagement tracking
- Web visibility monitoring
- Content planning

**Start here**: `/wiki/contacts/fans.md`

### 5. 📇 CRM (Customer Relationship Management)
- Venue contacts and relationships
- Event organizer/promoter database
- Fan engagement tracking
- Industry networking

**Start here**: `/wiki/contacts/`

### 6. 🌐 Web Visibility
- Platform presence tracking
- Analytics monitoring
- SEO optimization
- Content performance

### 7. 🎸 General Management
Everything else a manager or label would do:
- Tour planning
- Equipment inventory
- Press kit maintenance
- Contract management

---

## 🤖 Agentic Workflow Tools

This repository now includes frameworks for AI-powered automation and external integrations:

### MCP (Model Context Protocol) Tools

**Location**: `/mcps/`

Integrate with external services to automate band management tasks:

- **Google Drive MCP**: Upload/download band documents, share files with venues, organize press kits
- **Email MCP**: Send automated venue outreach, schedule follow-ups, track responses
- **Future**: Dropbox, cloud storage, calendar integration

**Status**: Framework implemented, full functionality requires API credentials. See `/mcps/README.md` for setup instructions.

### Web Scraping Tools

**Location**: `/tools/scrapers/`

Discover bands, venues, and booking opportunities:

- **Instagram Scraper**: Find bands by hashtag, track follower growth, analyze engagement
- **Backstage Pro Scraper**: Discover venues and events by location/genre
- **Base Scraper**: Ethical scraping framework with rate limiting and robots.txt respect

**Status**: Framework implemented with ethical guidelines. Full implementation requires API access and legal review. See `/tools/scrapers/README.md` for details.

### Band Website

**Location**: `/website/`

Professional band website for Combine Harvester:

- **Technology**: Jekyll static site + Netlify CMS
- **Hosting**: GitHub Pages (free, custom domain support)
- **Features**: Show calendar, Spotify embed, photo gallery, non-technical content management
- **Status**: Deployment-ready mockup. See `/website/DEPLOYMENT.md` for setup.

### Development Environment

**Devcontainer**: Pre-configured Python 3.11 environment with all dependencies
- GitHub Copilot integration
- Flask, BeautifulSoup, Google API clients pre-installed
- VS Code extensions for Python and Markdown
- One-click setup with Docker

**Start here**: Open repository in VS Code and select "Reopen in Container"

---

## 🔥 Workflows

### Booking a Show
Follow the complete workflow: `/docs/workflows/show-booking-workflow.md`

**Quick steps**:
1. Research venue → Add to `/wiki/contacts/venues.md`
2. Customize email from `/docs/templates/venue-email-template.md`
3. Attach tech rider from `/docs/templates/tech-rider.md`
4. Track in `/tasks/current-tasks.md`
5. Follow up after 1-2 weeks
6. Confirm and promote!

### Managing Merch
1. Track inventory in `/docs/templates/merch-inventory.md`
2. Set restock alerts
3. Record sales after each show
4. Update financial tracking

### Tracking Finances
1. Record all income/expenses immediately
2. Update monthly in `/docs/templates/financial-tracking.md`
3. Review cashflow regularly
4. Keep receipts for taxes

---

## 🤖 AI Agent Integration

This repository is designed to work seamlessly with GitHub Copilot and AI agents.

### Agent Personality
Your Band Manager Agent is:
- Professional but not corporate (we're metal, not suits)
- Direct and efficient
- Authentic to the metal community
- Focused on results

### Agent Instructions
Main agent documentation: `.github/agents/band-manager-agent.md`

### Future Enhancements

See comprehensive roadmap: `/docs/FUTURE_ROADMAP.md`

**Planned (Phase 5 - Agentic Tools)**:
- Form tools library for various workflows
- Google Drive and email automation
- Instagram and venue discovery scrapers
- Financial tracking web UI
- Social media monitoring
- Calendar and scheduling integration

**Long-term (Phases 2-4)**:
- SQL Database for structured data
- RAG System for intelligent document search
- Multi-agent orchestration
- Advanced analytics and insights

---

## 📝 How to Use This System

### Daily Tasks
- Check and respond to booking inquiries
- Update any new contacts in CRM
- Record any financial transactions
- Post social media content

### Weekly Review
- Review upcoming shows
- Check merch inventory
- Update task list
- Plan content for next week

### Monthly Review
- Financial report
- Analytics review
- Update band info if needed
- Plan next month's strategy

---

## 🎓 Tips for Success

1. **Keep Info Updated**: The system is only as good as the data you put in
2. **Be Consistent**: Use the templates and workflows
3. **Track Everything**: Shows, expenses, contacts - it all matters
4. **Build Relationships**: CRM isn't just data, it's people
5. **Stay Professional**: Even in metal, professionalism gets you booked
6. **Have Fun**: This is about music, not just business

---

## 🔮 Future Roadmap

### Phase 1 (Current)
- ✅ Repository structure
- ✅ Band information wiki
- ✅ Email templates
- ✅ Tech rider
- ✅ CRM system
- ✅ Workflow documentation

### Phase 2 (Next)
- [ ] Automated financial reports
- [ ] Show calendar integration
- [ ] Social media content calendar
- [ ] Analytics dashboard

### Phase 3 (Future)
- [ ] SQL database integration
- [ ] RAG system for knowledge queries
- [ ] Automated follow-up reminders
- [ ] AI-powered insights and recommendations

---

## 🤘 The Metal Manager Philosophy

**Work hard. Play loud. Stay organized.**

Running a band is like drumming - it requires:
- **Timing**: Know when to push and when to wait
- **Rhythm**: Consistent effort beats sporadic hustle
- **Power**: Go all-in when it matters
- **Control**: Keep track of the details
- **Passion**: Never forget why you started

This system handles the boring stuff so you can focus on the music.

---

## 📞 Contact & Support

**Manager**: Fabian Wohlgemuth (Fabi)  
**Role**: Drums & Vocals  
**Bands**: Near's 2 Far, Combine Harvester

For questions about this system or agent setup, refer to:
- Agent instructions: `.github/agents/band-manager-agent.md`
- Configuration: `config/agent-config.json`

---

## 🎸 Let's Do This!

You've got the tools. You've got the talent. Now go book some shows, sell some merch, and bring the metal to the masses.

**Remember**: Every legendary band started with one show, one fan, one step at a time.

*Keep it heavy.* 🤘🥁🎸

---

*Last Updated: 2026-02-19*  
*Version: 2.0.0 - Agentic Workflows*  
*Built with ❤️ and 🤘*
