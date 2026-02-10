---
allowed-tools: list_tasks, check_duplicates, create_task, Glob, Read, Write
argument-hint: [days] (optional, default: 3)
description: Extract action items from recent meeting transcripts and present for review before creating
---

## Context

- Config: `config.yaml` (priority caps, category keywords, duplicate thresholds)
- Today's date: $TODAY
- Time window: Past 3 days (or user-specified via `$ARGUMENTS`)
- Processing log: `knowledge/transcripts/.processed-meetings`

## Workflow

**Always present findings for user review before creating anything.**

### Step 1: Find Recent Transcripts

Use Glob to find transcripts in `knowledge/transcripts/` with YYYY-MM-DD prefixes from the past N days.

If MCP available, use MCP tools. Otherwise, use direct file operations.

### Step 1.5: Filter Already-Processed

Read `knowledge/transcripts/.processed-meetings`. Remove any found transcripts that are already listed. Report: "Found X transcripts, Y already processed, Z new." If zero new, stop early and tell the user.

### Step 2: Analyze Each Transcript

Read each transcript and extract items into three categories:

| Category | What to Extract |
|----------|-----------------|
| **Tasks** | Direct assignments, commitments made, follow-ups, decisions needing action, blockers |
| **Initiatives** | Product opportunities, feature requests, strategic discussions, pain points |
| **References** | Links, competitor info, data points, resources to save |

**Skip**: General discussion, other people's action items, sentiment/small talk.

#### Parallel Processing (3+ Transcripts)

When 3+ transcripts are found, use parallel processing for efficiency:

1. **Group transcripts into batches** of 2-3 files each

2. **Launch parallel agents** to process each batch:
   ```
   Task(subagent_type="Explore", prompt="Analyze transcripts [paths] and extract: tasks (assignments, follow-ups, decisions), initiatives (opportunities, features, pain points), references (links, data points). Return structured list with source attribution.")
   ```

3. **Each agent extracts** from its batch:
   - Tasks with priority suggestion and due date (if mentioned)
   - Initiatives with description and source meeting
   - References with context

4. **Merge results** from parallel agents:
   - Combine all extracted items
   - Check for duplicates across batches (same topic from different meetings)
   - Flag items that appear in multiple transcripts (likely higher priority)

5. **Deduplicate** merged items before presenting to user

**When to use parallel processing:**
- 3+ transcripts found in the time window
- Transcripts are from different meetings
- Need faster processing

**When to use sequential processing:**
- 1-2 transcripts
- Transcripts are from a multi-part meeting
- Deep context preservation is critical

### Step 3: Check for Duplicates

Compare extracted items against existing tasks in `tasks/`, initiatives in `knowledge/initiatives/`.

### Step 4: Present Findings

Show user a summary with:
- **Transcripts processed**: Table with date, meeting name, items found
- **Tasks**: Table with title, category, priority, due date, source
- **Initiatives**: Bullet list with name, description, source
- **References**: Bullet list
- **Possible duplicates**: Similar existing items with match %
- **Ambiguous items**: Vague items needing clarification

### Step 5: Get Confirmation

Ask: "How would you like to proceed?"

**Wait for user response before creating anything.**

### Step 6: Enforce Priority Caps

Check caps from `config.yaml` before creating. If exceeded:
1. Show current tasks at that priority
2. Ask user to demote existing or downgrade new task
3. Wait for decision

### Step 7: Create Approved Items

**Tasks**: Use `create_task` MCP tool or create file with frontmatter:
- title, category, priority, due_date (if mentioned), status: n
- Include source transcript in Context section
- Link to relevant goal from `GOALS.md`

**Initiatives**: Use template from `templates/initiative-template.md`, include source meeting.

**References**: Add to existing file or create new in `knowledge/references/`.

### Step 8: Summary

Report what was created:
- Tasks by priority level
- Initiatives and references created
- Skipped items (duplicates, declined, ambiguous)
- Transcripts processed

Append all processed transcript paths (relative to `knowledge/transcripts/`) to `knowledge/transcripts/.processed-meetings`, one per line.

## Extraction Examples

| Source Text | Extract As |
|-------------|------------|
| "Sam, can you follow up with Neil about the API?" | Task: "Follow up with Neil on API integration" |
| "I'll send the updated spec by Wednesday" | Task: "Send updated spec" (due: Wednesday) |
| "Users are complaining about slow mobile startup" | Initiative: "Mobile Performance Issues" |
| "Check out that TechCrunch article on Stripe" | Reference: Link to article |
| "That's interesting" / "It's been a rough day" | Skip (not actionable) |

## Key Reminders

- **Never auto-create** - Always present findings first
- **Be selective** - Only extract clear, actionable items for tasks
- **Link context** - Always reference source meeting
- **Check duplicates** - Meeting discussions often overlap with existing work
- **Preserve transcripts** - Never modify or delete transcript files
