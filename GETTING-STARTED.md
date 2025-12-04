# Getting Started with PM Co-Pilot

Complete setup guide to transform your AI assistant into your product management partner.

**Time**: 30 minutes
**Goal**: Working PM Co-Pilot with your context

---

## Prerequisites

Before you begin:
- [ ] AI coding assistant installed (Cursor, Claude Code, etc.)
- [ ] Git installed (only if you plan to push to remote)
- [ ] Basic familiarity with Markdown
- [ ] Optional: Python 3.10+ (only for MCP servers)
- [ ] Tip: Use Obsidian along Cursor or Claude code for better markdown support

---

## Step 1: Clone and Setup (5 minutes)

### Clone the Repository

```bash
# Clone the repo
git clone <your-repo-url>
cd pm-copilot

# Open in your AI assistant
cursor .  # or open with your AI assistant
```

### First Conversation with AI

Tell your AI assistant:

```
Read @AGENTS.md to understand how to help me as a PM Co-Pilot.

Then let's set up my workspace with essential context.
```

The AI will guide you through setup using the instructions in AGENTS.md.

---

## Step 2: Add Company Context (10 minutes)

Create essential context files so AI understands your work environment.

### Company Context

Create `knowledge/company-context/overview.md`:

```markdown
# Company Overview

## Mission
[Your company mission]

## Product(s)
[What you build, who it's for]

## Team Structure
- Product: [team size, structure]
- Engineering: [team size, structure]
- Design: [team size, structure]

## Current Stage
[Startup, growth, enterprise]

## Key Stakeholders
- [Name, role, what they care about]
```

### Product Strategy

Create `knowledge/product-strategy/2024-strategy.md`:

```markdown
# 2024 Product Strategy

## Vision
[Where are we going?]

## Strategic Pillars
1. **[Pillar 1]**: [Description]
2. **[Pillar 2]**: [Description]
3. **[Pillar 3]**: [Description]

## Current Priorities (Q4 2024)
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

## Success Metrics
- [Metric 1]: Current X, Target Y
- [Metric 2]: Current X, Target Y
```

### About You

Create `knowledge/about-me/about-me.md`:

```markdown
# About Me

## Background
[Your PM experience, domain expertise]

## Working Style
- Prefer: [Bullets, concise communication, data-driven]
- Avoid: [Verbose docs, premature optimization]
- Decision-making: [How you make decisions]

## Current Focus
[What you're working on now]

## Frameworks I Use
- Prioritization: [RICE, Value vs Effort]
- Goal-setting: [OKRs, Milestones]
- Research: [Jobs-to-be-Done, Customer interviews]

## Communication Preferences
- Execs: [Style]
- Team: [Style]
- Stakeholders: [Style]
```

**Pro Tip**: Be specific! "I prefer 3-5 bullet summaries before detailed sections" is better than "I like concise communication."

---

## Step 3: Set Up First Backlog (5 minutes)

### Add Ideas to BACKLOG.md

Open `BACKLOG.md` and brain dump ideas:

```markdown
# Backlog

Drop raw notes or todos here. Say `process my backlog` when you're ready for triage.

## Mobile Performance Issues
- Source: Support tickets (15 this week)
- Context: Android app slow on startup
- Impact: 4.2⭐ rating, users complaining

## Enterprise SSO Request
- Source: Sales (Acme Corp deal)
- Context: Need SAML for security compliance
- Impact: $500K deal blocker

## User Onboarding Improvements
- Source: Analytics (60% drop-off after signup)
- Context: Too many steps, confusing flow
- Impact: Losing potential customers
```

Don't worry about format - just capture ideas with enough context.

See `examples/example_files/backlog-example.md` for more examples.

---

## Step 4: Process Your First Initiative (5 minutes)

### Process the Backlog

Tell your AI:

```
process my backlog
```

Or simply:

```
/backlog
```

**What happens**:
1. AI reads `BACKLOG.md`
2. Creates structured initiative files in `initiatives/`
3. Suggests priorities (P0-P3)
4. Flags duplicates
5. Clears processed items from backlog

### Review Output

Check `initiatives/` folder for new files like:

```
initiatives/
├── mobile-performance.md      # Full opportunity assessment
├── enterprise-sso.md
├── user-onboarding.md
└── dark-mode.md
```

Each contains:
- Objective
- Target customer
- Success metrics
- What we know
- What to research
- Solution ideas
- Risks
- Questions to validate
- Priority

---

## Step 5: Test Key Workflows (5 minutes)

### Planning Workflow

```
/plan
"What should I prioritize this week?"
```

AI will:
- Read your initiatives
- Check your strategy
- Recommend priorities
- Suggest next actions

### Expand an Initiative

```
/expand-initiative mobile-performance
```

AI adds:
- Detailed research questions
- Solution options evaluated
- Risk assessment
- Validation approach

### Generate a Document

```
/spec mobile-performance
```

Or:

```
/prd mobile-performance
```

AI creates comprehensive spec or PRD from your initiative.

---

## Next Steps

### Daily Use

**Morning**:
```
/plan
"What should I work on today?"
```

**Throughout day**:
- Brain dump ideas to `BACKLOG.md`
- Chat with AI about decisions
- Generate docs as needed

**End of day**:
- Update initiative status
- Document decisions

**Weekly**:
```
/backlog
"Process new backlog items"
```

### Learn More

**Beginner** (complete next):
1. [Tutorial 1: Getting Started](examples/tutorials/01-getting-started.md) - Deeper dive on basics
2. [Tutorial 2: Working with Initiatives](examples/tutorials/02-working-with-initiatives.md) - Initiative lifecycle

**Advanced** (week 2+):
3. [Tutorial 3: Memory & Context](examples/tutorials/03-memory-and-context.md) - Optimize AI context
4. [Tutorial 4: Voice Training](examples/tutorials/04-voice-training.md) - Make AI write like you

### Explore Workflows

See `examples/workflows/README.md` for the complete library:
- Backlog processing
- Initiative management
- Document generation
- Research synthesis
- Stakeholder communication
- Technical collaboration
- And more...

---

## Common Issues

### "AI doesn't understand my context"

**Problem**: AI gives generic responses

**Solutions**:
1. Add more detail to `knowledge/` files
   - Be specific about your domain
   - Include examples
   - Add current metrics
2. Use @ mentions to reference files
   ```
   "Use my product strategy from @knowledge/product-strategy/"
   ```
3. Create `knowledge/frameworks/` docs for your methods

### "BACKLOG.md is getting messy"

**Problem**: Too many unprocessed ideas

**Solutions**:
1. Process weekly: `/backlog`
2. Archive old ideas: Move to `archive/old-backlog-2024-12.md`
3. Be ruthless: Not every idea becomes an initiative
4. Use P3 for "someday/maybe"

### "Initiatives feel incomplete"

**Problem**: Not enough detail to act on

**Solutions**:
1. Run `/expand-initiative [name]` before building
2. Add research to `knowledge/transcripts/`
3. Update initiative as you learn
4. It's OK to iterate - documents are living

### "AI outputs don't sound like me"

**Problem**: Generic corporate language

**Solutions**:
1. Add voice samples: `knowledge/voice-samples/`
2. Complete Tutorial 4: Voice Training
3. Give feedback: "Make this more direct"
4. Update `knowledge/about-me/` with style preferences

### "Can't find workflow I need"

**Problem**: Don't know what's available

**Solutions**:
1. Browse `examples/workflows/README.md`
2. Search workflow files for keywords
3. Ask AI: "What workflows do you have for [task]?"
4. Create your own (see CONTRIBUTING.md)

---

## Verification Checklist

After setup, you should have:

**Context Files**:
- [ ] `knowledge/company-context/overview.md`
- [ ] `knowledge/product-strategy/2024-strategy.md`
- [ ] `knowledge/about-me/about-me.md`

**Backlog & Initiatives**:
- [ ] `BACKLOG.md` processed (or ready to process)
- [ ] At least 1 initiative in `initiatives/`
- [ ] Initiatives have priorities (P0-P3)

**Tested Workflows**:
- [ ] `/backlog` creates initiatives from backlog
- [ ] `/plan` gives personalized recommendations
- [ ] `/expand-initiative [name]` adds detail
- [ ] `/spec [name]` or `/prd [name]` generates docs

**AI Understanding**:
- [ ] AI references your strategy in responses
- [ ] AI suggests priorities based on your context
- [ ] AI uses your frameworks (if added)

---

## Tips for Success

### 🎯 Start Small
- Add minimum context to get started
- Process 3-5 backlog items, not 50
- Generate 1 spec before batch creating docs
- Learn one workflow category at a time

### 📝 Document as You Go
- Update strategy when it changes
- Add learnings to initiative files
- Capture frameworks you actually use
- Archive completed work regularly

### 🔄 Iterate on Context
- Your first context files will be rough - that's OK
- Refine as you use the system
- Add examples of good outputs
- Update preferences as you learn what works

### 🎤 Invest in Voice Training (Week 2)
- Biggest impact on output quality
- Tutorial 4 walks you through it
- Takes 30 minutes, saves hours later
- Makes AI drafts feel like your drafts

### 🤝 Customize for Your Team
- Add team-specific frameworks
- Create custom templates
- Document your unique processes
- Share what works

---

## What's Next?

### Immediate (Today)
1. ✅ Complete this setup (30 min)
2. Process real backlog
3. Generate one real document
4. See what works for you

### This Week
- Complete Tutorial 1 & 2 (35 min)
- Use daily workflows (`/plan`, `/backlog`)
- Build habit of brain dumping to BACKLOG.md
- Refine your context files

### Next Week
- Complete Tutorial 3 & 4 (55 min)
- Add frameworks to `knowledge/frameworks/`
- Train AI on your voice
- Explore advanced workflows

### Month 2+
- Create custom workflows
- Add MCP integrations (optional)
- Share learnings (CONTRIBUTING.md)
- Help others get started

---

## Getting Help

### Resources
- **[README.md](README.md)** - Overview and features
- **[examples/tutorials/](examples/tutorials/)** - 4 learning tutorials
- **[examples/workflows/README.md](examples/workflows/README.md)** - Complete workflow library
- **[AGENTS.md](AGENTS.md)** - How AI understands this system (includes style guidance)

### Stuck?
1. Check tutorials for your topic
2. Browse workflow library
3. Ask AI: "How do I [task] in PM Co-Pilot?"
4. Open an issue in the repo

---

## Success Stories (Add Yours!)

_This section will grow with user examples. Share what works for you!_

**Example use case**:
```
Morning routine: `/plan` shows P0 mobile bug and P1 enterprise feature.
Added research notes to both initiatives.
Generated PRD for enterprise feature.
Shared with eng lead - saved 2 hours of back-and-forth.
```

---

**You're ready! Start with `/plan` and let the AI guide you.** 🚀

**Next**: [Tutorial 1: Getting Started](examples/tutorials/01-getting-started.md) for a deeper dive.
