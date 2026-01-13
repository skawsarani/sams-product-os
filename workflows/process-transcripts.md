---
allowed-tools: list_tasks, check_duplicates, create_task, Glob, Read, Write
argument-hint: [days] (optional, default: 3)
description: Extract action items from recent meeting transcripts and create tasks
---

## Context

You are processing meeting transcripts to extract actionable tasks, commitments, and follow-ups.

Configuration for task creation is in `core/config.yaml`:
- Priority caps: P0 max 3, P1 max 7, P2 max 15
- Category keywords for auto-assignment
- Duplicate detection thresholds

Today's date: $TODAY

## Your Task

Extract action items, commitments, and follow-ups from recent meeting transcripts in `knowledge/transcripts/` and convert them into organized tasks.

**Time window:** Process transcripts from the past 3 days (or user-specified days) based on YYYY-MM-DD filename prefix.

## Using MCP Tools (Preferred)

If the task-manager-mcp server is available:

### Step 1: Find Recent Transcripts

Use Glob to find all transcripts with YYYY-MM-DD prefixes from the past N days:
- Pattern: `knowledge/transcripts/**/*.md`
- Filter by date prefix (e.g., if today is 2026-01-12, look for 2026-01-10, 2026-01-11, 2026-01-12)

### Step 2: Read and Analyze Each Transcript

For each transcript, read the full content and extract:

**Action items to capture:**
- Direct tasks assigned to the user (e.g., "Sam, can you follow up with...")
- Commitments made by the user (e.g., "I'll send the update by Wednesday")
- Follow-ups mentioned (e.g., "Need to check in on X", "Resend the API docs")
- Decisions that require follow-through (e.g., "We agreed to scale back feature X - update the spec")
- Blockers or issues raised that need resolution

**What NOT to capture:**
- General discussion without action
- Context/background information
- Other people's action items (unless they need your follow-up)
- Strategic insights (these can go to opportunities via `/process-backlog`)

### Step 3: Check for Duplicates

Before creating tasks, use **check_duplicates** for each extracted item to:
- Avoid creating duplicate tasks
- Surface similar existing tasks
- Ask user whether to merge or create new

### Step 4: Create Tasks

For each unique action item, use **create_task** with:

```yaml
title: [Clear, actionable task title]
priority: P0/P1/P2/P3 (based on urgency/deadline mentioned)
due_date: YYYY-MM-DD (if deadline mentioned in transcript)
category: auto-assigned from keywords in core/config.yaml
keywords: [relevant, keywords, from, context]
body: |
  ## Context
  Source: [Transcript title and date]
  [Why this task matters, relevant context from meeting]

  ## Next Actions
  - [ ] [First concrete step]
  - [ ] [Second step if needed]

  ## Progress Log
  - $TODAY: Task created from transcript
```

**Priority assignment guidelines:**
- P0: Urgent, deadline today/tomorrow, blocking
- P1: Important, deadline this week, commitments made
- P2: Follow-ups, normal work, mentioned but not urgent
- P3: Nice to have, low priority mentions

### Step 5: Enforce Priority Caps

Check priority caps from `core/config.yaml`:
- P0: Max 3 tasks
- P1: Max 7 tasks
- P2: Max 15 tasks

If caps exceeded:
1. Use **list_tasks** to show current tasks at that priority level
2. Ask user: "You already have [N] P[X] tasks. Should I demote one, or make this new task P[X+1] instead?"
3. Wait for user decision before proceeding

### Step 6: Summary

After processing all transcripts, provide summary:
```
Processed N transcripts from [date range]:
- Created X tasks (P0: N, P1: N, P2: N, P3: N)
- Skipped Y items (duplicates or not actionable)
- Flagged Z items for clarification

Transcripts processed:
- YYYY-MM-DD - [Meeting title]
- YYYY-MM-DD - [Meeting title]
```

## Manual Processing (Fallback)

If MCP tools unavailable, mention "Note: Using direct file reading (MCP unavailable)" and follow these steps:

### Step 1: Find Recent Transcripts

Use Glob with pattern `knowledge/transcripts/**/*.md` and filter by YYYY-MM-DD prefix for past 3 days.

### Step 2: Read Each Transcript

Read full content and extract action items (same criteria as MCP approach above).

### Step 3: Check for Duplicates

Manually scan `tasks/` folder to check if similar tasks already exist.

### Step 4: Create Task Files

For each action item, create file in `tasks/` with frontmatter:

```yaml
---
title: Task name
category: auto-assigned from core/config.yaml keywords
priority: P0/P1/P2/P3
status: n
created_date: YYYY-MM-DD
due_date: YYYY-MM-DD (if mentioned in transcript)
source: transcript
source_file: knowledge/transcripts/path/to/transcript.md
---

## Context
Source: [Meeting title] on [date]
[Relevant context from the meeting about why this matters]

## Next Actions
- [ ] First step
- [ ] Second step

## Progress Log
- YYYY-MM-DD: Task created from transcript
```

### Step 5: Enforce Priority Caps

Manually count existing tasks at each priority level and check against caps. If exceeded, ask user before proceeding.

### Step 6: Summary

Provide summary of what was processed and created (same format as MCP approach).

## Key Reminders

- **Be selective** - Only create tasks for clear, actionable items assigned to the user
- **Link context** - Always reference the source meeting and why it matters
- **Check duplicates** - Meeting discussions often overlap with existing work
- **Link to goals** - Reference relevant goals from GOALS.md in task context
- **Clarify ambiguous items** - If an action item is vague, flag it for user clarification before creating
- **Preserve transcripts** - Never modify or delete transcript files (they're historical records)
- **Use due dates** - If a deadline or timeframe was mentioned ("by end of week", "Wednesday"), set due_date

## Examples of Action Items to Extract

**Good examples:**
- "Sam, can you follow up with Neil about the API integration?" → Task: "Follow up with Neil on API integration"
- "I'll send the updated spec by Wednesday" → Task: "Send updated spec" (due: Wednesday)
- "Need to check in on Michael and Rachel" → Task: "Check in on Michael and Rachel"
- "Let me know if there's anything else, I need to get some heads down to write metrics" → Task: "Write metrics and updates"
- "I'll keep driving Interac" → Task: "Continue driving Interac initiative"

**Bad examples (skip these):**
- "That's interesting" → Just discussion
- "Michael might be expecting this" → Someone else's context
- "The team needs to decide on X" → No clear action assigned to you
- "It's been a rough day" → Sentiment, not actionable

## Configuration

Default: Process past 3 days
User can override: `/process-transcripts 7` to process past week
