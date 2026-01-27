# PM Co-Pilot

> Turn your AI assistant into a product management partner. Process ideas, generate specs, prioritize strategically.

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-orange.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Star this repo](https://img.shields.io/github/stars/skawsarani/pm-copilot?style=social)](https://github.com/skawsarani/pm-copilot)


---

## What is This?

PM Co-Pilot is a simple system that turns AI assistants (Cursor, Claude Code) into PM tools:

- **Priority-Focused Workflow** - Max 3 P0 tasks keeps you focused
- **Backlog Processing** - Brain dump → Organized tasks/initiatives
- **Document Generation** - Specs, briefs, PRDs from conversation
- **Research Synthesis** - Transform interviews into insights
- **Voice Training** - Match your writing style

---

## Quick Start

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd pm-copilot
./setup.sh
cursor .    # Or your AI assistant
```

Tell your AI:
```
Read @AGENTS.md to understand how to help me as a PM Co-Pilot.
```

### 2. Add Your Context

Fill in these essential files created by setup:

- `knowledge/product-strategy/current-strategy.md` - Vision, priorities, metrics
- `knowledge/company-context/company-overview.md` - Mission, products, team
- `knowledge/about-me/about-me.md` - Background, working style, preferences

See `templates/` for examples.

### 3. Start Using It

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
- **Initiatives** → `knowledge/initiatives/` (strategic ideas to explore)
- **References** → `knowledge/references/` (useful context)

**Generate docs when ready:**
```
/write-prd mobile-performance
/write-spec mobile-performance
/write-user-stories mobile-performance
```

---

## Directory Structure

```
pm-copilot/
├── BACKLOG.md              # Daily inbox (gitignored)
├── AGENTS.md               # AI instructions
├── VOICE-GUIDE.md          # Your writing style (optional, gitignored)
├── config.yaml             # Priority caps, categories (customizable)
├── setup.sh                # Setup script
│
├── evals/                  # Automated AI tests
├── mcp/                    # MCP servers
│   └── task-manager/       # Task management MCP server
│       ├── server.py       # MCP server
│       └── README.md       # MCP tool documentation
│
├── tasks/                  # Your tasks (gitignored)
├── knowledge/              # Your context (gitignored)
│   ├── about-me/
│   ├── product-strategy/
│   ├── company-context/
│   ├── frameworks/
│   ├── initiatives/
│   ├── briefs-and-specs/
│   ├── transcripts/
│   ├── voice-samples/
│   ├── references/
│   └── notes/             # Archived backlog snapshots
│
├── skills/                 # AI capabilities and specialized workflows
├── workflows/              # Slash command workflows
├── templates/              # Document templates
├── integrations/           # Read-only API clients for external services
└── prototypes/             # Code prototypes (gitignored)
```

---

## What Gets Committed vs. Gitignored

**Committed (shared structure):**
- Directory structure
- Documentation, templates, workflows
- `config.yaml` (priority caps, categories)
- `evals/` folder (automated tests)
- `skills/` folder (AI capabilities)
- `AGENTS.md`

**Gitignored (your data):**
- `BACKLOG.md`
- `GOALS.md`
- `VOICE-GUIDE.md`
- Content in `knowledge/`, `tasks/`, `prototypes/`

---

## Core Workflow

```
BACKLOG.md → /process-backlog → Tasks (P0≤3) / Initiatives / References
```

1. **Brain dump** to `BACKLOG.md` throughout the day
2. **Process** with `/process-backlog` - AI categorizes and enforces priority caps
3. **Work** - Focus on your 3 P0 tasks, explore initiatives, generate docs

---

## Priority System

Tasks use P0-P3 with strict caps to prevent overwhelm:

- **P0** (Critical): Max 3 tasks - Today's focus
- **P1** (High): Max 7 tasks - This week
- **P2** (Medium): Max 15 tasks - This month
- **P3** (Low): Unlimited - Backlog

When `/process-backlog` would exceed caps, AI asks you to deprioritize.

---

## Skills (Auto-Invoked)

Skills are specialized tools AI uses automatically:

**Product Docs (`product-docs` skill):**
- `/write-prd [name]`, `/write-spec [name]`, `/write-brief [name]`
- `/write-user-stories [name]`, `/write-decision [topic]`
- Auto-pulls context from knowledge base

**Doc Co-Authoring (`doc-coauthoring` skill):**
- Guided workflow for collaborative documentation
- Proposals, technical specs, decision docs

**Product Metrics Analysis (`product-metrics-analysis` skill):**
- Analyze product metrics (usage, retention, conversion, funnels)
- Apply PM frameworks (AARRR, cohort analysis, PMF, North Star)
- Calculate metrics, identify patterns, and provide actionable recommendations
- Works with CSV, JSON, SQL results, or dashboard descriptions

**UX Copy (`ux-copy` skill):**
- Create UI copy, error messages, microcopy, notifications
- English interface text and UX writing

**i18n Translator (`i18n-translator` skill):**
- French translation (Canadian/European)
- UI localization and cultural adaptation

**User Research (`user-research-analysis` skill):**
- Analyze interviews and transcripts
- Synthesize research, create personas

**Competitor Analysis (`competitor-analysis` skill):**
- Analyze single competitor comprehensively
- Features, pricing, strengths, gaps, testimonials

**Prototyping (`prototype-builder` skill):**
- Build working prototypes from specs
- React, TypeScript, Shadcn/ui

**Internal Comms (`internal-comms` skill):**
- Status reports, updates, FAQs

**MCP Builder (`mcp-builder` skill):**
- Create MCP servers for external integrations
- Python (FastMCP) or Node/TypeScript

**Skill Creator (`skill-creator` skill):**
- Create new skills to extend AI capabilities

**Slash Command Builder (`slash-command-builder` skill):**
- Build custom slash command workflows

---

## Task Management MCP (Optional)

For faster task operations, install the task management MCP server:

```bash
uv sync
```

Then configure your AI assistant to use `mcp/task-manager/server.py` (see `mcp/task-manager/README.md` for setup).

**Benefits:**
- 10x faster task operations (CRUD, deduplication, statistics)
- Programmatic access to tasks
- Auto-categorization and priority enforcement
- Find stale/overdue tasks, prune completed ones

---

## Integrations (Optional)

Read-only API clients for pulling context from external services:

| Service | Capabilities |
|---------|--------------|
| **Slack** | Messages, channels, threads, users, search, channel summaries |
| **Notion** | Pages, databases, blocks, search |
| **Linear** | Issues, projects, initiatives, cycles, labels, customers |
| **Google Calendar** | Events, calendars |
| **Google Drive** | Files, folders, permissions, search |
| **Avoma** | Meetings, notes, transcripts |

See `integrations/README.md` for full API reference.

---

## Common Commands

**Daily:**
- "What should I work on today?" - Review P0/P1 tasks
- `/process-backlog` - Process ideas into tasks/initiatives
- `/today` - Quick view of due/overdue tasks
- `/daily-planning` - Plan your day with priorities

**Weekly:**
- `/upcoming` - Tasks due in next 7 days
- `/weekly-review` - Review the week, plan next week

**Tasks:**
- `/tasks` - View all tasks with filters
- "Mark task [name] as complete"
- "Find stale tasks"
- "Prune completed tasks" - Delete tasks older than 90 days

**Documents:**
- `/write-prd [name]` - Generate PRD
- `/write-spec [name]` - Generate spec
- `/write-brief [name]` - Generate brief

**Research:**
- `/competitor-research [names]` - Research multiple competitors, generate matrix

**Git:**
- `/commit` - Commit with conventional format and emoji
- `/pr` - Create pull request
- `/push` - Push to remote

**Natural language works too:**
- "Create a spec for the mobile performance initiative"
- "Analyze the user interviews in knowledge/transcripts/"
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
- Morning: "What should I work on today?"
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

---

## License
This work is licensed under CC BY-NC-SA 4.0.

Copyright © 2026 Sam Kawsarani. You may view, use, modify, and share this repo with attribution for non-commercial purposes. Commercial sale is not permitted, but you may use it internally for work and business.

Full license: [https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)
