# Knowledge Base

This directory stores all your context - the information your AI assistant uses to understand your product, company, and workflows.

**⚠️ This entire directory is gitignored** - your private context stays local.

## Directory Structure

```
knowledge/
├── about-me/             # Personal context, background, working style
├── briefs-and-specs/     # Product specs, feature briefs, technical docs
├── company-context/      # Company info, mission, org structure
├── frameworks/           # PM frameworks, methodologies, mental models
├── notes/                # Archived inbox snapshots, meeting notes, uncategorized items
├── processes/            # How your team works
├── product-analytics/    # KPIs, dashboards, performance data
│   └── interac-metrics/  # Metric definitions and historical data
├── product-strategy/     # Vision, strategy, roadmap
├── proposals/            # Decision docs, RFCs, proposals
├── references/           # Links, articles, competitive analysis
├── transcripts/          # Interview and meeting transcripts
└── voice-samples/        # Personal writing samples for AI voice matching
```

## What to Put Where

### about-me/

**Purpose**: Personal context to help AI understand your background, expertise, and working style.

**Why This Matters**: The more AI knows about you, the better it can:
- Tailor communication to your style
- Reference your experience and expertise
- Understand your priorities and values
- Suggest approaches that fit your context

**Include**:
- **Professional Background**: Current role, years in PM, domain expertise, previous roles, strengths, areas of focus
- **Working Style**: Communication preferences, tools you use, work patterns, decision-making style
- **Product Philosophy**: Core beliefs, frameworks you use, decision-making principles
- **Current Context**: Company stage, team size, product stage, key challenges, this quarter's focus, learning goals

**Example files**:
- `about-me.md`

**See example**: `examples/example_files/about-me-example.md` for a concrete example of what to include.

**Usage**: Reference in conversations for personalized recommendations:
- "Draft this update in my communication style (see @knowledge/about-me/)"
- "Prioritize these features using my usual frameworks (see @knowledge/about-me/)"
- "What would you recommend given my current context? (see @knowledge/about-me/)"

**Tips**:
- Start simple - even a few bullets help
- Update quarterly - keep it current
- Be honest - helps AI give better advice
- Include examples - "I prefer X style (example: ...)"
- Reference other docs - link to your frameworks, processes

**Privacy**: This folder is **gitignored** - your personal context stays private.

---

### briefs-and-specs/

**Purpose**: Store completed product specifications, feature briefs, and technical documentation.

**Include**:
- Product specifications (PRDs)
- Feature briefs
- Technical specs
- Design documents
- Integration docs

**Naming Convention**:
- `spec-[feature-name].md` - Product specifications
- `brief-[project-name].md` - Feature or project briefs
- `YYYY-MM-DD-[name].md` - Dated documents

**Example files**:
- `spec-mobile-app-redesign.md`
- `brief-enterprise-sso.md`
- `2024-12-01-api-v2-spec.md`
- `spec-onboarding-flow.md`

**Usage**: Reference these when:
- Starting similar features
- Understanding past decisions
- Training new team members
- Generating new specs with AI

**Use the template**: `@templates/spec-template.md` or `@templates/brief-template.md`

---

### company-context/

**Purpose**: Help AI understand your company

**Include**:
- Company mission, vision, values
- Product overview
- Target customers and personas
- Organizational structure
- Team information
- Company culture and principles

**Example files**:
- `company-overview.md`
- `product-overview.md`
- `team-structure.md`
- `personas.md`

**Example content**:
```markdown
# Company Overview

## Mission
[Your company mission]

## Products
- Product A: [Description]
- Product B: [Description]

## Target Customers
- Segment 1: [Description]
- Segment 2: [Description]

## Team
- Engineering: [Team size and structure]
- Product: [Team size and structure]
- Design: [Team size and structure]
```

---

### frameworks/

**Purpose**: Document the PM frameworks, methodologies, and mental models you use. This helps AI apply your preferred approaches consistently.

**Why Document Frameworks**: When AI knows your frameworks, it can:
- Apply them automatically to decisions
- Use consistent terminology
- Structure analyses the way you think
- Make recommendations aligned with your methods

**Common PM Frameworks**:

**Prioritization**:
- RICE Scoring (Reach, Impact, Confidence, Effort)
- Value vs Effort Matrix
- ICE Scoring (Impact, Confidence, Ease)

**Strategy**:
- Jobs-to-be-Done
- OKRs
- North Star Framework

**User Research**:
- User Story Mapping
- Opportunity Solution Trees

**Product Development**:
- Agile/Scrum Variations
- Shape Up

**Organization**: Create one file per framework (e.g., `rice-scoring.md`, `jobs-to-be-done.md`)

**See example**: `examples/example_files/framework-example.md` for examples of RICE scoring and custom frameworks.

**Framework Documentation Template**:
- What It Is
- When I Use It
- How I Apply It (step-by-step)
- Example (concrete case from your work)
- Variations (how you've adapted it)
- References (original source, useful articles)
- Related Frameworks

**Usage**: Reference frameworks when asking AI to prioritize or analyze:
- "Prioritize these features using my RICE framework (@knowledge/frameworks/rice-scoring.md)"
- "Analyze this opportunity using my three questions framework"
- "Apply the jobs-to-be-done approach we use"

**Tips**:
- Document what you actually use - not textbook versions
- Include your adaptations - how you've customized it
- Add examples - real cases from your work
- Update as you learn - frameworks evolve
- Link to related docs - connect frameworks to processes

---

### processes/

**Purpose**: Document how your team works

**Include**:
- Development process (Agile, Kanban, etc.)
- Sprint/cycle planning approach
- Decision-making frameworks
- Meeting cadences
- Review processes
- Launch checklists

**Example files**:
- `how-we-work.md`
- `sprint-process.md`
- `decision-making.md`
- `launch-checklist.md`

---

### notes/

**Purpose**: Store archived inbox snapshots, meeting notes, and uncategorized items from backlog processing.

**Include**:
- Daily archived snapshots from `BACKLOG.md` processing (named `YYYY-MM-DD.md`)
- Meeting notes that don't fit into other categories
- Random thoughts and uncategorized items
- Items that were processed but didn't fit into initiatives, tasks, or references

**Naming Convention**:
- `YYYY-MM-DD.md` - Daily archived inbox snapshots
- `YYYY-MM-DD-meeting-[topic].md` - Meeting notes
- `YYYY-MM-DD-notes.md` - General notes

**Example files**:
- `2024-12-02.md` - Archived backlog snapshot
- `2024-12-01-meeting-q4-planning.md` - Meeting notes
- `2024-11-30-notes.md` - General notes

**Usage**: This directory is automatically populated when processing `BACKLOG.md`. Items that don't fit into initiatives, tasks, or references are archived here with a dated snapshot.

---

### product-strategy/

**Purpose**: Keep AI aligned with your strategic direction

**Include**:
- Product vision (2-3 year)
- Strategic priorities
- Quarterly/annual roadmap
- OKRs or goals
- Strategic frameworks you use

**Example files**:
- `product-vision.md`
- `2024-strategy.md`
- `q1-2024-roadmap.md`
- `strategic-pillars.md`

**Why this matters**: When AI helps prioritize, it references your strategy to ensure alignment.

---

### product-analytics/

**Purpose**: Keep AI informed about product performance

**Include**:
- Key metrics definitions
- Current performance data
- Dashboards (screenshots or links)
- Metric trends
- Success criteria for features

**Example files**:
- `key-metrics.md`
- `weekly-metrics-YYYY-MM-DD.md`
- `dashboard-definitions.md`
- `goals-and-targets.md`

**Example content**:
```markdown
# Key Metrics - Week of 2024-01-15

## North Star Metric
**Active Users**: 12,450 (+8% WoW)

## Engagement
- DAU: 3,200 (+5%)
- Session Duration: 8.5 min (+12%)
- Feature Adoption: 23%

## Business
- Conversion Rate: 4.2% (-0.3%)
- MRR: $125K (+3%)
- Churn: 2.1% (↔️)

## Notes
- Conversion rate drop needs investigation
- Session duration improving with new dashboard
```

---

### proposals/

**Purpose**: Track major decisions and proposals

**Include**:
- Decision documents
- RFCs (Request for Comments)
- Feature proposals
- Technical architecture decisions
- Strategic pivots

**Example files**:
- `decision-use-graphql-2024-01.md`
- `proposal-new-pricing-model.md`
- `rfc-mobile-architecture.md`

**Use the template**: `@templates/decision-doc-template.md`

---

### references/

**Purpose**: External information that informs decisions

**Include**:
- Competitive analysis
- Market research
- Industry articles
- Best practices
- Useful links
- Inspiration

**Example files**:
- `competitive-analysis.md`
- `market-trends-2024.md`
- `inspiration-links.md`
- `best-practices.md`

---

### transcripts/

**Purpose**: Store transcripts from user interviews, stakeholder meetings, research sessions, and customer calls.

**Include**:
- User interview transcripts
- Stakeholder meeting notes
- Customer feedback sessions
- Research session recordings (transcribed)
- Product review meetings

**Naming Convention**:
- `YYYY-MM-DD-[type]-[participant].md` - Dated with context
- `interview-[name]-[date].md` - User interviews
- `meeting-[topic]-[date].md` - Meetings

**Example files**:
- `2024-12-01-user-interview-sarah.md`
- `2024-11-28-stakeholder-meeting-q4-planning.md`
- `interview-john-mobile-app-2024-11-20.md`
- `meeting-launch-review-2024-12-15.md`

**Usage**: Reference these when:
- Synthesizing research insights
- Creating opportunity assessments
- Validating assumptions
- Building empathy for users
- Making product decisions

**AI can help synthesize multiple transcripts into insights using `/synthesize` workflow.**

---

### voice-samples/

**Purpose**: Your personal writing samples to help AI match your voice and communication style.

**Why This Matters**: When AI drafts emails, updates, or documents for you, it should sound like *you*, not a generic AI. Voice samples teach AI your patterns.

**What to Include**: Collect 5-10 examples of your real writing across different contexts:

**Professional Writing**:
- Emails to colleagues - Your natural tone with peers
- Emails to executives - How you communicate up
- Slack messages - Casual, quick communication
- Product specs - Technical/formal writing
- Updates/memos - Status communication

**External Writing**:
- LinkedIn posts - Public voice
- Blog posts - Thought leadership
- Customer emails - External communication
- Presentations - Slide content, speaker notes

**How to Collect Samples**:
1. Find your best writing (writing you're proud of, messages that got good responses)
2. Save as markdown files with metadata:
   ```markdown
   # Email to Peer - Project Update
   
   **Context**: Quick status update to team member  
   **Audience**: Engineering lead (peer)  
   **Tone**: Casual, direct  
   **Date**: 2024-11-15
   
   ---
   
   [Your actual email content here]
   ```

**Analyzing Your Voice**: Once you have 5+ samples, ask AI to analyze:
- Sentence structure and length
- How you open and close messages
- Words/phrases you use often
- What you never say
- Tone by audience
- How you structure arguments

**Using the Voice Guide**:
1. Add voice guide to AGENTS.md so it applies to all drafts
2. Reference when drafting: "Draft an exec update using my voice from @knowledge/voice-samples/"
3. Refine over time - update quarterly as your voice evolves

**Context-Specific Voices**: You might write differently by context:
- **To Peers (Casual)**: Incomplete sentences OK, humor welcome, direct, quick to the point
- **To Executives (Concise)**: Data-first, clear ask/decision needed, no unnecessary context, bullet points OK
- **To Customers (Warm)**: Complete sentences, helpful tone, clear next steps, acknowledge their concern
- **Public (Confident)**: Opinionated, hook in first line, short paragraphs, actionable takeaways

**Quick Start**:
1. Collect 5 samples from your recent writing
2. Save here with context metadata
3. Ask AI to analyze: "Analyze my voice from @knowledge/voice-samples/"
4. Add guide to AGENTS.md so it applies to all drafts
5. Test: "Draft [thing] in my voice"
6. Refine: Give feedback on what matches/doesn't

**Privacy**: This folder is **gitignored** - your writing samples stay private.

**See examples**: `examples/voice-samples/` for formatted example files showing proper structure.

---

## Getting Started

### Day 1: Essential Context

Create these minimal files:

1. **About me**:
```bash
touch knowledge/about-me/about-me.md
# Add: Professional background, working style, product philosophy, current context
```

2. **Company context**:
```bash
touch knowledge/company-context/company-overview.md
# Add: Mission, products, target customers
```

3. **Product strategy**:
```bash
touch knowledge/product-strategy/current-strategy.md
# Add: Vision, priorities, current roadmap themes
```

4. **How we work**:
```bash
touch knowledge/processes/how-we-work.md
# Add: Sprint process, meeting cadence, decision process
```

### Week 1: Add More Context

- Current product analytics
- Key personas
- Recent decisions
- Competitive landscape

### Ongoing: Keep Fresh

- Update product analytics weekly
- Add research as you conduct it
- Document decisions as they're made
- Refresh strategy quarterly

## How AI Uses This

When you ask AI questions, it:

1. **Reads relevant context** from knowledge/
2. **Understands your situation** (company, strategy, constraints)
3. **Gives aligned recommendations** based on your strategy
4. **References your data** (metrics, research) in suggestions

### Example Flow

**You**: "What should we prioritize next?"

**AI thinks**:
- Reads `product-strategy/2024-strategy.md` → Sees Q1 focus is mobile
- Reads `product-analytics/latest-metrics.md` → Sees mobile engagement is low
- Reads `transcripts/` → Sees users struggling with mobile UX
- **Recommends**: "Focus on mobile UX improvements" (aligned with strategy + data)

## Best Practices

### 1. Start Small, Build Up

Don't try to document everything at once:
- Week 1: Essentials only
- Week 2-4: Add as you work
- Month 2: Fill gaps
- Ongoing: Maintain

### 2. Keep It Current

Old information misleads AI:
- Archive outdated strategy docs
- Update product analytics regularly
- Mark docs with "Last Updated" dates
- Delete stale references

### 3. Use Consistent Naming

```bash
# Good
product-strategy/2024-q1-strategy.md
product-analytics/weekly-2024-01-15.md
briefs-and-specs/spec-mobile-redesign.md
transcripts/2024-12-01-user-interview-sarah.md

# Confusing
stuff.md
notes-v2-final-FINAL.md
untitled.md
```

### 4. Link Related Docs

In your docs, reference related files:
```markdown
Related:
- [Decision to prioritize mobile](../proposals/decision-mobile-first.md)
- [Mobile user research](../transcripts/mobile-usability-study.md)
```

### 5. Make It Scannable

AI reads like a human - help it find key info:
- Use clear headers
- Bullet points over paragraphs
- Tables for comparisons
- Bold key points

## Maintenance

### Weekly

- [ ] Update product analytics
- [ ] Add new research (transcripts, briefs)
- [ ] Document any decisions

### Monthly

- [ ] Review and archive old docs
- [ ] Update strategy docs if changed
- [ ] Clean up duplicate content
- [ ] Check for outdated info

### Quarterly

- [ ] Refresh product strategy
- [ ] Update roadmap
- [ ] Review all docs for accuracy
- [ ] Add missing context

## Privacy & Security

### What to Store Here

✅ **Safe**:
- Product strategy
- User research (anonymized)
- Process documentation
- Public competitive info
- Metrics (no PII)

### What NOT to Store

❌ **Don't include**:
- Passwords or API keys
- Customer PII (names, emails, etc.)
- Financial details (revenue, salaries)
- Confidential business data
- Trade secrets

**Use** `.env` files (gitignored) for secrets.

### Sharing with Team

If you want to share some context:
1. Create a separate repo/folder for shared context
2. Keep personal context local
3. Be mindful of sensitive information

## Troubleshooting

### AI Doesn't Use Context

**Problem**: AI seems unaware of your context

**Solutions**:
- Reference files explicitly: `@knowledge/product-strategy/2024-strategy.md`
- Check files exist (not empty)
- Make sure content is clear and organized
- Add more specific context

### Too Much Information

**Problem**: Knowledge base is overwhelming

**Solutions**:
- Archive old docs
- Create summaries for long docs
- Link to external docs instead of copying
- Focus on what's actively relevant

### Context Conflicts

**Problem**: Docs contradict each other

**Solutions**:
- Keep one source of truth for each topic
- Archive outdated versions
- Use "Last Updated" dates
- Link related docs with "supersedes" notes

---

## Remember

This is **your** knowledge base. Organize it however makes sense for you. The structure provided is a starting point - adapt it to your needs!

The more context you provide, the better AI can:
- Align with your strategy
- Make informed recommendations
- Generate relevant artifacts
- Save you time

