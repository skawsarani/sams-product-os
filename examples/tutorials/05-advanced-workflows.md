# Tutorial 5: Advanced Workflows

**Time**: 45 minutes  
**Goal**: Master complex workflows that chain multiple steps together for real PM work

---

## The Problem

You've learned the basics:
- ✅ Processing backlog
- ✅ Creating initiatives
- ✅ Generating specs

But real PM work is **multi-step**:
- Research → Synthesis → Initiative → PRD → Decision
- Multiple initiatives → Prioritization → Roadmap
- Metrics → Analysis → Update → Action Plan

**Solution**: Chain workflows together and use advanced patterns.

---

## Part 1: Deep Initiative Expansion (10 min)

### Beyond Basic Expansion

Tutorial 2 covered basic expansion. Here's the **advanced** version.

### Start with Initiative

You have `initiatives/mobile-performance.md` with basic opportunity assessment.

### Advanced Expansion Command

```
"Expand the mobile-performance initiative with deep research:

1. Technical analysis:
   - Performance benchmarks needed
   - Architecture review questions
   - Infrastructure impact assessment

2. User research plan:
   - Interview guide for power users
   - Survey questions for broader audience
   - Analytics queries to run

3. Competitive analysis:
   - How do competitors handle this?
   - What's industry standard?
   - What are we missing?

4. Solution evaluation:
   - At least 3 distinct approaches
   - Effort estimates (engineering weeks)
   - Risk assessment for each
   - ROI calculation

5. Validation approach:
   - What to test before building
   - How to measure success
   - What would make us pivot

Save expanded version to initiatives/mobile-performance/expanded.md"
```

### What You Get

**Structured research plan**:
- Specific questions to answer
- Data sources to query
- People to interview
- Experiments to run

**Multiple solution paths**:
- Option A: Quick fix (2 weeks, low risk, 20% improvement)
- Option B: Refactor (8 weeks, medium risk, 60% improvement)
- Option C: Rebuild (16 weeks, high risk, 90% improvement)

**Clear validation criteria**:
- "If user interviews show X, we should choose Option B"
- "If analytics show Y, we need Option C"
- "If technical review reveals Z, we pivot to different problem"

---

## Part 2: Research Synthesis (15 min)

### The Research → Action Gap

You have:
- 5 user interview transcripts
- 20 support tickets
- Survey results
- Analytics data

**Problem**: How do you turn this into actionable insights?

### Step 1: Collect Research

Save transcripts to `knowledge/transcripts/`:

```
knowledge/transcripts/
  - 2024-11-15-interview-power-user-sarah.md
  - 2024-11-16-interview-new-user-mike.md
  - 2024-11-17-focus-group-session.md
  - 2024-11-18-support-tickets-analysis.md
```

### Step 2: Synthesize

```
"Synthesize all research in @knowledge/transcripts/

Extract:
1. Key insights (patterns across multiple sources)
2. Pain points (frequency + severity)
3. Opportunities (gaps we can fill)
4. User quotes (supporting evidence)
5. Contradictions (where sources disagree)
6. Actionable recommendations

Use @templates/research-synthesis-template.md"
```

### Step 3: What AI Generates

**Synthesis Document** with:

**Key Insights** (3-5 patterns):
- "80% of users mention slow load times on mobile"
- "New users struggle with onboarding step 3"
- "Power users want keyboard shortcuts"

**Pain Points** (prioritized):
1. **Mobile performance** (mentioned 12x, severity: high)
2. **Onboarding confusion** (mentioned 8x, severity: medium)
3. **Missing shortcuts** (mentioned 5x, severity: low)

**Opportunities**:
- Quick win: Add keyboard shortcuts (2 weeks, high satisfaction)
- Strategic: Mobile performance overhaul (8 weeks, retention impact)

**Supporting Quotes**:
- "I almost gave up during onboarding" - Sarah, power user
- "It's so slow on my phone I use desktop" - Mike, new user

**Contradictions**:
- Power users want more features, new users want simplicity
- Need to segment solutions

**Recommendations**:
1. Create initiative for mobile performance (P0)
2. A/B test simplified onboarding (P1)
3. Add keyboard shortcuts (P2, quick win)

### Step 4: Create Initiatives from Synthesis

```
"Based on the research synthesis, create initiatives for:
1. Mobile performance optimization
2. Onboarding simplification
3. Keyboard shortcuts feature

Save to initiatives/ folder with proper opportunity assessments"
```

---

## Part 3: Decision Documentation (10 min)

### Why Document Decisions?

**Problem**: 6 months later, you forget:
- Why did we choose Option A over B?
- What were the tradeoffs?
- What were we trying to achieve?

**Solution**: Document decisions as you make them.

### When to Document

Document decisions when:
- ✅ Multiple options were considered
- ✅ Tradeoffs were made
- ✅ Future you will ask "why?"
- ✅ Team needs alignment
- ✅ Stakeholders need context

### Decision Documentation Workflow

```
"Document this decision:

**Decision**: We're building mobile performance optimization using Option B (refactor approach) instead of Option A (quick fix) or Option C (rebuild).

**Context**: 
- Mobile load times are 3x slower than desktop
- 40% of users are mobile-only
- Retention drops 25% for mobile users

**Options Considered**:
- Option A: Quick fixes (2 weeks, 20% improvement)
- Option B: Refactor core components (8 weeks, 60% improvement)
- Option C: Rebuild mobile stack (16 weeks, 90% improvement)

**Rationale**:
- Option A too small for the problem
- Option C too risky and slow
- Option B balances impact vs. risk
- Can ship incremental improvements during refactor

**Tradeoffs**:
- Giving up: Quick wins (Option A)
- Taking on: 8-week timeline (vs. 2 weeks)
- Risk: Refactor could introduce bugs

**Success Criteria**:
- Mobile load time < 2 seconds (from 6 seconds)
- Mobile retention improves 15%
- Zero critical bugs from refactor

**Date**: 2024-11-20
**Owner**: Product Team
**Stakeholders**: Engineering, Design, Data

Save to knowledge/proposals/2024-11-20-mobile-performance-decision.md"
```

### Using Decision Template

```
"Document this decision using @templates/decision-doc-template.md:

[Paste decision details]"
```

### What You Get

**Decision Record** with:
- Clear decision statement
- Full context (why this came up)
- All options evaluated
- Rationale (why this option)
- Tradeoffs (what we're giving up)
- Success criteria (how we'll know it worked)
- Date and ownership

**Future value**:
- Reference in retrospectives
- Explain to new team members
- Learn from past decisions
- Avoid re-litigating settled questions

---

## Part 4: Complex Multi-Step Workflows (10 min)

### Chaining Workflows

Real PM work isn't one command—it's **sequences**.

### Pattern 1: Research → Initiative → PRD

```
"1. Synthesize research from @knowledge/transcripts/
2. Create initiatives for top 3 opportunities
3. Expand the highest priority initiative
4. Generate PRD from that initiative
5. Create user stories from the PRD"
```

**What happens**:
- AI synthesizes research
- Identifies top opportunities
- Creates 3 initiative files
- Expands the P0 one
- Generates full PRD
- Creates user stories

**Time saved**: 3 hours → 30 minutes

### Pattern 2: Backlog → Prioritize → Roadmap

```
"1. Process @BACKLOG.md into initiatives
2. Prioritize all initiatives using RICE framework
3. Group by quarter based on priority
4. Create roadmap document for next 2 quarters
5. Generate exec summary of roadmap"
```

**What happens**:
- Processes backlog items
- Scores each initiative (Reach × Impact × Confidence / Effort)
- Groups into Q1, Q2, Q3, Q4
- Creates roadmap with timeline
- Generates executive summary

### Pattern 3: Metrics → Analysis → Update → Action

```
"1. Analyze latest metrics from @knowledge/product-analytics/
2. Identify top 3 concerns and opportunities
3. Draft executive update with findings
4. Create action plan for top concern
5. Generate team update with action items"
```

**What happens**:
- Reviews metrics files
- Identifies patterns (drops, spikes, trends)
- Drafts exec update with data
- Creates action plan
- Generates team update

### Pattern 4: Feature Request → Evaluation → Decision

```
"1. Evaluate this feature request: [paste request]
2. Check alignment with @knowledge/product-strategy/
3. Assess effort vs. impact
4. Compare to current roadmap priorities
5. Document recommendation and decision"
```

**What happens**:
- Analyzes feature request
- Checks strategic alignment
- Estimates effort and impact
- Compares to existing priorities
- Documents decision with rationale

### Advanced: Conditional Workflows

```
"If mobile retention is below 70%:
1. Create P0 initiative for retention investigation
2. Synthesize user research on churn
3. Generate action plan
4. Draft exec update on retention risk

If mobile retention is above 70%:
1. Create P1 initiative for growth experiments
2. Generate experiment ideas
3. Prioritize experiments"
```

---

## Putting It All Together

### Real-World Scenario: Feature Launch

**Situation**: You need to launch a new feature in 6 weeks.

**Workflow**:

```
"Help me launch the mobile performance feature:

1. Review current initiative: @initiatives/mobile-performance.md
2. Generate full PRD with launch plan
3. Create user stories and acceptance criteria
4. Draft launch checklist
5. Generate stakeholder communication plan:
   - Exec update (what and why)
   - Engineering brief (technical requirements)
   - Support FAQ (user-facing changes)
   - Marketing brief (positioning)
6. Create success metrics dashboard plan
7. Document go/no-go decision criteria"
```

**What you get**:
- Complete PRD
- User stories
- Launch checklist
- 4 stakeholder communications
- Metrics plan
- Decision framework

**Time**: 30 minutes (vs. 8 hours manually)

---

## Best Practices

### 1. Be Explicit About Steps

❌ "Help me with mobile feature"  
✅ "1. Expand initiative, 2. Generate PRD, 3. Create stories"

### 2. Reference Files Explicitly

❌ "Use the mobile initiative"  
✅ "Use @initiatives/mobile-performance.md"

### 3. Specify Output Format

❌ "Create a roadmap"  
✅ "Create roadmap using @templates/roadmap-template.md"

### 4. Chain Related Work

Instead of:
- Separate command for PRD
- Separate command for stories
- Separate command for launch plan

Do:
- One command that generates all three

### 5. Iterate and Refine

```
"Generate PRD for mobile-performance"
→ "Add more detail on success metrics"
→ "Make technical requirements more specific"
→ "Add competitive analysis section"
```

---

## Common Multi-Step Patterns

### Weekly Planning

```
"1. Review @BACKLOG.md
2. Check @knowledge/product-analytics/ for latest metrics
3. Prioritize work for this week
4. Generate weekly plan document
5. Draft team update"
```

### Feature Evaluation

```
"1. Evaluate feature request: [details]
2. Check @knowledge/product-strategy/ for alignment
3. Assess effort and impact
4. Compare to current roadmap
5. Document recommendation"
```

### Research to Action

```
"1. Synthesize @knowledge/transcripts/
2. Create initiatives for top opportunities
3. Prioritize initiatives
4. Expand top priority
5. Generate PRD"
```

### Launch Preparation

```
"1. Review initiative: @initiatives/[name].md
2. Generate PRD
3. Create launch checklist
4. Draft stakeholder communications
5. Create success metrics plan"
```

---

## Troubleshooting

### "AI skipped a step"

Be explicit:
```
"Step 1: [do this]
Step 2: [do this]
Step 3: [do this]

Don't skip any steps."
```

### "Output format is wrong"

Specify template:
```
"Use @templates/[template-name].md for format"
```

### "Missing context"

Reference files:
```
"Use context from:
- @knowledge/product-strategy/
- @initiatives/[name].md
- @knowledge/briefs-and-specs/[relevant-doc].md"
```

---

## Practice Exercise

### Exercise: End-to-End Feature Launch

**Time**: 30 minutes

**Steps**:
1. Create a new initiative (or use existing one)
2. Expand it with deep research
3. Generate PRD
4. Create user stories
5. Draft launch checklist
6. Generate stakeholder communications
7. Document go/no-go criteria

**Goal**: Experience the full workflow from idea to launch-ready.

---

## Next Steps

### Explore Advanced Workflows

See `examples/workflows/` for specialized workflows:
- `research.md` - Research synthesis patterns
- `decisions.md` - Decision documentation
- `launch.md` - Launch planning
- `planning.md` - Strategic planning
- `communication.md` - Stakeholder updates

### Create Your Own Patterns

Document your common workflows:
```
"Save this workflow pattern to examples/workflows/my-pattern.md:

[Your workflow steps]"
```

### Integrate with MCP

If you have MCP servers configured:
- Fetch real-time metrics
- Pull tickets from Jira/Linear
- Update project management tools
- Automate status updates

---

## Key Takeaways

1. **Chain workflows** - Don't do one thing at a time
2. **Be explicit** - List steps clearly
3. **Reference files** - Use @ mentions
4. **Use templates** - Specify format
5. **Iterate** - Refine outputs
6. **Document decisions** - Future you will thank you
7. **Synthesize research** - Turn data into action

**Advanced workflows save hours** by automating the structured work, so you can focus on strategy and decisions.

---

**You've completed all 5 tutorials!** 🎉

You now know:
- ✅ Setup and basics (Tutorial 1)
- ✅ Initiative workflow (Tutorial 2)
- ✅ Context management (Tutorial 3)
- ✅ Voice training (Tutorial 4)
- ✅ Advanced workflows (Tutorial 5)

**Next**: Start using these patterns in your daily PM work. The more you use them, the better AI gets at helping you.

