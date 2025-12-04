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

## Category Index

Browse detailed workflows by category:

- [backlog.md](backlog.md) - Backlog & organization
- [documents.md](documents.md) - Document generation
- [planning.md](planning.md) - Prioritization & planning
- [research.md](research.md) - Research & analysis
- [metrics.md](metrics.md) - Metrics & success
- [communication.md](communication.md) - Stakeholder communication
- [decisions.md](decisions.md) - Decision making
- [technical.md](technical.md) - Technical collaboration
- [github.md](github.md) - GitHub & pull requests
- [bugs.md](bugs.md) - Bug & issue management
- [process.md](process.md) - Process improvement
- [frameworks.md](frameworks.md) - Templates & frameworks
- [maintenance.md](maintenance.md) - Maintenance & cleanup
- [goals.md](goals.md) - Goal setting & strategy
- [collaboration.md](collaboration.md) - Collaboration
- [launch.md](launch.md) - Launch & rollout

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
    "/plan": "Read @examples/workflows/planning.md",
    "/backlog": "Read @examples/workflows/backlog.md",
    "/spec": "Read @examples/workflows/documents.md and generate spec"
  }
}
```

---

## Core Workflows Explained

### 1. Backlog Processing

**Trigger**: `/backlog` or "Process my backlog"

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

## Workflow Files

Each `.md` file in this directory contains detailed workflows:

- **backlog.md** (53 lines) - Process & organize
- **documents.md** (140 lines) - Generate docs
- **planning.md** (137 lines) - Prioritize & plan
- **research.md** (120 lines) - Synthesize & analyze
- **metrics.md** (93 lines) - Metrics & dashboards
- **communication.md** (125 lines) - Stakeholder updates
- **decisions.md** (69 lines) - Document decisions
- **technical.md** (73 lines) - Tech collaboration
- **github.md** (67 lines) - GitHub & pull requests
- **bugs.md** (71 lines) - Bug management
- **process.md** (76 lines) - Process improvement
- **frameworks.md** (71 lines) - Apply frameworks
- **maintenance.md** (77 lines) - Cleanup & archive
- **goals.md** (78 lines) - OKRs & strategy
- **collaboration.md** (93 lines) - Team workflows
- **launch.md** (83 lines) - Launch planning

---

## Related

- **Tutorials**: See `examples/tutorials/` for step-by-step guides
- **Examples**: See `examples/example_files/` for sample outputs
- **Templates**: See `templates/` for document templates
- **AGENTS.md**: How AI processes these workflows
- **BACKLOG.md**: Your inbox for raw ideas
- **initiatives/**: Where processed ideas live

---

**Remember**: These workflows are starting points. AI understands natural language, so talk to it like a colleague. The slash commands are shortcuts, not rigid syntax.
