# SAMS PRODUCT OS

> Turn your AI assistant into a product management partner. Process ideas, generate specs, prioritize strategically.

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-orange.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Star this repo](https://img.shields.io/github/stars/skawsarani/sams-product-os?style=social)](https://github.com/skawsarani/sams-product-os)


*Quick links:* [Quick Start](#quick-start) · [Directory Structure](#directory-structure) · [Core Workflow](#core-workflow) · [Common Commands](#common-commands) · [Best Practices](#best-practices)

---

## What is This?

Sams Product OS is a simple system that turns AI assistants (Cursor, Claude Code) into PM tools:

- **Priority-Focused Workflow** - Max 3 P0 tasks keeps you focused
- **Backlog Processing** - Brain dump → Organized tasks/initiatives
- **Document Generation** - Specs, briefs, PRDs from conversation
- **Research Synthesis** - Transform interviews into insights
- **Voice Training** - Match your writing style

---

## Quick Start

### 1. Clone the Repo

```bash
git clone <your-repo-url>
cd sams-product-os
```

### 2. Prerequisites

- **macOS**: Install [Homebrew](https://brew.sh) — the setup skill handles the rest
- **Other platforms**: Install [uv](https://docs.astral.sh/uv/), [bun](https://bun.sh), and [qmd](https://github.com/tobi/qmd) manually

### 3. Run Setup

Open in your AI assistant and say:

```
Set up my product OS
```

The AI will install dependencies, create your workspace, configure MCP, and verify everything works.

> Setup configures for Claude Code by default. Say "set up for Cursor too" if you use Cursor.

### 4. Start Using It

**Brain dump to BACKLOG.md:**
```markdown
## Mobile Performance Issues
- Source: Support tickets (15 this week)
- Context: Android app slow on startup
- Impact: 4.2⭐ rating drop

## Follow up with Sarah about Q4 goals
- Need to align on OKRs by end of week
```

**Process your backlog:**
```
/process-backlog
```

AI categorizes into:
- **Tasks** → `tasks/` (P0-P3 priority, max 3 P0 tasks)
- **Initiatives** → `initiatives/` (strategic ideas to explore)
- **References** → `knowledge/references/` (useful context)

**Generate docs when ready:**
```
/write-doc prd mobile-performance
/write-doc spec mobile-performance
/write-doc user-stories mobile-performance
```

---

## Directory Structure

```
sams-product-os/
├── .claude/skills/         # AI agent skills & slash commands. Trigger via `/skillname`
├── tools/                  # Tools to extend AI agent capabilities
│   ├── integrations/       # Read-only API clients for external services
│   └── mcp-servers/        # Custom MCP servers
│       └── task-manager/   # Task management MCP server
│           ├── server.py   # MCP server
│           └── README.md   # MCP tool documentation
│
├── evals/                  # AI agent tests & evaluation
├── tasks/                  # Your personal tasks with archived backlog
├── knowledge/              # Persistent context & references for your AI agent
├── meetings/               # Meeting notes & transcripts
├── initiatives/            # Strategic initiatives & groomed requests
├── prototypes/             # Your vibe coded apps & prototypes
├── _temp/                  # Drop zone for files in transit or scratch work
├── templates/              # Document templates
├── BACKLOG.md              # Daily brain dump inbox of future work
├── GOALS.md                # Ownership areas & quarterly goals
├── AGENTS.md               # Your AI agent instructions
├── CLAUDE.md               # Points to AGENTS.md (agent instructions for Claude Code)
├── TOOLS.md                # MCP tool & CLI integration reference for AI agent
├── VOICE-GUIDE.md          # Your writing style (optional)
└── config.yaml             # Customizable configuration for your AI agent

```

---

## What Gets Committed vs. Gitignored

**Committed (shared structure):**
- Directory structure
- Documentation, templates, `.claude/skills/`
- `config.yaml` (priority caps, categories)
- `evals/` folder (automated tests)
- `.claude/skills/` folder (AI agent capabilities)
- `AGENTS.md`
- `TOOLS.md`

**Gitignored (your data):**
- `BACKLOG.md`
- `GOALS.md`
- `VOICE-GUIDE.md`
- Content in `knowledge/`, `tasks/`, `meetings/`, `initiatives/`, `prototypes/`, `_temp/`

---

## Core Workflow

```
BACKLOG.md → /process-backlog → Tasks (P0≤3) / Initiatives / References
```

1. **Brain dump** to `BACKLOG.md` throughout the day
2. **Process** with `/process-backlog` - AI categorizes and enforces priority caps
3. **Work** - Focus on your 3 P0 tasks, explore initiatives, generate docs

---

## Tasks

### Task File Structure

Each task is a markdown file in `tasks/` with YAML frontmatter:

- **title** - Task name
- **category** - technical, outreach, research, writing, admin, other
- **priority** - P0 (Critical), P1 (High), P2 (Normal), P3 (Low)
- **status** - n (not_started), s (started), b (blocked), d (done)
- **created_date** - YYYY-MM-DD
- **due_date** - YYYY-MM-DD (optional)
- **resource_refs** - Links to related files

Content sections:
- **Context** - Goals and references
- **Next Actions** - Steps to complete
- **Progress Log** - Notes, blockers, decisions

### Managing Tasks

**Update:**
- "Mark task [name] as complete"
- "Change task [name] status/priority/category"

**Find:**
- "Find tasks older than [N] days"
- "Find stale tasks"

**Prune:**
- "Prune completed tasks older than [N] days"

Tasks are marked complete with `status: d`. No file movement needed.

### Priority System

Tasks use P0-P3 with strict caps to prevent overwhelm:

- **P0** (Critical): Max 3 tasks - Today's focus
- **P1** (High): Max 7 tasks - This week
- **P2** (Medium): Max 15 tasks - This month
- **P3** (Low): Unlimited - Backlog

When `/process-backlog` would exceed caps, AI asks you to deprioritize.

---

## Skills

Skills are specialized tools AI agents uses automatically:

**Write Doc (`write-doc` skill):**
- `/write-doc prd [name]`, `/write-doc spec [name]`, `/write-doc brief [name]`
- `/write-doc user-stories [name]`, `/write-doc decision [topic]`
- Auto-generate mode for immediate drafts, co-authoring mode for iterative writing

**Analyze Metrics (`analyze-metrics` skill):**
- Analyze product metrics (usage, retention, conversion, funnels)
- Apply PM frameworks (AARRR, cohort analysis, PMF, North Star)
- Calculate metrics, identify patterns, and provide actionable recommendations
- Works with CSV, JSON, SQL results, or dashboard descriptions

**Write UX Copy (`write-ux-copy` skill):**
- Create UI copy, error messages, microcopy, notifications
- English interface text and UX writing

**Translate i18n (`translate-i18n` skill):**
- French translation (Canadian/European)
- UI localization and cultural adaptation

**Analyze Research (`analyze-research` skill):**
- Analyze interviews and transcripts
- Synthesize research, create personas

**Analyze Competitor (`analyze-competitor` skill):**
- Analyze single competitor or multiple competitors in parallel
- Features, pricing, strengths, gaps, comparison matrix

**Analyze Calendar (`analyze-calendar` skill):**
- Analyze Google Calendar events, identify focus blocks, meeting prep
- Meeting classification, schedule intelligence, back-to-back warnings
- Task-to-time-block alignment with PM task system

**Build Prototype (`build-prototype` skill):**
- Build working prototypes from specs
- React, TypeScript, Shadcn/ui

**Write Dev Docs (`write-dev-docs` skill):**
- `/write-dev-docs api-reference [resource]`, `/write-dev-docs guide [name]`
- `/write-dev-docs recipe [use-case]`, `/write-dev-docs postman [api-name]`
- Stripe-quality API references, integration guides, code recipes, Postman collections
- Supports OpenAPI specs, code, natural language, and PRD inputs

**Write Comms (`write-comms` skill):**
- 3P updates, stakeholder reports, newsletters, FAQs, incident reports
- Structured workflows with voice guide integration and quality checks

**Build MCP (`build-mcp` skill):**
- Create MCP servers for external integrations
- Python (FastMCP) or Node/TypeScript

**Create Skill (`create-skill` skill):**
- Create new skills to extend AI capabilities

**Setup Product OS (`setup-product-os` skill):**
- Guided workspace setup: prerequisites, directories, templates, MCP, search
- Platform-aware (automated on macOS, manual guide on other platforms)

**Daily Pulse (`daily-pulse` skill):**
- Morning briefing with calendar intelligence, tasks, and goal alignment
- Variations: tomorrow, week, time-constrained, focus mode, context recovery

**Weekly Review (`weekly-review` skill):**
- Reflect on the week, check goal progress, plan next week
- Quick mode for condensed output

**Weekly Recap (`weekly-recap` skill):**
- Exec-ready weekly update structured around initiatives
- Quick and Slack formatting modes

**View Tasks (`view-tasks` skill):**
- `/view-tasks today`: due today and overdue tasks
- `/view-tasks upcoming`: tasks due in next 7 days
- `/view-tasks all`: all tasks with optional filters

**Process Backlog (`process-backlog` skill):**
- Process BACKLOG.md into tasks, initiatives, references
- Deduplication and priority cap enforcement

**Process Meetings (`process-meetings` skill):**
- Extract action items from meeting transcripts
- Parallel processing for 3+ transcripts

**Commit (`commit` skill):**
- Conventional commits with emoji prefixes and smart splitting

**Push (`push` skill):**
- Push to remote with upstream tracking and force-push safety

**Create PR (`create-pr` skill):**
- Create pull requests with comprehensive summary and test plan

---

## MCP Servers (Optional)

MCP (Model Context Protocol) provides direct tool access for faster operations.

### Task Manager MCP

For faster task operations:

```bash
uv sync
```

Configure your AI assistant to use `tools/mcp-servers/task-manager/server.py` (see `tools/mcp-servers/task-manager/README.md`).

**Benefits:**
- 10x faster task operations (CRUD, deduplication, statistics)
- Auto-categorization and priority enforcement
- Find stale/overdue tasks, prune completed ones

See TOOLS.md for full MCP tool reference.

---

## Integrations (Optional)

Read-only API clients for pulling context from external services:

| Service | Capabilities |
|---------|--------------|
| **Slack** | Messages, channels, threads, users, search, channel summaries, find unanswered |
| **Notion** | Pages, databases, blocks, search |
| **Linear** | Issues, projects, initiatives, cycles, labels, customers, customer needs |
| **Google Calendar** | Events, calendars |
| **Google Drive** | Files, folders, permissions, search |
| **HubSpot** | Contacts, companies, deals, tickets, products, orders, invoices |
| **Common** | URL parser for Slack, Linear, Google, Notion URLs |

See `tools/integrations/README.md` for full API reference.

---

## Common Commands

**Daily:**
- "What should I work on today?" - Review P0/P1 tasks
- `/process-backlog` - Process ideas into tasks/initiatives
- `/view-tasks today` - Quick view of due/overdue tasks
- `/daily-pulse` - Morning briefing with calendar intelligence, tasks, and goals

**Weekly:**
- `/view-tasks upcoming` - Tasks due in next 7 days
- `/weekly-review` - Review the week, plan next week
- `/weekly-recap` - Generate exec-ready initiative recap for manager/execs
- `/process-meetings` - Extract action items from recent meeting transcripts

**Tasks:**
- `/view-tasks all` - View all tasks with filters
- "Mark task [name] as complete"
- "Find stale tasks"
- "Prune completed tasks" - Delete tasks older than 90 days

**Documents:**
- `/write-doc prd [name]` - Generate PRD
- `/write-doc spec [name]` - Generate spec
- `/write-doc brief [name]` - Generate brief
- `/write-doc user-stories [name]` - Generate user stories
- `/write-doc decision [topic]` - Generate decision doc

**Developer Docs:**
- `/write-dev-docs api-reference [resource]` - Generate API reference
- `/write-dev-docs guide [name]` - Generate integration guide
- `/write-dev-docs recipe [use-case]` - Generate code recipe
- `/write-dev-docs postman [api-name]` - Generate Postman collection

**Research:**
- `/analyze-competitor [names]` - Research competitors, generate comparison matrix

**Git:**
- `/commit` - Commit with conventional format and emoji
- `/create-pr` - Create pull request
- `/push` - Push to remote

**Building:**
- `/create-skill` - Create a new skill
- `/build-mcp` - Create a new MCP server

**Natural language works too:**
- "Create a spec for the mobile performance initiative"
- "Analyze the user interviews in meetings/"
- "What are my P0 tasks?"

---

## Voice Training

Give AI examples of your actual writing, then have it extract patterns and apply them.
### Step 1: Collect Your Writing Samples

Gather 5-10 examples of your real writing. Mix of formats works best:

```
knowledge/
├── voice-samples/
│   ├── email-to-colleague.md
│   ├── email-to-exec.md
│   ├── slack-messages.md
│   ├── linkedin-post.md
│   ├── blog-post-excerpt.md
│   └── product-spec-intro.md
```

**What makes good samples:**

- Emails you actually sent (not templates)
- Slack messages that got good responses
- Posts that felt authentically "you"
- Writing you're proud of

**What to avoid:**

- Heavily edited/formal documents
- Writing you copied from somewhere
- Samples that don't represent your natural style

### Step 2: Run Voice Analysis

Ask your agent to analyze your samples:

```
Read all files in knowledge/voice-samples/ and analyze my writing style.
Extract specific patterns for:
1. Sentence structure and length
2. How I open and close messages
3. Words/phrases I use often
4. What I never say
5. Tone and formality level
6. How I structure arguments

Create a voice guide.
```

### Step 3: Review the Voice Guide
Your agent will produce something like:

```md
## Your Writing Voice

### Sentence Style
- Short sentences. Punchy. You rarely go over 15 words.
- Questions used to transition: "So what does this mean?"
- Em dashes avoided - you use commas or periods instead

### Openers
- Emails: Jump straight to the point, no "Hope you're well"
- Posts: Lead with a surprising fact or bold claim
- Specs: Start with the user problem, not the solution

### Signature Phrases
- "Here's the thing..."
- "Let's be real"
- "The short version:"
- Ends with clear next step or question

### What You Avoid
- "I hope this email finds you well"
- "Please don't hesitate to reach out"
- Bullet point lists in emails (prefer paragraphs)
- Emojis in professional context
- "Key insights" or "learnings"

### Tone Calibration
- To peers: Casual, direct, occasional humor
- To execs: Concise, data-first, clear ask
- Public posts: Confident but not salesy
```

### Step 4: Save It (Optional)

**Option A: Save to VOICE-GUIDE.md** (faster, more consistent)
```
Save this to VOICE-GUIDE.md in the project root.
```
This file is gitignored. The agent automatically checks for it when drafting content.

**Option B: Skip saving** (simpler, always fresh)
Let the agent read from `knowledge/voice-samples/` each time you ask it to match your voice.

### Step 5: Test and Refine
```
Draft an email to my VP about pushing the launch date back one week.
Match my voice from VOICE-GUIDE.md (or knowledge/voice-samples/).
```

Compare the output to how you'd actually write it. Give feedback:

```
Good start, but I wouldn't say "I wanted to reach out" - I'd just say
"Quick update on launch timing." Also too many bullet points, I usually
write in short paragraphs. Try again.
```

**Maintenance**: Add new samples monthly as your voice evolves.
```
Read my recent writing in [location] and update my voice guide.
What patterns have changed? What's new?
```


---

## Best Practices

**Daily:**
- Morning: `/daily-pulse` for calendar + task briefing
- Throughout day: Brain dump to BACKLOG.md
- Weekly: `/process-backlog` to process

**Context:**
- Start small - add context as you go
- Process backlog weekly, not daily
- Update voice samples quarterly

**Tips:**
- Use @ mentions: `@knowledge/product-strategy/`
- Process 3-5 backlog items at a time, not 50
- Let priority caps guide you - max 3 P0 tasks

**Troubleshooting:**
- Generic responses? Add more to `knowledge/`
- AI not using context? Use @ mentions explicitly
- Too many tasks? Let AI enforce priority caps

---

## Running Evals

Test that your system is working correctly after making changes:

```bash
uv run pytest evals/ -v
```

This validates:
- Task categorization
- Auto-categorization based on config.yaml keywords
- Priority caps enforcement (P0≤3, P1≤7, P2≤15)
- File format and structure

See `evals/README.md` for details.

---

## For Contributors

Contributions should:
- Not include personal information
- Be generic and configurable
- Include documentation
- Follow the existing patterns
- Test with your AI assistant before submitting

---

## Acknowledgements

This project was inspired by the work of several amazing builders in the space. Special thanks to:

- [Aman Khan](<https://github.com/amanaiproduct>) - PersonalOS
- [Tal Raviv](https://www.talraviv.co) - LinkedIn Content + Articles
- [Carl Velloti](https://github.com/carlvellotti/carls-product-os) - carls-product-os, cursor-pm-course, claude-code-everyone-course

---

## License
This work is licensed under CC BY-NC-SA 4.0.

Copyright © 2026 Sam Kawsarani. You may view, use, modify, and share this repo with attribution for non-commercial purposes. Commercial sale is not permitted, but you may use it internally for work and business.

Full license: [https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)
