# Tutorial 3: Memory & Context Management

**Time**: 25 minutes  
**Goal**: Teach your AI agent about your context so it provides personalized, relevant help

---

## The Problem

AI agents don't remember between sessions. Each conversation starts fresh. But great product work requires context:
- Your company's strategy
- Your personal working style
- Your frameworks and processes
- Your current priorities

**PM Co-Pilot solves this with structured context files that AI reads automatically.**

---

## The Context Stack

```
┌──────────────────────────────────────┐
│  AGENTS.md (System Instructions)     │  ← AI reads this first
├──────────────────────────────────────┤
│  knowledge/about-me/ (Your Context)  │  ← Your style, preferences
├──────────────────────────────────────┤
│  knowledge/product-strategy/         │  ← Strategic direction
├──────────────────────────────────────┤
│  knowledge/frameworks/               │  ← Your methods
├──────────────────────────────────────┤
│  initiatives/ (Active Work)          │  ← Current state
└──────────────────────────────────────┘
```

---

## Part 1: Personal Context (10 min)

### Step 1: Create Your Profile

Create `knowledge/about-me/about-me.md`:

```markdown
# About Me

## Professional Background
- **Current Role**: Senior PM at TechCorp
- **Experience**: 6 years in B2B SaaS
- **Previous**: Software engineer → PM
- **Domain**: Enterprise productivity tools

## Working Style
- **Decision-making**: Data-driven with intuition overlay
- **Communication**: Prefer concise bullets over long paragraphs
- **Planning**: Weekly deep planning sessions, daily quick checks
- **Collaboration**: Highly collaborative, seek input before deciding

## Strengths
- Technical depth (former engineer)
- User research and synthesis
- Cross-functional alignment
- Quantitative analysis

## Growth Areas
- Enterprise sales cycles (learning)
- Executive stakeholder management
- Public speaking/presentations

## Current Context
- **Company Stage**: Series B, 80 employees
- **Team**: 3 PMs, 15 engineers, 2 designers
- **Product Stage**: Product-market fit achieved, scaling phase
- **This Quarter**: Focus on enterprise features, reduce churn
```

### Step 2: Document Your Frameworks

Create `knowledge/frameworks/my-prioritization.md`:

```markdown
# My Prioritization Framework

## Primary: RICE Scoring

**Formula**: (Reach × Impact × Confidence) / Effort

### My Scoring Rubric

**Reach** (users per quarter):
- 1: <100 users
- 2: 100-1K users
- 3: 1K-10K users
- 4: 10K+ users

**Impact** (per user):
- 0.25: Minimal
- 0.5: Low
- 1.0: Medium
- 2.0: High
- 3.0: Massive

**Confidence**:
- 50%: Hypothesis only
- 80%: Some data/research
- 100%: Strong evidence

**Effort**: Engineering person-months

### When I Use It
- Comparing features within a theme
- Need quantitative justification
- Stakeholder discussions

### When I Don't
- Strategic initiatives (can't quantify easily)
- Technical debt (use impact/urgency matrix)
- Quick wins (<1 week effort)
```

### Step 3: Add Product Strategy

Create `knowledge/product-strategy/2024-strategy.md`:

```markdown
# 2024 Product Strategy

## North Star Metric
**Weekly Active Teams** (currently 2,400)

## Strategic Pillars

### 1. Enterprise Readiness (40% of capacity)
- SSO, RBAC, audit logs
- Advanced security features
- White-label options

### 2. Core Product Excellence (35%)
- Performance optimization
- Mobile experience
- Core workflow improvements

### 3. Platform & Ecosystem (15%)
- API expansion
- Integration marketplace
- Developer tools

### 4. Expansion & Retention (10%)
- Upsell features
- User onboarding improvements
- Churn reduction

## Key Metrics
- WAT (Weekly Active Teams): 2,400 → 5,000
- Enterprise ARR: $2M → $8M
- Net Revenue Retention: 105% → 120%
- NPS: 42 → 55
```

---

## Part 2: How AI Uses Context (5 min)

### Automatic Context Loading

When you ask AI to help, it automatically references your context:

**Example 1: Prioritization**
```
You: "Should we prioritize mobile performance or dashboard redesign?"

AI thinks:
1. Reads your RICE framework from knowledge/frameworks/
2. Checks product strategy - sees "Core Product Excellence" pillar
3. Checks about-me/ - sees you're data-driven
4. Applies RICE to both options
5. Recommends based on scores + strategic fit
```

**Example 2: Communication Style**
```
You: "Draft an update for my VP"

AI thinks:
1. Reads knowledge/about-me/ - sees "concise bullets" preference
2. Checks your voice samples (if available)
3. Reads knowledge/product-analytics/ for latest metrics
4. Drafts in your style: data-first, bullets, clear ask
```

---

## Part 3: Testing Your Context (10 min)

### Test 1: Prioritization

```
"I have two initiatives:
1. Mobile performance optimization
2. Dashboard redesign

Help me prioritize using my framework and strategy.
Check @knowledge/frameworks/ and @knowledge/product-strategy/"
```

**What to look for**:
- ✅ AI applies your RICE scoring
- ✅ References strategic pillars
- ✅ Shows the math
- ✅ Gives clear recommendation

### Test 2: Style Matching

```
"Draft a quick Slack message to my team about pushing the launch date by one week.
Use my communication style from @knowledge/about-me/"
```

**What to look for**:
- ✅ Matches your formality level
- ✅ Uses your typical structure
- ✅ Avoids phrases you don't use
- ✅ Feels like you wrote it

### Test 3: Strategic Alignment

```
"Create an initiative for adding real-time collaboration features.
Check if it aligns with our strategy in @knowledge/product-strategy/"
```

**What to look for**:
- ✅ AI checks strategic pillars
- ✅ Notes which pillar this fits (or doesn't)
- ✅ Flags if it's off-strategy
- ✅ Suggests alternatives if misaligned

---

## Part 4: Context Maintenance

### Weekly: Update Active Context

```
knowledge/about-me/this-week.md
```

```markdown
# This Week's Context

**Week of**: Dec 2-8, 2024

## Top Priority
Shipping Q4 mobile release by Friday

## Blocked/Paused
- Dashboard redesign (waiting on design review)
- API v2 (engineering capacity)

## Key Meetings
- Thursday: Board update preparation
- Friday: Q4 release decision

## Avoid This Week
- No new commitments until launch
- Defer all P2/P3 discussions
```

### Monthly: Review Frameworks

```
"Read @knowledge/frameworks/ and check if my approaches have evolved.
What patterns have changed in my recent initiatives?"
```

### Quarterly: Refresh Strategy

```
"Review @knowledge/product-strategy/ against our progress.
What's changed? What needs updating?"
```

---

## Best Practices

### 1. Be Specific in Context

❌ "I like data-driven decisions"  
✅ "I need 80%+ confidence in RICE scoring before committing to build"

### 2. Include Examples

```markdown
## Communication Style

**Email to executives**:
- Subject line has the ask
- First line states recommendation
- Data in bullets
- Clear decision needed

Example: [paste actual email]
```

### 3. Link Related Context

```markdown
See also:
- @knowledge/frameworks/rice-scoring.md for how I prioritize
- @knowledge/about-me/about-me.md for my background
- @knowledge/product-strategy/2024-strategy.md for strategic alignment
```

### 4. Keep It Current

Set reminders:
- **Weekly**: Update this-week.md
- **Monthly**: Review frameworks
- **Quarterly**: Refresh strategy docs

---

## Common Issues

**"AI isn't using my context"**
- Check file paths: Use @knowledge/... to reference
- Be explicit: "Use my RICE framework from @knowledge/frameworks/"
- Test: Ask AI to summarize your context files

**"Priorities seem random"**
- Ensure product-strategy/ has clear priorities
- Add decision criteria to frameworks/
- Include "why" for each strategic pillar

**"AI uses generic language"**
- Add voice samples (see Tutorial 4)
- Be specific about phrase preferences in about-me/
- Give feedback: "I wouldn't say X, I'd say Y"

---

## Quick Wins

Start with these 3 files:

1. **knowledge/about-me/about-me.md** (5 min)
   - Role, experience, strengths
   - Working style basics
   - Current priorities

2. **knowledge/product-strategy/current-strategy.md** (10 min)
   - Top 3 strategic priorities
   - Key metrics you track
   - What's in/out of scope

3. **knowledge/frameworks/prioritization.md** (5 min)
   - Your go-to prioritization method
   - When you use it
   - Example scoring

**Total time**: 20 minutes for massive context improvement

---

## Next Steps

- **Tutorial 4**: Voice Training (make AI write like you)
- **Tutorial 5**: Advanced Workflows (initiative expansion, research synthesis)

---

**Key Takeaway**: Context = Quality. The more AI knows about your situation, preferences, and methods, the better its recommendations and drafts will be.

