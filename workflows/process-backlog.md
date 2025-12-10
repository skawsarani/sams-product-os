## Process Backlog

### Process Backlog

```
Process my backlog
```

**What it does**:
- Reads items from `BACKLOG.md` (your daily inbox)
- **Categorizes each item** into:
  - **Initiatives**: Product opportunities, features, strategic work → `initiatives/` folder
  - **Tasks**: Actionable, time-bound, operational work → `tasks/` folder
  - **References**: Useful info, links, context → `knowledge/references/`
  - **Uncategorized**: Meeting notes, random thoughts → archived in `knowledge/notes/YYYY-MM-DD.md`
- **Deduplication**: Checks against existing initiatives, tasks, and references across all categories
- Creates structured files for each category
- Archives remaining inbox content to `knowledge/notes/YYYY-MM-DD.md`
- Clears `BACKLOG.md` for next day

**When to use**: Daily or weekly, when inbox needs processing

**Detailed Steps**:

1. Read items from `BACKLOG.md` (single file at root)
2. **Categorize each item** into one of:
   - **Initiative**: Product opportunities, features, strategic work → `initiatives/` folder (opportunity assessment)
   - **Task**: Actionable, time-bound, operational work → `tasks/` folder (task file with frontmatter)
   - **Reference**: Useful info, links, context → `knowledge/references/`
   - **Uncategorized**: Items that don't fit above categories (meeting notes, random thoughts) remain in `BACKLOG.md` and will be archived with the snapshot
3. **Deduplication** (applies to ALL categories):
   - Check against existing initiatives, tasks, and references
   - Use similarity threshold from `config.yaml` (default 0.6)
   - Flag potential duplicates across all categories
   - Suggest merging or linking related items
4. For initiatives: Create opportunity assessment in `initiatives/` folder with this format:
   - **Objective**: What we're trying to achieve
   - **Target Customer**: Who this serves
   - **Success Metrics**: How we measure impact (specific, measurable)
   - **What We Know**: Current data, insights, evidence
   - **What We Should Research**: Open questions, validation needed
   - **Solution Ideas**: Potential approaches (not decisions yet)
   - **Risks**: What could go wrong
   - **Questions to Validate**: Key assumptions to test
   - Prioritize: P0 (Critical), P1 (High), P2 (Medium), P3 (Low)
5. For tasks: Create task file in `tasks/` folder with frontmatter:
   - title, category (auto-assigned using config.yaml keywords), priority, status (default: n), created_date, due_date (if mentioned), resource_refs
   - Include Context, Next Actions, and Progress Log sections
6. For references: Move to appropriate reference file or create new one in `knowledge/references/`
7. Remove processed items (initiatives, tasks, references) from `BACKLOG.md`
8. After processing, archive entire remaining `BACKLOG.md` content to `knowledge/notes/YYYY-MM-DD.md` (single file per day)
   - This archived snapshot contains all uncategorized items (meeting notes, random thoughts, etc.)
9. Clear `BACKLOG.md` for next day
10. Summarize what was created/categorized

---

### Quick Triage

```
Triage the items in BACKLOG.md
```

**What it does**:
- Quick categorization without full processing
- Assigns categories and priorities
- Flags urgent items and potential duplicates

**When to use**: Quick check before full processing

---

### Archive Completed Work

```
Archive completed work from [timeframe, e.g., "last quarter"]
```

**What it does**:
- Identifies completed items (initiatives, tasks, specs)
- Moves to `archive/` with date prefix
- Maintains directory structure
- Logs what was archived

**When to use**: Monthly/quarterly cleanup

---

### Update Knowledge Base

```
Review my knowledge/ folder and identify gaps or outdated content
```

**What it does**:
- Checks freshness of docs
- Identifies missing context
- Suggests updates or new docs needed
- Prioritizes by importance

**When to use**: Quarterly maintenance

---

### Consolidate Duplicate Content

```
Find and consolidate duplicate information in [folder]
```

**What it does**:
- Identifies similar or duplicate content
- Suggests consolidation approach
- Creates canonical versions
- Updates references

**When to use**: When things feel scattered

---

### Prioritize Backlog Items

```
Help me prioritize these backlog items: [paste list or reference file]
```

**What it does**:
- Applies prioritization framework (RICE, Impact/Effort, etc.)
- References product strategy
- Provides rationale for each priority
- Helps decide what becomes initiatives vs tasks

**When to use**: Planning sessions, backlog reviews
