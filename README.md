# PM Co-Pilot

> Your AI-powered companion for product management. Transform raw ideas into structured initiatives, generate specs, stay focused on strategic work.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## What is This?

PM Co-Pilot turns your AI coding assistant (Cursor, Claude Code, etc.) into an intelligent product management partner. It provides:

- 🧠 **Initiative-Based Workflow** → Think before building with structured opportunity assessments
- 📋 **Document Generation** → Specs, briefs, PRDs from natural conversation
- 🎯 **Strategic Prioritization** → Framework-based recommendations aligned with your strategy
- 📊 **Research Synthesis** → Turn interviews and data into actionable insights
- 🎤 **Voice Training** → Make AI write like you, not generic AI
- ⚡ **Workflow Library** → 15 categories of pre-built PM workflows

---

## Quick Start

### Prerequisites

- An AI coding assistant (Cursor, Claude Code, Windsurf, etc.)
- Git for version control (if you plan to push your structure to a remote repo - never use it to store context)
- Optional: Python 3.10+ (only if using MCP servers)

### Setup (10 minutes)

1. **Clone this repo**
   ```bash
   git clone <your-repo-url>
   cd pm-copilot
   ```

2. **Add your context** (see [GETTING-STARTED.md](GETTING-STARTED.md))
   - Company overview → `knowledge/company-context/`
   - Product strategy → `knowledge/product-strategy/`
   - About you → `knowledge/about-me/`

3. **Start using it**
   ```
   "Read @AGENTS.md and help me get organized"
   ```

---

## Core Workflow

```
Raw Idea → BACKLOG.md → Initiative Assessment → Expand & Research → PRD → Build
```

### 1. Brain Dump → BACKLOG.md

Drop ideas into `BACKLOG.md` without structure:

```markdown
## Mobile App Crashes
- Source: 20 support tickets this week
- Context: Android 12 users, affecting conversion
- Why now: Losing customers

## Enterprise SSO Request
- Source: Sales (Acme Corp - $500K deal)
- Context: Need SAML for 500 users
- Why now: Deal blocker
```

See `examples/example_files/backlog-example.md` for more examples and tips.

### 2. Process → Initiatives

Tell AI:
```
process my backlog
```
or
```
/backlog
```

AI creates structured **opportunity assessments** in `initiatives/`:
- Objective
- Target customer
- Success metrics
- What we know
- What we should research
- Solution ideas
- Risks
- Questions to validate

### 3. Expand Before Building

```
/expand-initiative mobile-crashes
```

AI adds:
- Detailed research plan
- Multiple solution options evaluated
- Risk analysis
- Validation approach

### 4. Generate Execution Docs

```
/prd mobile-crashes
/stories mobile-crashes
/launch-plan mobile-crashes
```

AI creates full PRD, user stories, launch plan from your initiative.

---

## Directory Structure

```
pm-copilot/
├── BACKLOG.md                    # Your inbox for raw ideas
├── AGENTS.md                     # AI agent instructions
├── README.md                     # This file
├── GETTING-STARTED.md            # Setup guide
├── CONTRIBUTING.md               # How to contribute
│
├── initiatives/                  # Opportunity assessments (gitignored content)
│   └── README.md
│
├── knowledge/                    # Your context (gitignored content)
│   ├── about-me/                # Personal PM context, preferences
│   ├── briefs-and-specs/        # Product specs, briefs, technical docs
│   ├── company-context/         # Company vision, values, org
│   ├── frameworks/              # Your PM frameworks (RICE, OKRs, etc.)
│   ├── processes/               # How your team works
│   ├── product-analytics/       # Metrics, KPIs, performance data
│   ├── product-strategy/        # Product vision, roadmap, pillars
│   ├── proposals/               # Decision docs, RFCs
│   ├── references/              # Links, articles, competitive analysis
│   ├── transcripts/             # User interviews, meetings, research
│   └── voice-samples/           # Your writing samples for AI
│
├── examples/                     # Learning & reference
│   ├── workflows/               # 15 PM workflow files + comprehensive README
│   ├── tutorials/               # 4 step-by-step guides (90 min total)
│   ├── example_files/           # Sample documents  
│   └── voice-samples/           # Example writing samples
│
├── templates/                    # 7 reusable document templates
├── mcp/                         # MCP server/client configs (optional)
├── archive/                     # Completed work (gitignored)
└── .env/                        # Environment variables (gitignored)
```

---

## Key Features

### 🎯 Initiative-Based Thinking

Don't jump straight to PRDs. Start with opportunity assessments:
- Why build this?
- Who's it for?
- How do we measure success?
- What do we need to validate?

**Then** generate execution docs when ready.

### 🧠 Context-Aware AI

AI understands YOUR context:
- Your working style (`knowledge/about-me/`)
- Your frameworks (`knowledge/frameworks/`)
- Your strategy (`knowledge/product-strategy/`)
- Your voice (`knowledge/voice-samples/`)

### 📚 Comprehensive Workflows

15 workflow categories covering:
- Backlog processing
- Document generation
- Prioritization & planning
- Research & analysis
- Stakeholder communication
- Decision making
- Technical collaboration
- Bug management
- Process improvement
- And more...

### 🎓 Learning System

- **4 tutorials** (90 min total) from beginner to advanced
- **Example files** showing real outputs
- **Voice samples** demonstrating format
- **Structured prompts** for complex workflows

---

## Common Workflows

### Monday Morning Planning

```
/plan
"What should I work on this week based on my priorities?"
```

### Feature Kick-off

```
1. Add idea to BACKLOG.md
2. /backlog → Creates initiative
3. /expand-initiative [name] → Add research
4. /prd [name] → Generate PRD
5. /stories [name] → Create user stories
```

### Weekly Update

```
/exec-update
"Draft update including metrics from @knowledge/product-analytics/"
```

### Research Synthesis

```
/synthesize
"Synthesize interviews in @knowledge/transcripts/"
```

---

## Slash Commands

Use workflows as shortcuts in Cursor or Claude Code:

**Daily**:
- `/plan` - Daily planning
- `/backlog` - Process ideas

**Initiatives**:
- `/expand-initiative [name]` - Add research before building
- `/create-initiative [topic]` - New opportunity assessment

**Documents**:
- `/spec [initiative]` - Generate spec
- `/prd [initiative]` - Generate PRD
- `/brief [project]` - Create brief
- `/stories [initiative]` - User stories

**Communication**:
- `/exec-update` - Executive update
- `/team-update` - Team update
- `/faq [topic]` - Generate FAQ

**More**: See `examples/workflows/README.md` for a complete list and how to set up in Claude Code or cursor.

---

## Learning Path

### Beginner (Week 1)
1. [Tutorial 1: Getting Started](examples/tutorials/01-getting-started.md) - 15 min
2. [Tutorial 2: Working with Initiatives](examples/tutorials/02-working-with-initiatives.md) - 20 min

### Advanced (Week 2+)
3. [Tutorial 3: Memory & Context](examples/tutorials/03-memory-and-context.md) - 25 min
4. [Tutorial 4: Voice Training](examples/tutorials/04-voice-training.md) - 30 min

**See**: `examples/tutorials/README.md` for complete learning path

---

## What Gets Committed vs. Gitignored

### ✅ Committed (shared structure)
- Directory structure (via `.gitkeep`)
- All documentation (README, AGENTS, guides)
- Templates
- Example files
- Tutorials
- Workflow definitions
- MCP configurations (without secrets)

### ❌ Gitignored (personal data)
- Everything in `knowledge/` (except READMEs)
- Everything in `initiatives/` (except README)
- Everything in `archive/`
- Everything in `.env/`
- Content of `BACKLOG.md` (optional - you decide)

---

## Best Practices

### 📝 Documentation
- Keep `knowledge/` updated with the latest strategy
- Process BACKLOG.md weekly
- Archive completed initiatives monthly
- Update voice samples quarterly

### 🎯 Initiatives
- Start with opportunity assessment
- Expand with research before committing
- Generate PRDs only when validated
- Archive when complete

### 🔄 Daily Routine
- **Morning**: `/plan` - "What should I work on?"
- **Throughout day**: Brain dump to BACKLOG.md
- **End of day**: Update initiative status
- **Weekly**: `/backlog` + archive completed work

---

## Acknowledgements

Inspired by the excellent work of:
- **[Aman Khan](https://github.com/amanaiproduct/personal-os)** - personal-os: Task management and goal-driven prioritization patterns
- **[Tal Raviv](https://github.com/talsraviv/from-thinking-to-coding)** - from-thinking-to-coding: Structured workflow prompts and spec generation approach

Built for product managers who want to spend more time on strategic thinking and less time on repetitive documentation.

---

## Documentation

### Getting Started
- **[GETTING-STARTED.md](GETTING-STARTED.md)** - Complete setup guide
- **[examples/tutorials/](examples/tutorials/)** - Step-by-step learning path

### Reference
- **[AGENTS.md](AGENTS.md)** - How the AI agent works (includes style guidance)
- **[examples/workflows/README.md](examples/workflows/README.md)** - Complete workflow library
- **[templates/](templates/)** - 7 document templates

### Advanced
- **[mcp/README.md](mcp/README.md)** - MCP server integration
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute

---

## Troubleshooting

**Q: AI doesn't understand my context**
- Add context to `knowledge/about-me/`, `knowledge/product-strategy/`
- Use @ mentions: `@knowledge/product-strategy/2024-roadmap.md`
- Check that files exist and have content

**Q: Outputs are too generic**
- Add more detail to `knowledge/` folders
- Include examples in your context docs
- Train AI on your voice (Tutorial 4)

**Q: BACKLOG.md is overwhelming**
- Process weekly: `/backlog`
- Archive old ideas: Move to `archive/`
- Use P3 liberally for low-priority items

**Q: How do I use slash commands?**
- Just type them in your AI assistant (e.g., `/plan`)
- Or use natural language: "Help me plan my day"
- See `examples/workflows/README.md` for all commands

---

## Contributing

Have templates, workflows, or improvements to share?
- Read [CONTRIBUTING.md](CONTRIBUTING.md)
- Submit a pull request

---

## License

MIT License - feel free to use and adapt for your needs.

---

## Support

**Quick help**:
- Start with [GETTING-STARTED.md](GETTING-STARTED.md)
- Browse [examples/tutorials/](examples/tutorials/)
- Check [examples/workflows/README.md](examples/workflows/README.md)

**Questions**:
- Open an issue
- Check existing documentation
- See [CONTRIBUTING.md](CONTRIBUTING.md)

---

**Ready to start?**

1. Read [GETTING-STARTED.md](GETTING-STARTED.md) (10 min)
2. Add context to `knowledge/` (20 min)
3. Brain dump to `BACKLOG.md` (5 min)
4. Run `/backlog` to create initiatives
5. Watch the magic happen ✨

Happy product managing! 🚀
