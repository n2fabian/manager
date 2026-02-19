# Future Integrations Roadmap 🚀

Planning for SQL Database and RAG System Integration

---

## Overview

This document outlines the future evolution of the Band Manager Agent system, transitioning from a markdown-based system to a hybrid approach using:
- **SQL Database**: For structured data (contacts, financials, inventory)
- **RAG (Retrieval-Augmented Generation)**: For unstructured data queries
- **HVE Core Framework**: Potential application of agentic workflow concepts

---

## Phase 1: Current State (Markdown-Based) ✅

**Status**: Complete

### What We Have
- Markdown files for all data storage
- Template-based workflows
- Manual tracking and updates
- GitHub Copilot integration
- Structured directory organization

### Strengths
- Simple to use and understand
- Version controlled (Git)
- Human-readable
- No dependencies or setup required
- Works offline

### Limitations
- Manual data entry and updates
- No automated queries or analytics
- Limited data relationships
- Harder to generate reports
- No real-time insights

---

## Phase 2: SQL Database Integration

**Status**: Planned  
**Priority**: Medium  
**Estimated Timeline**: 3-6 months

### Database Schema Design

#### Tables

**bands**
```sql
CREATE TABLE bands (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    genre TEXT,
    status TEXT,
    formation_date DATE,
    bio_short TEXT,
    bio_long TEXT,
    website TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);
```

**members**
```sql
CREATE TABLE members (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    role TEXT,
    email TEXT,
    phone TEXT,
    created_at TIMESTAMP
);
```

**band_members**
```sql
CREATE TABLE band_members (
    band_id INTEGER,
    member_id INTEGER,
    role TEXT,
    joined_date DATE,
    PRIMARY KEY (band_id, member_id),
    FOREIGN KEY (band_id) REFERENCES bands(id),
    FOREIGN KEY (member_id) REFERENCES members(id)
);
```

**venues**
```sql
CREATE TABLE venues (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT,
    state TEXT,
    country TEXT,
    capacity INTEGER,
    contact_name TEXT,
    contact_email TEXT,
    contact_phone TEXT,
    website TEXT,
    genre_focus TEXT,
    relationship_status TEXT,
    notes TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);
```

**shows**
```sql
CREATE TABLE shows (
    id INTEGER PRIMARY KEY,
    band_id INTEGER,
    venue_id INTEGER,
    date DATE,
    load_in_time TIME,
    soundcheck_time TIME,
    doors_time TIME,
    set_time TIME,
    set_length INTEGER,
    guarantee_amount DECIMAL(10,2),
    actual_payment DECIMAL(10,2),
    attendance_estimate INTEGER,
    status TEXT,
    notes TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (band_id) REFERENCES bands(id),
    FOREIGN KEY (venue_id) REFERENCES venues(id)
);
```

**contacts**
```sql
CREATE TABLE contacts (
    id INTEGER PRIMARY KEY,
    type TEXT, -- venue, organizer, fan, press, other
    name TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    organization TEXT,
    role TEXT,
    relationship_status TEXT,
    notes TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);
```

**financial_transactions**
```sql
CREATE TABLE financial_transactions (
    id INTEGER PRIMARY KEY,
    band_id INTEGER,
    date DATE,
    type TEXT, -- income, expense
    category TEXT,
    source TEXT,
    description TEXT,
    amount DECIMAL(10,2),
    payment_method TEXT,
    receipt_path TEXT,
    show_id INTEGER,
    created_at TIMESTAMP,
    FOREIGN KEY (band_id) REFERENCES bands(id),
    FOREIGN KEY (show_id) REFERENCES shows(id)
);
```

**merch_items**
```sql
CREATE TABLE merch_items (
    id INTEGER PRIMARY KEY,
    band_id INTEGER,
    item_type TEXT, -- tshirt, hoodie, cd, vinyl, sticker, etc.
    design_name TEXT,
    size TEXT,
    color TEXT,
    quantity INTEGER,
    cost_per_unit DECIMAL(10,2),
    retail_price DECIMAL(10,2),
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    FOREIGN KEY (band_id) REFERENCES bands(id)
);
```

**merch_sales**
```sql
CREATE TABLE merch_sales (
    id INTEGER PRIMARY KEY,
    merch_item_id INTEGER,
    show_id INTEGER,
    date DATE,
    quantity INTEGER,
    total_amount DECIMAL(10,2),
    location TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (merch_item_id) REFERENCES merch_items(id),
    FOREIGN KEY (show_id) REFERENCES shows(id)
);
```

**social_media_stats**
```sql
CREATE TABLE social_media_stats (
    id INTEGER PRIMARY KEY,
    band_id INTEGER,
    platform TEXT,
    date DATE,
    followers INTEGER,
    engagement_rate DECIMAL(5,2),
    posts_count INTEGER,
    notes TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (band_id) REFERENCES bands(id)
);
```

**streaming_stats**
```sql
CREATE TABLE streaming_stats (
    id INTEGER PRIMARY KEY,
    band_id INTEGER,
    platform TEXT,
    date DATE,
    monthly_listeners INTEGER,
    top_track TEXT,
    top_track_plays INTEGER,
    total_plays INTEGER,
    created_at TIMESTAMP,
    FOREIGN KEY (band_id) REFERENCES bands(id)
);
```

### Implementation Approach

1. **Technology Choice**
   - SQLite for local, single-user use (simple, no server)
   - PostgreSQL for multi-user or remote access (scalable)
   - Start with SQLite, migrate to PostgreSQL if needed

2. **Migration Strategy**
   - Create scripts to import existing markdown data
   - Maintain markdown files as backups initially
   - Gradual transition over 2-3 months

3. **Tools & Interfaces**
   - Python scripts for data management
   - Simple CLI for common operations
   - Optional: Web dashboard for visualization
   - Continue using Copilot for queries

4. **Benefits**
   - Automated reports and analytics
   - Complex queries (e.g., "Which venues paid best per attendee?")
   - Relationship tracking between entities
   - Data validation and consistency
   - Easy backup and export

---

## Phase 3: RAG System Integration

**Status**: Planned  
**Priority**: Low-Medium  
**Estimated Timeline**: 6-12 months

### What is RAG?

Retrieval-Augmented Generation allows AI to:
- Query unstructured documents (emails, notes, contracts)
- Find relevant information across all files
- Provide contextual answers based on your data
- Remember conversations and past interactions

### Use Cases

1. **Email Management**
   - "What did [Venue] say about payment last time?"
   - "Find all emails about [City] shows"
   - "Summarize my conversation with [Contact]"

2. **Document Search**
   - "What are the tech requirements for [Venue]?"
   - "Show me notes from shows in [City]"
   - "What's our best-performing social media content?"

3. **Contract Analysis**
   - "What are the terms of the [Venue] agreement?"
   - "Find all venues that do door splits"
   - "Which venues require insurance?"

4. **Historical Insights**
   - "How have our show numbers grown?"
   - "What promotional strategies worked best?"
   - "Which cities have the strongest fan base?"

### Implementation Approach

1. **Vector Database**
   - Use Pinecone, Weaviate, or ChromaDB
   - Store embeddings of all documents
   - Enable semantic search

2. **Document Processing**
   - Convert all markdown to embeddings
   - Index emails, notes, contracts
   - Regular updates for new content

3. **Query Interface**
   - Natural language queries via Copilot
   - CLI for specific searches
   - API for custom integrations

4. **Privacy & Security**
   - Local-first approach when possible
   - Encrypted storage for sensitive data
   - Control what gets indexed

---

## Phase 4: HVE Core Framework Application

**Status**: Research  
**Priority**: Low  
**Estimated Timeline**: 12+ months

### HVE Core Concepts

Based on your mention of HVE Core from your work, exploring how agentic workflows might apply:

### Potential Applications

1. **Specialized Agents**
   - Booking Agent: Handles all venue outreach
   - Finance Agent: Tracks and reports money
   - Promotion Agent: Manages social media
   - Merch Agent: Handles inventory and sales

2. **Agent Coordination**
   - Agents work together on complex tasks
   - Example: "Book a tour" involves multiple agents
   - Shared knowledge base and decision-making

3. **Autonomous Operations**
   - Automated follow-ups
   - Scheduled reporting
   - Proactive recommendations
   - Anomaly detection (e.g., "Sales down this month")

4. **Learning & Improvement**
   - Track what works (successful outreach templates)
   - Adapt strategies based on results
   - Personalize approaches per venue/contact

### Research Questions
- How can agentic workflows improve band management?
- What level of autonomy is helpful vs. overwhelming?
- How to maintain the personal touch with automation?
- What decisions should always involve human judgment?

---

## Migration Checklist

### Before Starting Database Migration

- [ ] Current markdown system is complete and working
- [ ] All templates are refined and proven
- [ ] Regular usage patterns established (know what queries you need)
- [ ] Backup strategy in place
- [ ] Choose database technology (SQLite vs. PostgreSQL)

### Database Migration Steps

- [ ] Design final schema
- [ ] Create database and tables
- [ ] Write import scripts for existing data
- [ ] Test with sample data
- [ ] Create query scripts for common tasks
- [ ] Build reporting templates
- [ ] Parallel run (markdown + database) for 1 month
- [ ] Full cutover to database
- [ ] Archive markdown files

### RAG System Steps

- [ ] Choose vector database
- [ ] Set up embedding pipeline
- [ ] Index existing documents
- [ ] Create query interface
- [ ] Test retrieval accuracy
- [ ] Integrate with Copilot
- [ ] Monitor and refine

---

## Keeping It Simple

**Important Philosophy**: Don't over-engineer!

### When to Migrate
- When markdown becomes limiting
- When you need complex analytics
- When you have significant data volume
- When automation would save substantial time

### When NOT to Migrate
- If current system works fine
- If you don't need complex queries
- If setup time exceeds benefits
- If it makes things harder, not easier

### Rule of Thumb
**Start simple. Add complexity only when you need it.**

The markdown system might be all you ever need. Don't migrate just because you can - migrate when you must.

---

## Cost Considerations

### Database
- SQLite: Free, local
- PostgreSQL: Free (self-hosted) or ~$20-50/month (managed)

### RAG System
- Open source (local): Free but requires setup
- Hosted services: $20-100/month depending on usage

### Development Time
- Database setup: 40-80 hours
- RAG setup: 60-120 hours
- Ongoing maintenance: 5-10 hours/month

### Is it worth it?
Consider if saved time and better insights justify the investment.

---

## Phase 5: Agentic Workflow Tools

**Status**: Planned  
**Priority**: High  
**Estimated Timeline**: Incremental rollout over 6-12 months

### Overview

Expand the band management system with AI-powered tools that automate repetitive tasks, integrate with external services, and provide intelligent assistance for day-to-day operations.

### Tier 1 - High Priority Tools

#### 1. Form Tools Library

**Purpose**: Expand beyond the current `simple_form_ui.py` with reusable form components for various workflows.

**Planned Forms**:
- **Venue Contact Form**: Structured outreach with validation
- **Show Booking Form**: Comprehensive show details entry
- **Financial Entry Form**: Income/expense tracking with categories
- **Merch Order Form**: Track new merchandise orders
- **Band Info Editor**: Update band details with preview

**Technical Approach**:
- Extend existing Flask + WTForms pattern
- Create base form class for consistency
- Modular components (date pickers, file uploads, etc.)
- JSON export for agent consumption
- Real-time validation

**Estimated Effort**: 20-30 hours

---

#### 2. MCP Tools for Shared Storage

**Purpose**: Integrate with cloud storage services to manage band documents, contracts, press photos, and recordings.

##### Google Drive MCP

**Capabilities**:
- Upload files (tech riders, contracts, EPKs) to organized folders
- Download files for local editing
- Generate shareable links for venue booking
- Search across all band documents
- Folder organization (per band, per event type)

**Implementation**:
- Google Drive API v3
- OAuth 2.0 authentication
- Credential storage in `.env` (not committed)
- Rate limiting and error handling
- Python client: `google-api-python-client`

**Security Considerations**:
- Store credentials in `.env` file (excluded from Git)
- Use service account for automated access
- Implement token refresh automatically
- Log all file operations for audit trail

**Example Usage**:
```python
from mcps import GoogleDriveMCP

drive = GoogleDriveMCP('credentials.json')
drive.upload_file('tech-rider.pdf', folder='Combine Harvester/Tech')
share_link = drive.create_share_link(file_id)
# Send share_link to venue via email
```

**Estimated Effort**: 15-20 hours

##### Dropbox MCP (Alternative/Additional)

**Capabilities**: Similar to Google Drive
- May be preferred by some collaborators
- Simpler API in some cases
- Good for large media files

**Estimated Effort**: 10-15 hours

---

#### 3. Web Scraping & Browsing Tools

##### Instagram Band Discovery

**Purpose**: Find bands, track growth, identify tour partners and promotional opportunities.

**Capabilities**:
- Search by hashtags (#metalcore, #germanmetal, #livemusic)
- Extract band profiles and follower counts
- Monitor follower growth over time
- Identify potential tour partners by genre and location
- Analyze engagement rates

**Implementation Approaches**:

**Option A: Instagram Graph API** (Recommended if accessible)
- Official API with proper authentication
- Rate limits but reliable
- Requires business account

**Option B: Web Scraping** (If API unavailable)
- Use `selenium` for JavaScript rendering
- Respect rate limits (2-3 seconds between requests)
- Parse public profile pages only
- Risk: May violate terms of service

**Ethical Guidelines**:
- Only scrape public information
- Respect robots.txt
- Implement rate limiting
- Do not store personal data
- Comply with GDPR and privacy laws

**Estimated Effort**: 25-40 hours

##### Backstage Pro Crawler

**Purpose**: Discover venues, festivals, and events for booking opportunities.

**Capabilities**:
- Scrape venue databases by city and genre
- Extract contact information
- Track event calendars
- Identify booking opportunities
- Export to contact management system

**Implementation**:
- `requests` + `BeautifulSoup` for HTML parsing
- Rate limiting (1-2 seconds between requests)
- Respect robots.txt
- Cache results to minimize requests

**Ethical Considerations**:
- Check Backstage Pro terms of service
- May need to contact site owner for permission
- Only use publicly available information
- Do not overload servers

**Estimated Effort**: 20-30 hours

##### General Web Scraper Framework

**Purpose**: Flexible scraper for various band management tasks.

**Use Cases**:
- Venue capacity from venue websites
- Festival lineup announcements
- Ticket sale platforms
- Music news and reviews
- Streaming statistics (if no API)

**Framework Features**:
- Configurable target URLs
- Custom parsing rules
- Rate limiting and retry logic
- Error handling and logging
- Data export to JSON/CSV

**Estimated Effort**: 15-25 hours

---

#### 4. Financial Tracking Tool

**Purpose**: Comprehensive band finance management beyond the markdown template.

**Features**:

**Income Tracking**:
- Show guarantees and door splits
- Merch sales (per show and online)
- Streaming royalties
- Grants and sponsorships
- Other income sources

**Expense Tracking**:
- Equipment purchases and repairs
- Travel costs (fuel, tolls, parking)
- Production costs (recording, mixing)
- Marketing and promotion
- Venue fees and deposits

**Reporting**:
- Monthly profit/loss statements
- Per-show profitability analysis
- Category-based spending reports
- Tax preparation summaries
- Year-over-year comparisons

**Implementation**:
- Flask web UI with dashboard
- SQLite database for storage
- Integration with existing `financial-tracking.md` template
- CSV/PDF export for accountants
- Receipt attachment and storage
- Multi-band support (separate budgets)

**Database Schema**:
```sql
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY,
    band_id INTEGER,
    date DATE,
    type TEXT CHECK(type IN ('income', 'expense')),
    category TEXT,
    description TEXT,
    amount DECIMAL(10,2),
    payment_method TEXT,
    receipt_path TEXT,
    show_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Estimated Effort**: 30-40 hours

---

#### 5. Email Automation MCP

**Purpose**: Send venue outreach, follow-ups, and confirmations with templates.

**Capabilities**:
- Gmail API integration
- Template-based email generation (use existing `venue-email-template.md`)
- Scheduled sending (follow-ups after 1 week, 2 weeks)
- Response tracking (read receipts, replies)
- Attachment support (tech riders, EPKs, contracts)
- Bulk sending with personalization
- Email campaign management

**Implementation**:
- Gmail API with OAuth 2.0
- Python `email` library for composition
- Template engine (Jinja2) for personalization
- Queue system for scheduled emails
- Database for tracking sent emails

**Example Workflow**:
1. Select venue from contact list
2. Choose email template
3. Customize with band-specific details
4. Attach tech rider and EPK
5. Schedule send time
6. Track opens and replies

**Security**:
- OAuth credentials in `.env`
- Rate limiting to avoid spam flags
- Unsubscribe links if bulk sending

**Estimated Effort**: 25-35 hours

---

### Tier 2 - Medium Priority Tools

#### 6. Social Media Monitoring

**Purpose**: Track band mentions, engagement, and growth across platforms.

**Platforms**:
- **Spotify for Artists API**: Monthly listeners, top tracks, playlist additions
- **Instagram Insights API**: Follower growth, post engagement, story views
- **Facebook Page Analytics**: Reach, engagement, audience demographics
- **YouTube Analytics**: View counts, watch time, subscriber growth

**Features**:
- Automated data collection (daily or weekly)
- Trend visualization and reporting
- Anomaly detection (viral posts, sudden drops)
- Competitor comparison
- Content performance analysis

**Estimated Effort**: 40-50 hours

---

#### 7. Calendar & Scheduling Integration

**Purpose**: Centralize show dates, rehearsals, and deadlines.

**Capabilities**:
- Google Calendar integration
- Automated reminders (load-in time, soundcheck, doors)
- Travel time calculations (Google Maps API)
- Conflict detection (double-bookings)
- Export to iCal for mobile devices
- Shared calendars with band members

**Estimated Effort**: 20-30 hours

---

#### 8. Press Kit Generator

**Purpose**: Automated EPK (Electronic Press Kit) creation.

**Features**:
- PDF generation from markdown content
- Asset management (photos, logos, music files)
- Version control for different venues/events
- Customizable templates
- QR codes for digital sharing
- One-click updates when band info changes

**Estimated Effort**: 25-35 hours

---

#### 9. Contract Management

**Purpose**: Track agreements, deadlines, and obligations.

**Features**:
- Template library (venue contracts, promoter agreements, rider templates)
- Digital signature integration (DocuSign API)
- Version tracking and comparison
- Expiration alerts
- Payment milestone tracking
- Archive of signed contracts

**Estimated Effort**: 30-40 hours

---

### Tier 3 - Long-term Infrastructure

#### 10. Multi-Agent Orchestration

**Purpose**: Specialized agents that work together on complex tasks.

**Specialized Agents**:
- **Booking Agent**: Handles venue outreach, negotiation, confirmation
- **Finance Agent**: Tracks money, generates reports, alerts on issues
- **Promotion Agent**: Manages social media, press releases, fan engagement
- **Merch Agent**: Handles inventory, sales, restock alerts

**Coordination**:
- Shared memory/context via database
- Agent communication protocols
- Task delegation and handoffs
- Conflict resolution
- Central orchestrator (RPI Agent or similar)

**Based on**: HVE Core Framework concepts (from research work)

**Estimated Effort**: 80-120 hours

---

#### 11. RAG System Enhancement

**Purpose**: Make the existing RAG system (Phase 3) agent-aware.

**Agent-Specific Features**:
- Query routing to appropriate agents
- Context injection for agent tools
- Agent memory persistence
- Cross-agent knowledge sharing
- Learning from agent interactions

**Estimated Effort**: 60-80 hours (in addition to Phase 3)

---

#### 12. API Gateway

**Purpose**: Centralized access point for all external integrations.

**Features**:
- Rate limiting and caching
- Error handling and retry logic
- Monitoring and logging
- Authentication management
- Request/response transformation
- Service health checks

**Estimated Effort**: 40-60 hours

---

### Implementation Priorities Summary

| Tool | Priority | Effort (hours) | Dependencies |
|------|----------|----------------|--------------|
| Form Tools Library | High | 20-30 | None |
| Financial Tracking Tool | High | 30-40 | SQLite (Phase 2) |
| Google Drive MCP | High | 15-20 | API credentials |
| Email Automation MCP | High | 25-35 | Gmail API credentials |
| Instagram Scraper | High | 25-40 | API access or ethical approval |
| Backstage Scraper | High | 20-30 | Terms of service review |
| General Scraper Framework | Medium | 15-25 | None |
| Social Media Monitoring | Medium | 40-50 | API credentials |
| Calendar Integration | Medium | 20-30 | Google Calendar API |
| Press Kit Generator | Medium | 25-35 | None |
| Contract Management | Medium | 30-40 | None |
| Multi-Agent Orchestration | Low | 80-120 | Phase 2, 3, other tools |
| RAG Enhancement | Low | 60-80 | Phase 3 complete |
| API Gateway | Low | 40-60 | Multiple tools in place |

**Total Estimated Effort**: 470-690 hours (approximately 3-6 months part-time)

---

## Phase 6: Web Presence & Band Websites

**Status**: Ready to Implement  
**Priority**: Medium-High  
**Estimated Timeline**: 2-4 weeks per band

### Overview

Create professional band websites with non-technical content management, hosted for free on GitHub Pages with Netlify CMS for easy updates.

### Technology Stack

**Hosting**: GitHub Pages (free, reliable, custom domain support)  
**Static Site Generator**: Jekyll (native GitHub Pages support)  
**CMS**: Netlify CMS (free, Git-backed, non-technical friendly)  
**Template**: HTML5 UP "Spectral" or similar (free, responsive, music-focused)

### Features

#### Public-Facing Pages

**Home Page**:
- Hero section with band photo
- Short bio
- Latest news/announcements
- Call-to-action (listen, buy tickets, etc.)

**Music Page**:
- Spotify/Apple Music embeds
- Streaming links
- Release history
- Music videos

**Shows Page**:
- Upcoming shows with ticket links
- Past show archive
- Show photos/videos

**Media Page**:
- Press photos (downloadable)
- Videos
- Press coverage
- Social media feeds

**Contact/Booking Page**:
- Booking inquiry form
- Management contact
- Social media links
- Newsletter signup

#### Admin Interface (Netlify CMS)

**Non-Technical Capabilities**:
- Add/edit/delete pages via web UI
- Upload images with drag-and-drop
- Manage show dates (add, edit, remove)
- Update bio and news
- Toggle page sections on/off
- Preview changes before publishing

**Limited Customization**:
- Change hero image
- Update colors (primary, secondary)
- Modify text content
- Rearrange sections (predefined layouts)

**What Non-Technical Users Cannot Do**:
- Major layout changes
- Add new page types
- Custom JavaScript
- Advanced styling

#### Backend Access (For Fabi)

**Full Control Via Git**:
- Direct HTML/CSS/JavaScript editing
- Custom functionality additions
- Advanced styling and layout
- Access to all configuration files

**Analytics & Tracking**:
- Google Analytics integration
- Request tracking via GA or Plausible Analytics
- Visitor demographics and behavior
- Traffic sources and referrals
- Popular content analysis

**Custom Features**:
- Mailing list integration (Mailchimp, ConvertKit)
- E-commerce (Shopify, Big Cartel) for merch
- Custom contact forms
- Social media integration
- Event calendar widgets

### Implementation for Combine Harvester

**Content from Existing Data** (`/wiki/bands/combine-harvester.md`):
- Band name, genre, members
- Bios (short and long)
- Streaming links (Spotify: https://open.spotify.com/artist/3GeTwZPCOlNlRw34hCJTx3)
- Social media (Instagram: combineharvester_band)

**Initial Pages**:
1. Home (hero + bio)
2. Music (Spotify embed)
3. Shows (empty initially, ready for updates)
4. Contact (booking form + social links)

**Deployment Steps**:
1. Create Jekyll site in `/website` directory
2. Configure GitHub Pages in repository settings
3. Add Netlify CMS configuration
4. Push to GitHub
5. Enable Netlify Identity for CMS access
6. Optional: Configure custom domain (combineharvester.band, ~$12/year)

**Ongoing Maintenance**:
- Band members add show dates via CMS
- Upload photos via CMS
- Update news/announcements
- Fabi handles technical updates via Git

### Template Selection

**Recommended: HTML5 UP "Spectral"**
- Clean, modern design
- Music/entertainment focused
- Mobile responsive
- Free license
- Easy customization

**Alternatives**:
- Jekyll theme "Minimal Mistakes" (blog-focused)
- Colorlib "MusicHub" (music-specific)
- Custom theme based on Bootstrap

### Custom Domain Setup (Optional)

**Domain Options**:
- `combineharvester.band` (most professional, ~$30/year)
- `combineharvester.com` (~$12/year)
- `combineharvester.rocks` (fun, ~$15/year)
- Free subdomain: `combine-harvester.github.io`

**Configuration**:
1. Purchase domain from Namecheap, Google Domains, etc.
2. Configure DNS with CNAME record
3. Update GitHub Pages settings
4. Enable HTTPS (automatic via Let's Encrypt)

### Analytics & Insights

**Free Options**:
- **Google Analytics**: Comprehensive, industry standard
- **Plausible Analytics**: Privacy-focused, simpler
- **Cloudflare Analytics**: If using Cloudflare CDN

**Metrics to Track**:
- Page views and unique visitors
- Traffic sources (social, search, direct)
- Popular pages and content
- Visitor location and demographics
- Device and browser breakdown
- Conversion rates (newsletter signup, ticket clicks)

### Mockup Status

**Current Status**: Full mockup created in `/website` directory  
**Deployment Ready**: Yes  
**Next Steps**:
1. Review mockup with band
2. Add initial content
3. Test locally with Jekyll
4. Deploy to GitHub Pages
5. Configure CMS access
6. Hand off to band members

**Estimated Effort**: 
- Initial setup: 10-15 hours
- Content population: 5-10 hours
- Testing and refinement: 5 hours
- **Total**: 20-30 hours per band

---

## Questions to Answer Before Migrating

1. **Is the markdown system limiting you?**
   - If no → stick with markdown
   - If yes → consider migration

2. **What specific problems would a database solve?**
   - List them specifically
   - Ensure they're real needs, not nice-to-haves

3. **Do you have time for setup and maintenance?**
   - Be honest about capacity
   - Consider ongoing updates needed

4. **Would automation improve your workflow?**
   - Or would it make things more complicated?
   - Start with smallest useful automation

5. **What's the ROI?**
   - Time saved vs. time invested
   - Better decisions vs. complexity cost

---

## Getting Started (When Ready)

### Learn First
- [ ] SQL basics (if not familiar)
- [ ] Vector databases and RAG concepts
- [ ] Python for scripting (or your preferred language)

### Start Small
- [ ] Migrate one table (e.g., shows)
- [ ] Build one report
- [ ] Test thoroughly
- [ ] Expand gradually

### Resources
- SQLite Tutorial: https://www.sqlitetutorial.net/
- RAG Basics: Research current best practices
- LangChain: For RAG implementation
- Python + SQLAlchemy: For database ORM

---

## Final Thoughts

This roadmap is aspirational. The markdown system you have now is complete and functional. Use it, refine it, let it prove its value. Only move to more complex systems when you hit real limitations.

**Remember**: The best system is the one you actually use. Simple and used beats complex and abandoned.

*Rock on!* 🤘

---

*Last Updated: 2026-02-19*  
*Status: Planning/Research Phase - Expanded with Agentic Workflow Tools (Phase 5) and Web Presence (Phase 6)*
