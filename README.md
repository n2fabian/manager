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

### For First-Time Setup
1. Clone this repo to your local machine
2. Explore the structure below
3. Fill in band-specific information in `/wiki/bands/`
4. Add your contacts to `/wiki/contacts/`
5. Use templates in `/docs/templates/` for outreach
6. Start booking shows and crushing it! 🤘

### Key Files to Start With
- **📧 Venue Email Template**: `/docs/templates/venue-email-template.md`
- **🎤 Tech Rider**: `/docs/templates/tech-rider.md`
- **📋 Band Info**: `/wiki/bands/nears-2-far.md` & `/wiki/bands/combine-harvester.md`
- **📞 Contacts**: `/wiki/contacts/venues.md`

---

## 📁 Repository Structure

```
manager/
├── .github/
│   └── agents/
│       └── band-manager-agent.md      # Main agent instructions
│
├── config/
│   └── agent-config.json              # Agent configuration
│
├── wiki/                              # Knowledge base
│   ├── bands/                         # Band information
│   │   ├── nears-2-far.md
│   │   └── combine-harvester.md
│   ├── contacts/                      # CRM
│   │   ├── venues.md
│   │   ├── organizers.md
│   │   └── fans.md
│   └── events/                        # Event documentation
│
├── docs/                              # Documentation & output
│   ├── templates/                     # Reusable templates
│   │   ├── venue-email-template.md
│   │   ├── tech-rider.md
│   │   ├── financial-tracking.md
│   │   └── merch-inventory.md
│   ├── output/                        # Generated documents
│   └── workflows/                     # Process documentation
│       └── show-booking-workflow.md
│
├── tasks/                             # Task tracking
│   └── current-tasks.md
│
├── mcps/                              # Model Context Protocols (future)
│
└── README.md                          # You are here
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
- **SQL Database**: Structured data storage for contacts, financials, inventory
- **RAG System**: Queryable unstructured data (documents, notes, emails)
- **Automation**: Scheduled reminders, follow-ups, reports
- **Analytics**: Deep insights into show performance, revenue, growth

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

*Last Updated: 2026-02-18*  
*Version: 1.0.0*  
*Built with ❤️ and 🤘*
