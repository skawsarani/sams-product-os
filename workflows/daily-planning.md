# Daily Planning Workflow

When user says: "What should I work on today?", "Help me plan my day", or "Daily standup"

---

## Purpose

Start your day with clarity on top priorities, time constraints, and goal alignment. This is your daily focus filter to avoid reactive mode.

**Best timing:** First thing in morning, before checking email/Slack

---

## Workflow Steps

### Step 1: Identify Today's Top Priorities

**Prompt the user:**
> Let me show you today's top priorities.

**Actions:**
1. Read `tasks/` directory for:
   - P0 tasks (not done)
   - P1 tasks (not done)
   - Tasks with due dates today or overdue
2. Read GOALS.md for goal context
3. Prioritize by:
   - Urgency (due dates, blockers)
   - Goal alignment
   - Dependencies (what unblocks others)

**Output format:**
```
## Today's Top 3 Priorities

### 1. [Task Name] (P0)
**Goal:** [Goal name from GOALS.md]
**Time estimate:** [X hours]
**Why today:** [Urgency/impact context]
**Next action:** [Specific first step]

### 2. [Task Name] (P1)
**Goal:** [Goal name]
**Time estimate:** [X hours]
**Why today:** [Context]
**Next action:** [First step]

### 3. [Task Name] (P1)
**Goal:** [Goal name]
**Time estimate:** [X hours]
**Why today:** [Context]
**Next action:** [First step]

**Total time:** [Sum of estimates]
```

---

### Step 2: Check for Blocked Items

**Actions:**
1. Find tasks with status `b` (blocked)
2. Identify if any blockers can be resolved today

**Output format:**
```
## 🚧 Blocked Items

**[Task name]** (P0) - Blocked on: [Dependency]
- Can you unblock today? [Yes/No + suggestion]

[If none:]
No blocked items today.
```

---

### Step 3: Offer Support

**Output:**
```
**Ready to start?**
- Say "start [task name]" to mark task as in progress
- Say "I only have 2 hours" for a time-constrained plan
- Say "What's the ONE thing?" if overwhelmed
```

---

## Variations

### Time-Constrained Day
**User says:** "I only have 2 hours before meetings"

**Response:**
```
## 2-Hour Focus Plan

**Realistically achievable:**
1. **[Task]** - [1 hour] - [First actionable chunk]
2. **[Task]** - [45 min] - [Completable subtask]

**Buffer:** 15 min for context switching

**Defer to later:** [List of P1 tasks moved to tomorrow]
```

### Overwhelmed Mode
**User says:** "What's the ONE thing I should focus on?"

**Response:**
```
## Your ONE Thing Today

**[Task Name]**
**Why this:** [Highest impact / Most urgent / Unblocks most]
**Time:** [X hours]
**Success looks like:** [Clear completion criteria]

Everything else can wait.
```

### Context Recovery
**User says:** "Remind me what I was working on yesterday"

**Actions:**
1. Find tasks updated yesterday
2. Check tasks with status `s` (started)

**Response:**
```
## Yesterday's Context

**You were working on:**
- [Task 1] - Status: [In progress / Completed]
- [Task 2] - Status: [In progress / Blocked]

**Natural next step:** [Suggestion for today]
```

---

## Best Practices

**For PM daily planning:**
- Run BEFORE checking communications (email/Slack)
- Keep session under 2 minutes
- Focus on outcomes, not activity
- Let AI decide when you're stuck choosing
- Mark tasks as started when you begin

**Frequency:**
- Every morning at same time
- Skip weekends unless needed
- Use weekly-review.md on Fridays/Sundays

---

## Related Files

- `GOALS.md` - Goal context for prioritization
- `tasks/` - All task files
- `workflows/weekly-review.md` - Weekly strategic planning
- `core/config.yaml` - Priority and category definitions
