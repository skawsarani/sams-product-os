---
allowed-tools: Skill, Read, Write, Glob, WebSearch, WebFetch
argument-hint: [optional: "competitor1, competitor2, ..." or path to competitors.md]
description: Research multiple competitors in parallel and generate comparison matrix
---

## Context

- Today's date: $TODAY
- User arguments: $ARGUMENTS
- Optional inputs:
  - `knowledge/references/competitors.md` (list of competitors)
  - `knowledge/references/product-info.md` (our product for comparison)

## Workflow

Research multiple competitors in parallel and synthesize into a comparison matrix.

**Outputs**:
- Individual reports: `knowledge/references/competitor-[name]-comparison.md`
- Comparison matrix: `knowledge/references/competitor-comparison-matrix-YYYY-MM-DD.md`

### Step 1: Identify Competitors

Check in this order:

1. **File**: Use Glob to check for `knowledge/references/competitors.md` → parse competitor list
2. **Arguments**: Parse `$ARGUMENTS` for comma-separated names/URLs
3. **Prompt**: If neither exists, ask user for competitor list

Also check for `knowledge/references/product-info.md` for comparison context.

### Step 2: Invoke Parallel Research

For EACH competitor, invoke the `competitor-analysis` skill **simultaneously**:

```
Skill(skill="competitor-analysis", args="competitor:[Name] website:[URL if known]")
```

Tell user which skills you're invoking: "I'm using the competitor-analysis skill to analyze [Competitor]"

### Step 3: Monitor & Handle Errors

Track results as they complete:
- ✅ Successful analyses → note report location
- ❌ Failed analyses → continue with others, note in summary

Don't block entire workflow on individual failures.

### Step 4: Aggregate Results

Read all generated reports via Glob (`competitor-*-comparison.md`).

Extract from each:
- Executive summary, features, pricing
- Strengths (top 2-3), weaknesses (top 2-3)
- Target customers, market positioning

Synthesize patterns:
- Common features (all have) vs unique features (only one has)
- Pricing patterns and ranges
- Shared strengths (threats) and common gaps (opportunities)

### Step 5: Generate Comparison Matrix

Use template from `templates/competitor-matrix-template.md` or create with these sections:

1. **Executive Summary** - 3-5 key insights
2. **Feature Comparison Matrix** - Table with ✅/⚠️/❌
3. **Pricing Comparison Matrix** - Tiers and ranges
4. **Target Customer Comparison** - ICP by competitor
5. **Positioning Map** - How competitors differ
6. **Strengths by Competitor** - Top 2-3 each
7. **Weaknesses by Competitor** - With "opportunity for us"
8. **Market Gaps & Opportunities** - Synthesized across all
9. **Competitive Threats** - With severity (High/Med/Low)
10. **Strategic Recommendations** - Immediate, short-term, long-term
11. **Links to Individual Reports**

### Step 6: Present Results

Provide concise summary:
- List of individual reports generated
- Link to comparison matrix
- 3 key insights
- Suggested next steps

## Error Handling

| Scenario | Action |
|----------|--------|
| No competitors.md + no arguments | Prompt user for list |
| No product-info.md | Proceed without "Us" column |
| Some competitor research fails | Continue with successful results |
| All research fails | Report error, suggest checking names/URLs |

## Key Reminders

- **Invoke skills in parallel** - All competitor analyses can run simultaneously
- **Don't block on failures** - Continue with successful results
- **Synthesize, don't just aggregate** - Provide insights, not just combined data
- **Make recommendations actionable** - Suggest what to do, not just describe
- **Note data currency** - Competitive landscapes change; timestamp research
