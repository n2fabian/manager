<!-- markdownlint-disable-file -->
# Implementation Plan: Agentic Workflow Transformation

**Plan Date**: 2026-02-19  
**Task**: Transform repository into base for agentic workflows  
**Research Document**: `.copilot-tracking/research/2026-02-19/agentic-workflow-transformation-research.md`  
**Planning Log**: `.copilot-tracking/plans/logs/2026-02-19/agentic-workflow-transformation-log.md`

---

## Overview and Objectives

### User Requirements (Source: Problem Statement)
1. Create a devcontainer for autonomous agent work
2. Expand FUTURE_ROADMAP.md to include agentic workflow improvements
3. Include tools similar to form tool (simple_form_ui.py)
4. Add MCPs for shared storage (Google Drive)
5. Add web browsing tools (Instagram, Backstage Pro)
6. Create band website mockup for Combine Harvester (if confident)
7. Add financial tracking tool to future scope

### Derived Objectives (Reasoning)
- **Devcontainer**: Enable consistent, reproducible development environment for all contributors
- **FUTURE_ROADMAP**: Provide clear roadmap for future agent sessions with actionable PBIs
- **Tool Framework**: Establish patterns for creating additional agentic tools
- **Website Mockup**: Demonstrate free hosting capability and admin-friendly CMS
- **Documentation**: Ensure all changes are well-documented for future sessions

### Context Summary

**Discovered Instructions Files**:
- `.github/agents/band-manager-agent.md`: Main agent for band management operations
- `.github/agents/rpi-agent.agent.md`: 5-phase iterative workflow orchestrator
- `.github/copilot-instructions.md`: Not found (may need to check)

**Current State**:
- Markdown-based band management system
- Single Python tool (simple_form_ui.py) for form collection
- No devcontainer or dependency management
- FUTURE_ROADMAP exists but limited to SQL/RAG plans
- No MCP implementations
- No web scraping tools

**Technology Stack**:
- Python 3.x (assumed, no version pinning)
- Flask web framework
- WTForms for form handling
- Markdown for documentation
- Git for version control

---

## Implementation Checklist

### Phase 1: Development Environment Setup
<!-- parallelizable: false -->

- [ ] **1.1** Create `.devcontainer/devcontainer.json`
  - Configure Python 3.11 base image
  - Add GitHub Copilot extension
  - Configure port forwarding (5000 for Flask)
  - Set post-create command
  - Lines: See details 1-50

- [ ] **1.2** Create `requirements.txt`
  - Add Flask, WTForms, MarkupSafe
  - Add requests, beautifulsoup4 for web scraping
  - Add Google API client libraries
  - Add testing and utility libraries
  - Lines: See details 51-100

- [ ] **1.3** Create `.env.example`
  - Template for SECRET_KEY
  - Placeholder for Google API credentials
  - Document environment variables
  - Lines: See details 101-120

- [ ] **1.4** Update `.gitignore`
  - Add .env to ignored files
  - Add Python virtual environment patterns
  - Add devcontainer build artifacts
  - Lines: See details 121-140

**Dependencies**: None  
**Success Criteria**: Devcontainer builds without errors, requirements install successfully

---

### Phase 2: FUTURE_ROADMAP Expansion
<!-- parallelizable: false -->

- [ ] **2.1** Backup existing FUTURE_ROADMAP.md
  - Create copy for reference
  - Lines: See details 141-145

- [ ] **2.2** Add Phase 5: Agentic Workflow Tools
  - Form tools library
  - MCP tools (Google Drive, Email)
  - Web scraping tools (Instagram, Backstage Pro)
  - Financial tracking tool
  - Lines: See details 146-350

- [ ] **2.3** Expand Phase 2 with Financial Tool Details
  - Integration with existing templates
  - SQLite backend specifications
  - Flask UI design
  - Lines: See details 351-400

- [ ] **2.4** Add Phase 6: Web Presence & Band Website
  - GitHub Pages hosting details
  - Netlify CMS integration
  - Template selection and customization
  - Deployment workflow
  - Lines: See details 401-500

- [ ] **2.5** Add Implementation Priorities Section
  - Tier 1 (High Priority)
  - Tier 2 (Medium Priority)
  - Tier 3 (Long-term)
  - Lines: See details 501-550

**Dependencies**: Phase 1 complete  
**Success Criteria**: FUTURE_ROADMAP is comprehensive, actionable, and well-structured

---

### Phase 3: MCP Tool Framework
<!-- parallelizable: true -->

- [ ] **3.1** Create `mcps/` directory structure
  - Create `mcps/README.md` with overview
  - Create `mcps/base_mcp.py` with base class
  - Lines: See details 551-600

- [ ] **3.2** Create Google Drive MCP skeleton
  - File: `mcps/google_drive_mcp.py`
  - Base implementation with method stubs
  - Documentation and usage examples
  - Lines: See details 601-700

- [ ] **3.3** Create Email MCP skeleton
  - File: `mcps/email_mcp.py`
  - Gmail API integration structure
  - Template support
  - Lines: See details 701-750

**Dependencies**: Phase 1 complete (for imports)  
**Success Criteria**: Framework is clear, extensible, and well-documented

---

### Phase 4: Web Scraper Framework
<!-- parallelizable: true -->

- [ ] **4.1** Create `tools/scrapers/` directory structure
  - Create `tools/scrapers/README.md`
  - Create `tools/scrapers/base_scraper.py`
  - Lines: See details 751-800

- [ ] **4.2** Create Instagram scraper skeleton
  - File: `tools/scrapers/instagram_scraper.py`
  - Method stubs for profile, hashtag search
  - Rate limiting and ethics notes
  - Lines: See details 801-850

- [ ] **4.3** Create Backstage Pro scraper skeleton
  - File: `tools/scrapers/backstage_scraper.py`
  - Method stubs for venue, event discovery
  - Documentation
  - Lines: See details 851-900

**Dependencies**: Phase 1 complete (for imports)  
**Success Criteria**: Framework establishes clear patterns for scraper development

---

### Phase 5: Band Website Mockup
<!-- parallelizable: true -->

- [ ] **5.1** Create `website/` directory structure
  - Create README.md with deployment guide
  - Lines: See details 901-950

- [ ] **5.2** Create Jekyll configuration
  - File: `website/_config.yml`
  - Basic site configuration for Combine Harvester
  - Lines: See details 951-1000

- [ ] **5.3** Create home page template
  - File: `website/index.html`
  - Hero section, bio, call-to-action
  - Lines: See details 1001-1100

- [ ] **5.4** Create music page
  - File: `website/music.html`
  - Spotify embed, streaming links
  - Lines: See details 1101-1150

- [ ] **5.5** Create shows page
  - File: `website/shows.html`
  - Upcoming and past shows listing
  - Lines: See details 1151-1200

- [ ] **5.6** Create Netlify CMS configuration
  - File: `website/admin/config.yml`
  - Content models for shows, pages
  - Lines: See details 1201-1300

- [ ] **5.7** Create deployment guide
  - File: `website/DEPLOYMENT.md`
  - Step-by-step GitHub Pages setup
  - Custom domain configuration
  - Lines: See details 1301-1400

**Dependencies**: None  
**Success Criteria**: Website is ready to deploy, admin panel is configured, guide is complete

---

### Phase 6: Documentation Updates
<!-- parallelizable: false -->

- [ ] **6.1** Update main README.md
  - Add devcontainer usage instructions
  - Link to FUTURE_ROADMAP
  - Mention new tools and frameworks
  - Lines: See details 1401-1450

- [ ] **6.2** Update GETTING_STARTED.md (if exists)
  - Add devcontainer setup steps
  - Environment variable configuration
  - Lines: See details 1451-1500

- [ ] **6.3** Create CONTRIBUTING.md
  - Guidelines for adding new MCPs
  - Guidelines for adding new scrapers
  - Guidelines for adding new tools
  - Lines: See details 1501-1600

**Dependencies**: All previous phases complete  
**Success Criteria**: Documentation is clear, complete, and actionable

---

## Planning Log Reference

**Log File**: `.copilot-tracking/plans/logs/2026-02-19/agentic-workflow-transformation-log.md`

**Key Decisions**:
- Devcontainer: Python 3.11 (modern, stable, good async support)
- FUTURE_ROADMAP: Expand rather than replace (preserve existing work)
- MCPs: Framework + skeletons (implementation deferred to future sessions)
- Website: Full mockup (high confidence in implementation)

**Deviations from Research**:
- None expected; plan follows research recommendations

**Unaddressed Research Items**:
- Actual MCP implementations (deferred to future)
- Working scrapers (deferred to future)
- Database migration (already in FUTURE_ROADMAP)
- RAG system (already in FUTURE_ROADMAP)

---

## Dependencies

### Discovered Skills
- Python development
- Flask web framework
- Git version control
- Markdown documentation
- Jekyll static site generation (for website)

### External Dependencies
- GitHub Pages (for website hosting)
- Netlify CMS (for admin interface)
- Google APIs (for future MCP implementations)

### Internal Dependencies
- Phase 1 must complete before Phase 2, 6
- Phases 3, 4, 5 can run in parallel after Phase 1

---

## Success Criteria

### Functional Requirements
- ✅ Devcontainer builds and runs successfully
- ✅ All dependencies install without errors
- ✅ FUTURE_ROADMAP is comprehensive and actionable
- ✅ MCP framework is clear and extensible
- ✅ Scraper framework is well-documented
- ✅ Band website is ready for deployment
- ✅ All documentation is complete

### Non-Functional Requirements
- ✅ Code follows existing repository patterns
- ✅ Documentation uses consistent markdown style
- ✅ No breaking changes to existing functionality
- ✅ Security: No credentials committed to Git
- ✅ Minimal changes principle adhered to

### Quality Criteria
- ✅ All markdown passes linting
- ✅ Python code follows PEP 8 style
- ✅ File structure is logical and organized
- ✅ Comments explain non-obvious decisions
- ✅ Examples are provided where helpful

---

## Timeline Estimate

**Total Estimated Time**: 4-6 hours

- Phase 1: 1 hour (devcontainer, requirements, env config)
- Phase 2: 2 hours (FUTURE_ROADMAP expansion)
- Phase 3: 45 minutes (MCP framework)
- Phase 4: 45 minutes (scraper framework)
- Phase 5: 2 hours (band website mockup)
- Phase 6: 30 minutes (documentation updates)

**Note**: This is for RPI Agent orchestration time; actual implementation may be delegated to phase-implementor subagents.

---

## Risk Assessment

### Low Risk
- ✅ Devcontainer creation (well-documented standard)
- ✅ Requirements.txt (straightforward dependencies)
- ✅ Documentation updates (clear requirements)

### Medium Risk
- ⚠️ FUTURE_ROADMAP expansion (must balance detail vs. brevity)
- ⚠️ Website mockup (design decisions require judgment)

### Mitigation Strategies
- Use existing FUTURE_ROADMAP structure as template
- Select proven, well-documented website template
- Keep framework implementations simple and extensible

---

## Notes

- This plan focuses on **structure and framework** rather than full implementation
- MCPs and scrapers are **skeletons** - actual functionality deferred
- Band website is **deployment-ready mockup** but may need content refinement
- All changes maintain **backward compatibility**
- No changes to existing `/tools/simple_form_ui.py`

---

*Plan Created: 2026-02-19*  
*Status: Ready for Implementation*
