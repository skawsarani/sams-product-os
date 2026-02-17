---
name: analyze-calendar
description: Analyzes Google Calendar events to surface meeting intelligence, focus blocks, prep needs, and schedule optimization. Invoked when asked about calendar events, daily schedule, meeting prep, focus time, or schedule analysis.
---

# Calendar Analysis

Analyze Google Calendar events and produce actionable intelligence: meeting classification, focus block identification, prep needs, and task-to-time alignment.

## CLI Reference

```bash
# Today's events
uv run python -m tools.integrations.google_calendar list-events --date today

# Tomorrow's events
uv run python -m tools.integrations.google_calendar list-events --date tomorrow

# Next N days
uv run python -m tools.integrations.google_calendar list-events --days 7

# Specific date
uv run python -m tools.integrations.google_calendar list-events --date 2026-02-10

# Search events
uv run python -m tools.integrations.google_calendar list-events --date today --query "standup"
```

## Workflow

### Phase 1: Fetch Calendar Data & Establish Context

1. **Capture current time** by running `date "+%Y-%m-%d %H:%M %Z"` to establish time awareness
2. Run the CLI to fetch events for the requested time range (default: today)
3. If doing a daily pulse, also fetch tomorrow's events for look-ahead context
4. Parse the JSON output -- each event contains: `summary`, `start`, `end`, `attendees`, `description`, `hangoutLink`, `location`, `organizer`, `creator`
5. **Filter declined events**: Remove events where the user's `responseStatus` is `"declined"`. If any were filtered, note the count for output: "(N declined event(s) hidden)"

### Phase 2: Analyze Events

#### Meeting Classification

Categorize each event by type based on attendee count and event attributes:

| Type | Heuristic |
|------|-----------|
| **1:1** | Exactly 2 attendees (including self) |
| **Small group** | 3-5 attendees |
| **Large meeting** | 6+ attendees |
| **All-hands** | Keywords in title: "all-hands", "town hall", "company", "team sync" |
| **External** | Attendees with email domains different from organizer |
| **Focus block** | No attendees, or keywords: "focus", "heads down", "no meetings", "blocked" |
| **Social/casual** | Keywords: "lunch", "coffee", "happy hour", "1:1 social" |

#### Time Analysis

Calculate from the event list:

- **Working window**: Default to 9am-5pm, but if the first event starts before 9am or the last event ends after 5pm, extend the window to match actual calendar boundaries. Use the adjusted window for all calculations below.
- **Total meeting time** vs. total working hours (based on adjusted working window)
- **Meeting density**: percentage of working window in meetings
- **Current-time context** (for today only):
  - Mark past events as completed (dimmed in output)
  - Highlight the next upcoming event with time-until: `NEXT UP: [Event] in [X] min`
  - Only show "NEXT UP" when the next event is within 2 hours
- **Focus blocks**: Gaps of 30+ minutes between meetings -- list each with start time, duration, and a recommendation. For today, only show remaining focus blocks (exclude blocks that already passed).
- **Back-to-back warnings**: Flag sequences of 2+ meetings with no gap
- **Overbooked flag**: If meeting density exceeds 80%, explicitly warn

#### Prep Identification

Flag events that likely need preparation:

- Events with descriptions containing links, docs, or agendas
- Events with "review", "demo", "presentation", "pitch", "planning" in the title
- External meetings (different domain attendees)
- Events where the user is the organizer (they likely need to lead/present)

#### Meeting Intelligence

Flag high-priority meetings:

- Meetings with many attendees (6+)
- External-facing meetings
- Meetings with leadership (based on organizer or attendee patterns)
- First occurrence of a recurring meeting after a gap

### Validation

Before producing output, verify:
- Event count matches the raw data (no events lost or double-counted)
- Total meeting time adds up correctly against individual event durations
- Focus blocks don't overlap with meetings
- Past/future classification is correct based on current time
- Declined events are excluded from all calculations

### Phase 3: Task Alignment

When PM Tasks MCP is available:

1. Fetch P0/P1 tasks via `list_tasks` and overdue tasks via `find_overdue_tasks`
2. Map focus blocks to task priorities -- suggest which block to use for which task
3. If no focus blocks available, recommend rescheduling low-priority meetings or batching tasks into smaller chunks

### Output Format

```
Daily Pulse for [Day, Date]

NEXT UP: [Event] in [X] min                    ← only if next event within 2h

TOP 3 PRIORITIES
1. [Most important meeting or task with context]
2. [Second priority]
3. [Third priority]

CALENDAR ([X] meetings, [Y]h [Z]m total, [N]% of day) (N declined hidden)

  HIGH-IMPACT
  - [Time] [Event Name] ([Type]) -- [Why it matters / Prep needed]

  ALL EVENTS
  - ~~[Time]-[Time] [Past Event] ([Type])~~     ← past events dimmed
  - [Time]-[Time] [Event Name] ([Type], [N] attendees)   ← upcoming
  - [Time]-[Time] [Event Name] ([Type], [N] attendees)

  SCHEDULING NOTES
  - [Back-to-back warnings, overbooked alerts, conflicts]
  - Working window: [Adjusted start]-[Adjusted end] (extended from default if applicable)

FOCUS BLOCKS (remaining today)
  - [Start]-[End] ([Duration]) -- [Suggested use based on tasks]

PREP NEEDED
  - [Event at Time]: [What to prepare -- links, docs, agenda items]

TOMORROW LOOK-AHEAD (if fetched)
  - [N] meetings, [Key event to note]
```

Adjust the output based on the request:
- **Ad-hoc calendar query** ("what meetings do I have Thursday"): Show just the events list, skip task alignment
- **Daily pulse / morning briefing**: Full output with all sections
- **Meeting prep** ("what do I need to prep for"): Focus on Prep Needed section
- **Focus time** ("when can I do deep work"): Focus on Focus Blocks section
- **Week overview**: Show per-day summary with meeting counts and density
