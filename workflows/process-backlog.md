---
allowed-tools: process_backlog, clear_backlog, check_duplicates, create_task, list_tasks, Glob, Read, Write
argument-hint:
description: Process BACKLOG.md into organized tasks, initiatives, and references
---

## Context

- Config: `core/config.yaml` (priority caps, category keywords, duplicate thresholds)
- Today's date: $TODAY

## Workflow

**Always present findings for user review before creating anything.**

### Step 1: Analyze Backlog

Read `BACKLOG.md` and categorize each item:

| Category | Destination | Examples |
|----------|-------------|----------|
| **Tasks** | `tasks/` | "Email Sarah about Q4", "Review PRD draft" - clear action + completion criteria |
| **Initiatives** | `knowledge/initiatives/` | "Mobile perf issues", "Enterprise SSO" - strategic ideas to explore |
| **References** | `knowledge/references/` | Articles, competitor info, research - context to save |
| **Notes** | Archive | Meeting notes, incomplete thoughts |

If MCP available, use **process_backlog** (auto_create=false). Otherwise, read files directly.

### Step 2: Check for Duplicates

Compare against existing items in `tasks/`, `knowledge/initiatives/`, `knowledge/references/`.

### Step 3: Present Findings

Show user a summary with:
- **Tasks**: Table with title, category, priority, due date
- **Initiatives**: Bullet list with name + description
- **References**: Bullet list
- **Ambiguous items**: Items needing clarification
- **Possible duplicates**: Similar existing items
- **Notes to archive**: Remaining content

### Step 4: Get Confirmation

Ask: "How would you like to proceed?"

**Wait for user response before creating anything.**

### Step 5: Resolve Ambiguities

For vague items, ask:
- What specific action should be taken?
- When does this need to be done?
- Why does this matter?

### Step 6: Enforce Priority Caps

Check caps from `core/config.yaml` before creating. If exceeded:
1. Show current tasks at that priority
2. Ask user to demote existing or downgrade new task
3. Wait for decision

### Step 7: Create Approved Items

**Tasks**: Use template from `templates/task-template.md` or create with frontmatter:
- title, category (from config keywords), priority, status: n, created_date, due_date
- Link to relevant goal from `GOALS.md` in Context section

**Initiatives**: Use template from `templates/initiative-template.md`

**References**: Add to existing file if related topic exists, or create new file

### Step 8: Archive & Clear

1. Archive remaining content to `knowledge/notes/YYYY-MM-DD.md`
2. Clear `BACKLOG.md`
3. Summarize: tasks created (by priority), initiatives, references, archived items

## Key Reminders

- **Never auto-create** - Always present findings first
- **Ask for clarification** on ambiguous items before creating
- **Link to goals** - If no goal fits, ask user to clarify why it matters
- Fewer clear items > many vague ones
