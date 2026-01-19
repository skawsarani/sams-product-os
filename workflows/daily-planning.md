---
allowed-tools: list_tasks, find_overdue_tasks, get_task_summary, Glob, Read
argument-hint: [optional: "2 hours" for time-constrained, "one thing" for focus mode]
description: Plan your day with top priorities, blockers, and goal alignment
---

## Context

Tasks are in `tasks/` with YAML frontmatter (priority, status, due_date, category).
Goals are in `GOALS.md`.
Today's date: $TODAY

**Best timing:** First thing in morning, before checking email/Slack

## Your Task

Help the user start their day with clarity on top priorities.

If user provided arguments: $ARGUMENTS
- "2 hours" or time constraint → Use Time-Constrained variation
- "one thing" or "overwhelmed" → Use Focus Mode variation
- "yesterday" or "context" → Use Context Recovery variation

## Step 1: Process Yesterday's Transcripts

**Actions:**
1. Invoke `/process-transcripts 1` to check for and process transcripts from yesterday
2. The process-transcripts workflow will:
   - Find any unprocessed transcripts from the previous day
   - Present detailed findings (tasks, initiatives, references)
   - Ask for confirmation before creating items
3. If no transcripts found, note "No transcripts from yesterday to process"
4. Proceed to priority identification after transcript processing completes

**Note:** This ensures action items from yesterday's meetings are captured before planning today's work.

## Step 2: Identify Today's Top Priorities

**Actions:**
1. Read `tasks/` directory for:
   - P0 tasks (not done)
   - P1 tasks (not done)
   - Tasks with due dates today or overdue
2. Read `GOALS.md` for goal context
3. Prioritize by:
   - Urgency (due dates, blockers)
   - Goal alignment
   - Dependencies (what unblocks others)

**Output format:**
```
## Today's Top 3 Priorities

### 1. [Task Name] (P0)
**Goal:** [Goal name from GOALS.md]
**Why today:** [Urgency/impact context]
**Next action:** [Specific first step]

### 2. [Task Name] (P1)
**Goal:** [Goal name]
**Why today:** [Context]
**Next action:** [First step]

### 3. [Task Name] (P1)
**Goal:** [Goal name]
**Why today:** [Context]
**Next action:** [First step]
```

## Step 3: Check for Blocked Items

**Actions:**
1. Find tasks with status `b` (blocked)
2. Identify if any blockers can be resolved today

**Output format:**
```
## Blocked Items

**[Task name]** (P0) - Blocked on: [Dependency]
- Can you unblock today? [Yes/No + suggestion]

[If none: "No blocked items today."]
```

## Step 4: Offer Support

```
**Ready to start?**
- Say "start [task name]" to mark task as in progress
- Say "I only have 2 hours" for a time-constrained plan
- Say "What's the ONE thing?" if overwhelmed
```

---

## Variations

### Time-Constrained Day

**When to use:** User specifies a time constraint like "2 hours" or passes time argument

```
## [X]-Hour Focus Plan

**Realistically achievable:**
1. **[Task]** - [Time estimate] - [First actionable chunk]
2. **[Task]** - [Time estimate] - [Completable subtask]

**Buffer:** 15 min for context switching

**Defer to later:** [List of tasks moved to tomorrow]
```

### Focus Mode (Overwhelmed)

**When to use:** User passes "one thing" argument or indicates feeling overwhelmed

```
## Your ONE Thing Today

**[Task Name]**
**Why this:** [Highest impact / Most urgent / Unblocks most]
**Success looks like:** [Clear completion criteria]

Everything else can wait.
```

### Context Recovery

**When to use:** User passes "yesterday" or "context" argument to recover previous work context

**Actions:**
1. Find tasks with status `s` (started)
2. Check for recently updated tasks

```
## Yesterday's Context

**You were working on:**
- [Task 1] - Status: [In progress / Completed]
- [Task 2] - Status: [In progress / Blocked]

**Natural next step:** [Suggestion for today]
```

---

## Best Practices

- Keep this session under 2 minutes
- Focus on outcomes, not activity
- Mark tasks as started when you begin work
- If user seems stuck choosing, make a recommendation
