# PM Co-Pilot Workflows

AI-powered workflows for product management. These are your slash commands for Cursor and Claude Code.

---

## Quick Reference

### 🚀 Daily Workflows

```
/plan           → "What should I work on today?"
/backlog        → Process BACKLOG.md into initiatives
/prioritize     → Prioritize work based on strategy
```

### 📋 Initiatives & Documents

```
/expand-initiative [name]  → Add research and details before PRD
/spec [initiative]         → Generate product spec from initiative
/prd [initiative]          → Generate full PRD from initiative
/stories [initiative]      → Generate user stories from initiative
/brief [project]           → Create project brief
```

### 💬 Communication

```
/exec-update    → Draft executive update with metrics
/team-update    → Write team update
/stakeholder    → Prepare for stakeholder meeting
/faq [topic]    → Generate FAQ
```

### 📊 Research & Analysis

```
/synthesize     → Synthesize research from knowledge/transcripts/
/insights [file]→ Extract key insights
/feedback       → Analyze customer feedback
/competitive    → Competitive analysis
```

### 🔍 Decision & Planning

```
/decide [decision] → Document decision
/evaluate          → Evaluate options
/sprint            → Plan next sprint
/roadmap           → Create/update roadmap
/weekly            → Plan this week
```

---

## Workflow Index (Action-Based)

Browse workflows by action:

### Process & Organize
- [process-backlog.md](process-backlog.md) - Process backlog items into initiatives, tasks, references
- [archive-completed.md](archive-completed.md) - Archive completed work

### Generate & Create
- [generate-docs.md](generate-docs.md) - Generate specs, PRDs, briefs, user stories
- [use-structured-prompts.md](use-structured-prompts.md) - Use structured workflow prompts

### Plan & Prioritize
- [prioritize-work.md](prioritize-work.md) - Prioritize work, create roadmaps, plan sprints
- [plan-launch.md](plan-launch.md) - Plan launches and rollouts
- [set-goals.md](set-goals.md) - Set OKRs and align to strategy

### Research & Analyze
- [synthesize-research.md](synthesize-research.md) - Synthesize research and interviews
- [track-metrics.md](track-metrics.md) - Track and analyze metrics

### Communicate
- [write-update.md](write-update.md) - Write stakeholder updates and communications

### Document & Decide
- [document-decision.md](document-decision.md) - Document decisions and evaluate options

### Manage & Collaborate
- [manage-tasks.md](manage-tasks.md) - Manage tasks
- [triage-bugs.md](triage-bugs.md) - Triage and manage bugs
- [collaborate-engineering.md](collaborate-engineering.md) - Collaborate with engineering
- [collaborate-team.md](collaborate-team.md) - Collaborate with team

### Review & Improve
- [review-pr.md](review-pr.md) - Review pull requests
- [improve-process.md](improve-process.md) - Improve processes
- [apply-framework.md](apply-framework.md) - Apply PM frameworks

---

## Setup Slash Commands

### For Cursor

The `.cursorrules` file in project root has 30+ pre-configured slash commands.

**Usage**: Just type `/plan` or `/backlog` in Cursor chat!

**Add Your Own**:
Edit `.cursorrules` to add custom workflows.

### For Claude Code

Add to project instructions:

```markdown
When I use shortcuts like /plan, /backlog, /spec, read the corresponding
workflow file in examples/workflows/ and execute it.

Always reference:
- @AGENTS.md for behavior
- @templates/ for document structure
- @knowledge/ for context
```

### For Windsurf

```json
{
  "cascade.shortcuts": {
    "/plan": "Read @examples/workflows/prioritize-work.md",
    "/backlog": "Read @examples/workflows/process-backlog.md",
    "/spec": "Read @examples/workflows/generate-docs.md and generate spec"
  }
}
```

---

## Core Workflows Explained

### 1. Process Backlog

**Trigger**: `/backlog` or "Process my backlog"

**Workflow**: [process-backlog.md](process-backlog.md)

**What it does**:
1. Reads items from `BACKLOG.md`
2. Creates initiative files in `initiatives/` folder
3. Each initiative has opportunity assessment format:
   - Objective
   - Target customer
   - Success metrics
   - What we know
   - What we should research
   - Solution ideas
   - Risks
   - Questions to validate
4. Prioritizes as P0-P3
5. Clears processed items from BACKLOG.md

**When to use**: Weekly, or when BACKLOG.md has 5+ items

**Example**:
```
/backlog
→ Creates initiatives/mobile-performance.md
→ Creates initiatives/enterprise-sso.md
→ Clears BACKLOG.md
```

---

### 2. Expand Initiative

**Trigger**: `/expand-initiative [name]`

**Workflow**: [prioritize-work.md](prioritize-work.md)

**What it does**:
Before generating a PRD, expand the initiative with:
- Detailed research plan
- More solution options
- Risk analysis
- Validation approach
- Effort estimates
- Competitive analysis

**When to use**: After creating initiative, before committing to build

**Example**:
```
/expand-initiative mobile-performance
→ Adds detailed technical analysis needed
→ Adds user research plan
→ Evaluates 3-4 solution options
→ Flags gaps and questions
```

---

### 3. Generate PRD from Initiative

**Trigger**: `/prd [initiative-name]`

**Workflow**: [generate-docs.md](generate-docs.md)

**What it does**:
Converts initiative to full Product Requirements Document:
- Uses initiative's objective → problem statement
- Uses target customer → user personas
- Uses success metrics → KPIs
- Uses solution ideas → requirements
- Adds technical details, user stories, launch plan

**When to use**: After initiative is expanded and validated

**Example**:
```
/prd mobile-performance
→ Reads @initiatives/mobile-performance.md
→ Uses @templates/spec-template.md  
→ Generates comprehensive PRD
→ Saves to initiatives/mobile-performance/prd.md
```

---

## Common Patterns

### Monday Morning

```
1. /plan
   "What should I work on this week?"

2. /backlog
   "Process weekend ideas"

3. /prioritize
   "Help me prioritize based on @knowledge/product-strategy/"
```

### Feature Kick-off

```
1. Create initiative (from backlog or manually)
2. /expand-initiative [name]
3. Review and validate assumptions
4. /prd [name]
5. /stories [name]
6. /tech-req [name]
7. /brief [name]
```

### Research Synthesis

```
1. Add transcripts to knowledge/transcripts/
2. /synthesize
3. /insights
4. Create initiatives from top opportunities
5. /prioritize
```

### Weekly Update

```
1. /metrics
   "Get latest numbers from @knowledge/product-analytics/"

2. /exec-update
   "Draft update for leadership"

3. (Iterate)
   "Make it more concise"
   "Add more on blockers"
```

---

## Tips for Success

### 1. Be Specific
❌ `/spec`  
✅ `/spec mobile-onboarding-redesign`

### 2. Add Context
❌ `/update`  
✅ `/exec-update on Q1 mobile initiative including latest metrics from @knowledge/product-analytics/`

### 3. Reference Files
Always use @ mentions:
```
/spec mobile-redesign using insights from @knowledge/briefs-and-specs/mobile-study.md
```

### 4. Chain Workflows
```
"First /backlog to process ideas,
then /prioritize based on strategy,
then /spec for top 2 P0 initiatives"
```

### 5. Iterate
Don't expect perfection first try:
```
/spec feature-name
→ "Add more detail on success metrics"
→ "Make technical requirements more specific"
→ "Add competitive analysis section"
```

---

## All Workflow Files

Each `.md` file in this directory contains detailed workflows:

**Process & Organize**:
- **process-backlog.md** - Process backlog items
- **archive-completed.md** - Archive completed work

**Generate & Create**:
- **generate-docs.md** - Generate specs, PRDs, briefs
- **use-structured-prompts.md** - Structured workflow prompts

**Plan & Prioritize**:
- **prioritize-work.md** - Prioritize and plan work
- **plan-launch.md** - Plan launches
- **set-goals.md** - Set goals and OKRs

**Research & Analyze**:
- **synthesize-research.md** - Synthesize research
- **track-metrics.md** - Track metrics

**Communicate**:
- **write-update.md** - Write updates

**Document & Decide**:
- **document-decision.md** - Document decisions

**Manage & Collaborate**:
- **manage-tasks.md** - Manage tasks
- **triage-bugs.md** - Triage bugs
- **collaborate-engineering.md** - Collaborate with engineering
- **collaborate-team.md** - Collaborate with team

**Review & Improve**:
- **review-pr.md** - Review PRs
- **improve-process.md** - Improve processes
- **apply-framework.md** - Apply frameworks

---

## Related

- **Tutorials**: See `examples/tutorials/` for step-by-step guides
- **Examples**: See `examples/example_files/` for sample outputs
- **Templates**: See `templates/` for document templates
- **AGENTS.md**: How AI processes these workflows (lean reference guide)
- **BACKLOG.md**: Your inbox for raw ideas
- **initiatives/**: Where processed ideas live

---

**Remember**: These workflows are starting points. AI understands natural language, so talk to it like a colleague. The slash commands are shortcuts, not rigid syntax.
