---
allowed-tools: process_backlog, clear_backlog, check_duplicates, create_task, list_tasks, Glob, Read, Write
argument-hint:
description: Process BACKLOG.md into organized tasks, opportunities, and references
---

## Context

Configuration for backlog processing is in `core/config.yaml`:
- Priority caps: P0 max 3, P1 max 7, P2 max 15
- Category keywords for auto-assignment
- Duplicate detection thresholds

Today's date: 2026-01-06

## Your task

**Read and follow the workflow in `workflows/process-backlog.md`**

The workflow contains complete instructions for:
- Using MCP tools (`process_backlog`, `clear_backlog`) with manual failover
- Categorization logic (tasks/opportunities/references)
- Duplicate detection
- Priority assignment and cap enforcement
- File creation formats
- Archiving process

**Key reminders:**
- Prefer MCP tools, mention if falling back to manual processing
- Ask for clarification on ambiguous items BEFORE creating
- Check duplicates against existing tasks/opportunities
- Link tasks to goals from GOALS.md in the Context section
- Enforce priority caps - ask user what to demote if exceeded
