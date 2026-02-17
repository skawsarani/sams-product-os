---
name: daily-pulse
description: Generates a morning briefing combining calendar intelligence with task priorities and goal alignment. Invoked via /daily-pulse or "morning pulse", "what's my day look like". Supports variations: tomorrow, week, "2 hours", "one thing", yesterday.
allowed-tools: list_tasks, find_overdue_tasks, get_task_summary, Glob, Read, Bash
argument-hint: [optional: "tomorrow", "week", "2 hours", "one thing", "yesterday"]
---

## Context

Tasks are in `tasks/` with YAML frontmatter (priority, status, due_date, category).
Goals are in `GOALS.md`.
Today's date: $TODAY
Arguments: `$ARGUMENTS` (optional — see variations: tomorrow, week, 2 hours, one thing, yesterday)

**Best timing:** First thing in morning, before checking email/Slack

## Your Task

Generate a comprehensive morning pulse that combines calendar intelligence with task priorities.

If user provided arguments: $ARGUMENTS
- "tomorrow" → Use Tomorrow Look-Ahead variation
- "week" → Use Week Overview variation
- "2 hours" or time constraint → Use Time-Constrained variation
- "one thing" or "overwhelmed" → Use Focus Mode variation
- "yesterday" or "context" → Use Context Recovery variation

---

## Default: Full Morning Pulse

### Step 1: Check Yesterday's Meeting Transcripts

**Actions:**
1. Use Glob to check for transcripts from yesterday in `meetings/` (files with yesterday's YYYY-MM-DD prefix)
2. If transcripts found: note "N transcript(s) from yesterday available — run `/process-meetings` to review"
3. If no transcripts found: skip silently (don't mention it)
4. Proceed immediately to calendar analysis — do not block on transcript processing

### Step 2: Calendar Intelligence

**Actions:**
1. Fetch today's events:
   ```bash
   uv run python -m tools.integrations.google_calendar list-events --date today
   ```
2. Invoke the `analyze-calendar` skill to analyze the fetched events (it handles classification, density, focus blocks, prep identification, and all calendar intelligence)
3. Optionally fetch tomorrow for look-ahead context

### Step 3: Task Priorities

**Actions:**
1. Read `tasks/` directory for:
   - P0 tasks (not done)
   - P1 tasks (not done)
   - Tasks with due dates today or overdue
2. Read `GOALS.md` for goal context
3. Find blocked tasks (status `b`) and identify if any can be unblocked today
4. Prioritize by: urgency (due dates, blockers), goal alignment, dependencies

### Step 4: Synthesize

Combine calendar + tasks into a unified briefing. Map focus blocks to task priorities.

**Omit any section that would be empty — don't show headers or placeholder text for empty sections.** For example, if there are no blocked items, skip the BLOCKED ITEMS section entirely. If no prep is needed, skip PREP NEEDED.

**Output format:**
```
Daily Pulse for [Day, Date]

TOP 3 PRIORITIES
1. [Task or meeting with context]
   Goal: [Goal name from GOALS.md]
   Why today: [Urgency/impact]
   Next action: [Specific first step]

2. [Second priority]
   ...

3. [Third priority]
   ...

CALENDAR ([X] meetings, [Y]h [Z]m total, [N]% of day)

  HIGH-IMPACT
  - [Time] [Event] ([Type]) -- [Why / Prep needed]

  ALL EVENTS
  - [Time]-[Time] [Event] ([Type], [N] attendees)
  - ...

  SCHEDULING NOTES
  - [Back-to-back warnings, overbooked alerts]

FOCUS BLOCKS
  - [Start]-[End] ([Duration]) -- [Suggested task: Task Name (P0)]
  - [Start]-[End] ([Duration]) -- [Suggested use]

PREP NEEDED
  - [Event at Time]: [What to prepare]

BLOCKED ITEMS
  [Task name] (P0) - Blocked on: [Dependency]
  - Can you unblock today? [Yes/No + suggestion]

MEETING TRANSCRIPTS
  N transcript(s) from yesterday available — run `/process-meetings` to review

TOMORROW LOOK-AHEAD
  - [N] meetings, [Key event to note]
```

### Step 5: Offer Support

```
Ready to start?
- Say "start [task name]" to mark task as in progress
- Say "I only have 2 hours" for a time-constrained plan
- Say "What's the ONE thing?" if overwhelmed
```

---

## Variations

### Tomorrow Look-Ahead

**When to use:** User passes "tomorrow" argument

**Actions:**
1. Fetch tomorrow's events:
   ```bash
   uv run python -m tools.integrations.google_calendar list-events --date tomorrow
   ```
2. Analyze with analyze-calendar skill
3. Show tasks with due dates tomorrow
4. Skip meeting transcript check

**Output:** Calendar analysis for tomorrow + tasks due tomorrow

### Week Overview

**When to use:** User passes "week" argument

**Actions:**
1. Fetch next 7 days of events:
   ```bash
   uv run python -m tools.integrations.google_calendar list-events --days 7
   ```
2. Summarize per-day: meeting count, total meeting time, meeting density
3. Show tasks due this week from `tasks/`
4. Skip meeting transcript check

**Output format:**
```
Week Overview ([Date Range])

[Day]  [N] meetings  [X]h  [Light/Moderate/Heavy]
[Day]  [N] meetings  [X]h  [Light/Moderate/Heavy]
...

BUSIEST DAY: [Day] -- [Context]
LIGHTEST DAY: [Day] -- Best for deep work

TASKS DUE THIS WEEK
- [Task] (P0) - Due [Day]
- [Task] (P1) - Due [Day]
```

### Time-Constrained Day

**When to use:** User specifies a time constraint like "2 hours"

**Actions:**
1. Run calendar analysis for today (identify available focus blocks)
2. Match tasks to available blocks within time constraint

```
[X]-Hour Focus Plan

Realistically achievable:
1. [Task] - [Time estimate] - [Suggested block: Start-End]
2. [Task] - [Time estimate] - [Suggested block: Start-End]

Buffer: 15 min for context switching

Defer to later: [Tasks moved to tomorrow]
```

### Focus Mode (Overwhelmed)

**When to use:** User passes "one thing" argument or indicates feeling overwhelmed

```
Your ONE Thing Today

[Task Name]
Why this: [Highest impact / Most urgent / Unblocks most]
Best time: [Suggested focus block from calendar]
Success looks like: [Clear completion criteria]

Everything else can wait.
```

### Context Recovery

**When to use:** User passes "yesterday" or "context" argument

**Actions:**
1. Find tasks with status `s` (started)
2. Check for recently updated tasks
3. Show today's first meeting for time context

```
Yesterday's Context

You were working on:
- [Task 1] - Status: [In progress / Completed]
- [Task 2] - Status: [In progress / Blocked]

Natural next step: [Suggestion]
First meeting today: [Time] - [Event] (you have [X] min before it)
```

---

## Best Practices

- Keep this session under 2 minutes
- Focus on outcomes, not activity
- Mark tasks as started when you begin work
- If user seems stuck choosing, make a recommendation
- If calendar fetch fails, proceed with task-only pulse and note the issue
