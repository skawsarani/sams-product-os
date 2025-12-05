# Task Example

Example of a task file created when processing backlog or created directly.

---

## Format

Each task file uses frontmatter with metadata, followed by context and action items.

---

## Example Task File

```markdown
---
title: Follow up with Sarah about Q4 goals
category: outreach
priority: P1
status: n
created_date: 2024-12-02
due_date: 2024-12-06
resource_refs:
  - knowledge/product-strategy/2024-strategy.md
---

# Follow up with Sarah about Q4 goals

## Context
Need to align on OKRs for next quarter. Sarah mentioned she had some concerns about our current goals during last week's team meeting. This is blocking our quarterly planning session.

## Next Actions
- [ ] Schedule 30-min meeting with Sarah
- [ ] Review current Q4 goals document
- [ ] Prepare questions about her concerns
- [ ] Send calendar invite with agenda

## Progress Log
- 2024-12-02: Task created from backlog processing
```

---

## Task Categories

Tasks are auto-categorized using keywords from `config.yaml`:

- **technical**: code, api, database, deploy, fix, bug, implement, develop, debug, server
- **outreach**: email, contact, reach, meeting, call, follow, introduce, connect
- **research**: research, study, learn, investigate, analyze, explore, understand, evaluate
- **writing**: write, draft, document, blog, article, report, proposal, outline
- **admin**: schedule, organize, expense, invoice, calendar, filing, review
- **other**: Miscellaneous items

---

## Status Codes

- **n** (not_started): Task hasn't been started
- **s** (started): Work in progress
- **b** (blocked): Waiting on something/someone
- **d** (done): Task completed

---

## Updating Tasks

Ask the AI:
- "Mark task [name] as complete" → Updates status to `d`
- "Change task [name] priority to P0" → Updates priority
- "Update task [name]" → Can update multiple fields

---

## Tips

- Keep Next Actions specific and actionable
- Update Progress Log as you work
- Link to related knowledge files in resource_refs
- Use due_date for time-sensitive tasks

