# Setup Templates

Templates created during Step 4 of the setup skill. Each template is only created if the target file doesn't already exist.

## Template: about-me.md

Target: `knowledge/about-me/about-me.md`

```markdown
# About Me

## Background
[Your PM experience, domain expertise, previous roles]

## Working Style
- Communication preferences: [How you like to communicate]
- Decision-making style: [How you make decisions]
- Tools you use: [Project management, design, analytics tools]

## Product Philosophy
- Core beliefs: [Your product principles]
- Frameworks you use: [RICE, OKRs, Jobs-to-be-Done, etc.]

## Current Context
- Company stage: [Startup, growth, enterprise]
- Team size: [Your team structure]
- This quarter's focus: [Key priorities]

## Strengths
- [Your key strengths as a PM]

## Growth Areas
- [Areas you're working on]

---

**Tip**: Be specific! The more detail you provide, the better AI can tailor its responses to your style and context.
See `templates/about-me-template.md` for more detailed examples.
```

## Template: company-overview.md

Target: `knowledge/company-context/company-overview.md`

```markdown
# Company Overview

## Mission
[Your company mission]

## Products
[What you build, who it's for]

## Target Customers
- [Customer segment 1]: [Description]
- [Customer segment 2]: [Description]

## Team Structure
- Product: [Team size, structure]
- Engineering: [Team size, structure]
- Design: [Team size, structure]

## Current Stage
[Startup, growth, enterprise]

## Key Stakeholders
- [Name, role, what they care about]

---

**Tip**: Keep this updated as your company evolves. This helps AI understand your business context.
```

## Template: current-strategy.md

Target: `knowledge/product-strategy/current-strategy.md`

```markdown
# Product Strategy

## Vision
[Where are you going? What is your product vision?]

## Strategic Pillars
1. **[Pillar 1]**: [Description]
2. **[Pillar 2]**: [Description]
3. **[Pillar 3]**: [Description]

## Current Priorities
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

## Success Metrics
- [Metric 1]: Current X, Target Y
- [Metric 2]: Current X, Target Y

## Key Challenges
- [Challenge 1]
- [Challenge 2]

---

**Tip**: Update this quarterly or when priorities shift. AI uses this to align recommendations with your strategy.
```

## Template: how-we-work.md

Target: `knowledge/processes/how-we-work.md`

```markdown
# How We Work

## Team Process
- Sprint cadence: [Weekly, bi-weekly, etc.]
- Planning process: [How you plan work]
- Review process: [How you review completed work]

## Decision-Making
- How decisions are made: [Process for making product decisions]
- Who makes decisions: [Decision-makers and their roles]
- Escalation process: [When and how to escalate]

## Communication
- Meeting cadence: [Standups, retros, reviews, etc.]
- Communication tools: [Slack, email, etc.]
- Documentation: [Where you document decisions and processes]

## Frameworks We Use
- Prioritization: [RICE, Value vs Effort, etc.]
- Goal-setting: [OKRs, Milestones, etc.]
- Research: [Jobs-to-be-Done, Customer interviews, etc.]

---

**Tip**: Document your actual process, not the ideal. This helps AI understand how to work within your team's constraints.
```

## Template: BACKLOG.md

Target: `BACKLOG.md`

```markdown
# Backlog

Your daily inbox for all notes, ideas, tasks, and thoughts. Capture everything here throughout the day.

Say `process my backlog` when you're ready to categorize and organize items into opportunities, tasks, references, or archive.
```

## Template: GOALS.md

Target: `GOALS.md`

```markdown
# Goals

Define your personal and business goals here. AI will use these to align task priorities and recommendations.

---

## How to Use This File

1. Define 3-5 quarterly goals (too many = unfocused)
2. Update quarterly or when priorities shift
3. AI references this during:
   - Weekly reviews (goal progress tracking)
   - Daily planning (priority alignment)
   - Backlog processing (strategic task categorization)

**Tip**: Make goals specific and measurable. Vague goals get vague results.

---

## Current Quarter Goals

### Goal 1: [Goal Name]

**Description**: [What you want to achieve]

**Why it matters**: [Impact / Strategic alignment]

**Success criteria**:
- [ ] [Measurable milestone 1]
- [ ] [Measurable milestone 2]

**Target date**: [YYYY-MM-DD]

---

### Goal 2: [Goal Name]

**Description**: [What you want to achieve]

**Why it matters**: [Impact / Strategic alignment]

**Success criteria**:
- [ ] [Measurable milestone 1]
- [ ] [Measurable milestone 2]

**Target date**: [YYYY-MM-DD]

---

### Goal 3: [Goal Name]

**Description**: [What you want to achieve]

**Why it matters**: [Impact / Strategic alignment]

**Success criteria**:
- [ ] [Measurable milestone 1]
- [ ] [Measurable milestone 2]

**Target date**: [YYYY-MM-DD]

---

## Archive

Move completed goals here for reference.
```
