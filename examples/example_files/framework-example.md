# Framework Example

Example of how to document a PM framework in `knowledge/frameworks/`. This shows the RICE scoring framework as a concrete example.

---

## Example: RICE Scoring Framework

Create `knowledge/frameworks/rice-scoring.md`:

```markdown
# RICE Scoring Framework

## What It Is
Quantitative prioritization using Reach, Impact, Confidence, Effort

## My Scoring Rubric

**Reach** (users per quarter):
- 1-100: Small (score 1)
- 100-1K: Medium (score 2)  
- 1K-10K: Large (score 3)
- 10K+: Massive (score 4)

**Impact** (per user):
- 0.25 = Minimal
- 0.5 = Low
- 1 = Medium
- 2 = High
- 3 = Massive

**Confidence**:
- 50% = Low data
- 80% = Some data
- 100% = Strong data

**Effort** (person-months):
- Actual engineering estimate

## When I Use It
- Prioritizing features within a theme
- Comparing different types of work
- Need quantitative justification

## Example

Mobile performance (from initiative):
- Reach: 20% of users = 2K/quarter = 3
- Impact: High (affects conversion) = 2
- Confidence: 80% (have data)
- Effort: 2 person-months

RICE = (3 × 2 × 0.8) / 2 = 2.4

## Notes
- Don't over-index on score alone
- Use to start conversations
- Combine with strategic alignment
```

---

## Example: Custom Framework

```markdown
# The Three Questions Framework

## What It Is
My personal framework for any decision

## When I Use It
- Feature decisions
- Roadmap prioritization
- Build vs buy
- Partnership opportunities

## How I Apply It

1. **Does this serve our users?**
   - Clear user benefit?
   - Addresses real pain?
   - Would they pay for it?

2. **Does this serve our business?**
   - Revenue impact?
   - Strategic value?
   - Competitive advantage?

3. **Can we do it well?**
   - Technical feasibility?
   - Team capability?
   - Resource availability?

If answer is "no" to any: pause and reconsider.

## Example

**Decision**: Should we build enterprise SSO?

1. Does this serve our users?
   - ✅ Yes - Enterprise customers need SSO for security/compliance
   - ✅ Yes - They explicitly requested it (validated need)
   - ✅ Yes - They would pay for enterprise tier

2. Does this serve our business?
   - ✅ Yes - Unlocks $500K+ ARR enterprise deals
   - ✅ Yes - Strategic move into enterprise market
   - ✅ Yes - Competitive advantage (competitors have it)

3. Can we do it well?
   - ✅ Yes - Engineering estimates 6-8 weeks (feasible)
   - ✅ Yes - Team has experience with auth systems
   - ⚠️ Maybe - Need to confirm engineering capacity

**Decision**: Proceed, but confirm engineering capacity first

## Variations
- Sometimes I add a 4th question: "Is this the right time?" (timing/urgency)
- For smaller decisions, I use just questions 1 and 3

## References
- Inspired by: Jobs-to-be-Done framework
- Related: Value vs Effort matrix

## Related Frameworks
- RICE Scoring (for quantitative comparison)
- Jobs-to-be-Done (for understanding user needs)
```

---

## Framework Documentation Template

Use this structure for any framework:

```markdown
# [Framework Name]

## What It Is
Brief description of the framework

## When I Use It
- Situation 1
- Situation 2

## How I Apply It

### Step 1: [Name]
[Details]

### Step 2: [Name]
[Details]

## Example
[Concrete example from your work]

## Variations
[How you've adapted it]

## References
- [Original source]
- [Useful articles]

## Related Frameworks
- [Other frameworks you combine with this]
```

---

## Tips

- Document what you actually use - not textbook versions
- Include your adaptations - how you've customized it
- Add examples - real cases from your work
- Update as you learn - frameworks evolve
- Link to related docs - connect frameworks to processes

