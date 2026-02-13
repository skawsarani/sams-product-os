---
name: setup-product-os
description: Sets up the Sams Product OS workspace — checks platform (macOS for automated install), installs prerequisites via Homebrew (uv, bun, qmd), creates knowledge base directories, generates template files, configures MCP and search, and runs a verification checklist. Invoked via /setup or when user asks to set up, initialize, or bootstrap the product OS. Defaults to Claude Code; configures Cursor if requested.
---

# Setup Product OS

Guided setup for bootstrapping the Sams Product OS workspace. Checks what's already done, installs what's missing, and verifies everything works.

## Workflow

Execute steps 0-6 in order. Skip what's already done. Report progress after each step.

### Step 0: Platform Check

Run `uname` to detect the OS.

- **macOS (Darwin)**: Proceed with full automated setup (Steps 1-6)
- **Other platforms**: Print manual prerequisites guide with install links, then continue with Steps 3-6 (directory/template/config work is platform-independent):
  - uv: https://docs.astral.sh/uv/
  - bun: https://bun.sh
  - qmd: https://github.com/tobi/qmd

### Step 1: Check & Install Prerequisites (macOS only)

Check each tool and install if missing:

1. `which brew` — if missing, **stop** and instruct user to install from https://brew.sh (do not install Homebrew automatically)
2. `which uv` — if missing, run `brew install uv`
3. `which bun` — if missing, run `brew install oven-sh/bun/bun`
4. `which qmd` — if missing, run `bun install -g github:tobi/qmd`

Report what was installed vs already present.

### Step 2: Install Python Dependencies

Run `uv sync` to install core dependencies (mcp, pyyaml).

Ask the user: "Do you want API integrations (Slack, Google Calendar, Linear, HubSpot, etc.)?"
- If yes: run `uv sync --extra integrations`
- If no: skip

### Step 3: Create Knowledge Base Directory Structure

The repo ships top-level dirs (`knowledge/`, `tasks/`, `meetings/`, `initiatives/`, `prototypes/`) via .gitkeep. This step creates **knowledge subdirectories**.

Create each if missing (preserve existing):
- `knowledge/about-me/`
- `knowledge/company-context/`
- `knowledge/product-strategy/`
- `knowledge/frameworks/`
- `knowledge/processes/`
- `knowledge/product-analytics/`
- `knowledge/references/`
- `knowledge/voice-samples/`

Report what was created vs already existed.

### Step 4: Create Template Files

Read templates from `references/setup-templates.md` in this skill directory.

Create only if files don't exist (never overwrite user content):
- `knowledge/about-me/about-me.md`
- `knowledge/company-context/company-overview.md`
- `knowledge/product-strategy/current-strategy.md`
- `knowledge/processes/how-we-work.md`
- `BACKLOG.md`
- `GOALS.md`

Report what was created vs already existed.

### Step 5: Configure AI & Search

**Skills directory:**
- `.claude/skills/` is committed to the repo and available out of the box — no symlink needed for Claude Code
- If user asked for **Cursor** setup: create `.cursor/skills` symlink pointing to `../.claude/skills` if not exists

**MCP configuration:**
`.mcp.json` is gitignored and does not ship with the repo. Handle accordingly:
- If `.mcp.json` exists: read it, check if `pm-tasks` server is configured. If not, add it.
- If `.mcp.json` missing: create it with pm-tasks config:
  ```json
  {
    "mcpServers": {
      "pm-tasks": {
        "command": "uv",
        "args": ["run", "python", "tools/mcp-servers/task-manager/server.py"]
      }
    }
  }
  ```
- If user asked for **Cursor** setup: do the same for `.cursor/mcp.json`

**Search (qmd):**
If qmd is available (`which qmd` succeeds):
1. Check existing collections (`qmd collection list`), add missing ones:
   - `qmd collection add knowledge/ --name knowledge`
   - `qmd collection add meetings/ --name meetings`
   - `qmd collection add initiatives/ --name initiatives`
   - `qmd collection add tasks/ --name tasks`
2. Add context descriptions:
   - `qmd context add knowledge "Product strategy, company context, frameworks, processes, analytics"`
   - `qmd context add meetings "Meeting transcripts and notes"`
   - `qmd context add initiatives "Strategic initiatives and groomed requests"`
   - `qmd context add tasks "Active tasks with priorities and progress"`
3. Run `qmd embed` to build the search index

If qmd not available: skip and note in verification.

### Step 6: Verification Checklist

Run actual checks and print results:

```
## Setup Verification

### Prerequisites
- [x/ ] uv installed
- [x/ ] bun installed
- [x/ ] qmd installed
- [x/ ] Python dependencies installed (uv run python -c "import mcp; import yaml")

### Knowledge Base
- [x/ ] knowledge/ subdirectories (8 dirs)

### Template Files
- [x/ ] about-me.md, company-overview.md, current-strategy.md, how-we-work.md
- [x/ ] BACKLOG.md, GOALS.md

### AI Configuration
- [x/ ] .claude/skills/ directory exists
- [x/ ] .mcp.json with pm-tasks server

### Search
- [x/ ] qmd collections configured (4: knowledge, meetings, initiatives, tasks)
- [x/ ] qmd index built
```

For any `[ ]` failures: provide the specific command to fix it.

**Next Steps** (print after checklist):
1. Fill in context files (about-me, company-overview, current-strategy, how-we-work) — 15-20 min
2. Define quarterly goals in GOALS.md
3. Start brain-dumping to BACKLOG.md
4. Say `/process-backlog` when ready
