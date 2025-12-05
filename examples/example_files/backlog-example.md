# Backlog Example

Example of how to use BACKLOG.md for capturing raw ideas.

---

## How It Works

1. **Brain dump** - Add ideas, requests, bugs, tasks, notes, references - everything goes here
2. **Process daily/weekly** - Say: `"process my backlog"` or `/backlog`
3. **AI categorizes** - Items become:
   - **Initiatives** → `initiatives/` folder (opportunity assessments)
   - **Tasks** → `tasks/` folder (actionable items)
   - **References** → `knowledge/references/` (useful info)
   - **Uncategorized** → Archived in `knowledge/notes/YYYY-MM-DD.md` (meeting notes, random thoughts)
4. **Review** - Adjust priorities and add details

---

## Example Entries

### Initiatives (Strategic Work)

#### Mobile App Performance Issues
- **Source**: Customer support (15 tickets this week)
- **Context**: App crashes on Android 12, checkout flow timing out
- **Why now**: Affecting 20% of mobile users, impacting conversion

#### Enterprise SSO Request  
- **Source**: Acme Corp (potential $500K deal)
- **Context**: They need SAML SSO for 500+ users
- **Why now**: Blocker for Q1 expansion deal

#### Dashboard Redesign
- **Source**: User research, internal feedback
- **Context**: Current dashboard is cluttered, low engagement (15% DAU)
- **Why now**: Competitor X launched cleaner version, losing mindshare

### Tasks (Actionable Items)

#### Follow up with Sarah about Q4 goals
- Need to align on OKRs for next quarter
- Due: End of week

#### Update metrics dashboard
- Add new conversion funnel visualization
- Reference: analytics team request

#### Email design team about dark mode mockups
- They said they'd have something by Friday

### References (Useful Info)

#### Competitor X launched feature Y
- Link: [article URL]
- Notes: They're using AI-powered recommendations, we should evaluate

#### Article about PM frameworks
- Link: [article URL]
- Notes: Good framework for prioritization, might adapt for our team

### Uncategorized (Meeting Notes, Random Thoughts)

#### Meeting with engineering lead
- Discussed API rate limiting concerns
- They mentioned seeing abuse patterns
- Need to follow up on infrastructure costs

#### Random thought: What if we added a mobile app?
- Not sure if this is strategic yet
- Need to research market first

---

## Tips for Capturing

### Good Captures
✅ Include **source** (customer, team, data)  
✅ Add **context** (what's happening)  
✅ Note **urgency** (why now matters)  
✅ Keep it **brief** (details come later)

### Less Useful
❌ Just titles without context  
❌ Solutions instead of problems  
❌ Already-processed ideas  
❌ Too much detail (save for initiatives)

---

## Format Options

### Minimal (Fastest)
```
- Add dark mode
- Fix mobile checkout bug
- Enterprise SSO for Acme deal
```

### Structured (Recommended)
```
## Feature Name
- Source: Who/where it came from
- Context: Brief description
- Why now: Urgency or timing
```

### Voice Note Style
```
## Meeting with Sarah - Enterprise Features
Customer wants SSO, RBAC, audit logs. Deal is $500K ARR. 
Timeline: Need decision by end of Q1. Competitor offers this.
Engineering says 6-8 weeks for SSO, rest can wait.
```

---

## What Happens When You Process

**Input** (in BACKLOG.md):
```
## Enterprise SSO Request
- Source: Acme Corp 
- Context: Need SAML for 500 users
- Why now: $500K deal blocker
```

**Output** (AI creates `initiatives/enterprise-sso.md`):
```markdown
# Initiative: Enterprise SSO

**Priority**: P0
**Status**: Evaluating
**Owner**: [TBD]
**Created**: 2024-12-02

## Objective
Enable enterprise customers to use their identity providers 
for authentication, removing security barrier to large deals.

## Target Customer
Enterprise customers (500+ users) with security/compliance 
requirements for centralized identity management.

## Success Metrics
- Close Acme Corp deal ($500K ARR)
- Enable 3+ enterprise deals in Q1
- Reduce sales cycle time for enterprise by 30%

## What We Know
- Acme Corp needs SAML SSO for 500 users
- This is a common blocker for enterprise deals
- Engineering estimates 6-8 weeks
- Competitors offer this as standard

## What We Should Research
- Which identity providers to support (Okta, Azure AD, etc.)
- Security/compliance requirements
- User provisioning needs (SCIM)
- Pricing implications

## Solution Ideas
1. SAML SSO with Okta, Azure AD support
2. User provisioning (SCIM)
3. Just-in-time provisioning
4. SSO + RBAC together

## Risks
- Engineering capacity (6-8 weeks)
- Ongoing maintenance cost
- Security vulnerabilities if not done right
- Scope creep to RBAC, audit logs

## Questions to Validate
- Will Acme proceed with just SSO or need RBAC?
- Are other deals waiting on this?
- Can we charge premium for enterprise tier?
- What's our support model?
```

---

## Maintenance

- **Process weekly** - Keep backlog clean
- **Archive quarterly** - Move to `archive/backlog-archive-YYYY-QN.md`
- **Delete duplicates** - AI will flag them during processing
- **Update context** - Add new info to existing items before processing

---

## Common Patterns

### Feature Requests
```
## [Feature Name]
- Source: User feedback, sales, etc.
- Context: What users want to do
- Why now: Business impact or urgency
```

### Bugs
```
## [Bug Description]
- Source: Support tickets, monitoring
- Context: What's broken, impact
- Why now: Severity, user count affected
```

### Technical Debt
```
## [Tech Debt Item]
- Source: Engineering team
- Context: What needs refactoring
- Why now: Cost, risk, or blocking new work
```

### Strategic Ideas
```
## [Initiative Name]
- Source: Strategy meeting, market research
- Context: Opportunity or competitive move
- Why now: Market timing, resources available
```

---

**Remember**: BACKLOG.md is your inbox. Don't overthink it - just capture and process later!

