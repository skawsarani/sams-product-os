---
allowed-tools: Skill, Read, Write, Glob, WebSearch, WebFetch
argument-hint: [optional: "competitor1, competitor2, ..." or path to competitors.md]
description: Research multiple competitors in parallel and generate comparison matrix
---

# Competitor Research Workflow

Research multiple competitors simultaneously and synthesize findings into a comprehensive comparison matrix.

## Context

- Today's date: 2026-01-11
- User arguments: $ARGUMENTS
- Optional input files:
  - `knowledge/references/competitors.md` (list of competitors to track)
  - `knowledge/references/product-info.md` (our product for comparison)

---

## Your Task

Orchestrate parallel competitive research across multiple competitors and create a comparison matrix that synthesizes all findings.

**Output**:
- Individual reports: `knowledge/references/competitor-[name]-comparison.md` (one per competitor)
- Comparison matrix: `knowledge/references/competitor-comparison-matrix-YYYY-MM-DD.md`

---

## Step 1: Identify Competitors

Discover which competitors to research using this priority order:

### Mode A: Check for competitors.md File

Use `Glob` to check if `knowledge/references/competitors.md` exists:

```
Glob(pattern="competitors.md", path="knowledge/references/")
```

**If found**: Use `Read` to load the file and parse the competitor list.

**Expected format**:
```markdown
# Competitors to Track

- Stripe (stripe.com) - Payment processing
- Square (squareup.com) - Payment + POS
- PayPal (paypal.com) - Payment processing
```

Extract:
- Competitor names
- Website URLs
- Optional descriptions

### Mode B: Check for Arguments

If competitors.md doesn't exist, check `$ARGUMENTS` for competitor list.

**Accepted formats**:
- Comma-separated names: `Stripe, Square, PayPal`
- Comma-separated URLs: `stripe.com, square.com, paypal.com`
- Mixed: `Stripe (stripe.com), Square, paypal.com`

Parse arguments to extract:
- Competitor names
- Website URLs (if provided, otherwise will be discovered by skill)

### Mode C: Prompt User

If neither file nor arguments exist, ask user:

> "Which competitors would you like me to research? Please provide:
> - Competitor names (I'll find their websites)
> - Or competitor names with websites (e.g., 'Stripe (stripe.com), Square (squareup.com)')
> - Or a path to a competitors.md file"

### Check for product-info.md (Optional)

Use `Glob` to check if `knowledge/references/product-info.md` exists:

```
Glob(pattern="product-info.md", path="knowledge/references/")
```

**If found**: Use `Read` to load our product context.
- This will be passed to each competitive-research skill invocation
- Enables comparison columns in individual reports

**If not found**: Proceed without product comparison context.

---

## Step 2: Invoke Parallel Competitive Research

For EACH competitor identified, invoke the `competitive-research` skill in parallel.

**Important**: Invoke ALL skills in a single message (parallel execution).

### Invocation Pattern

For each competitor, use the Skill tool:

```
Skill(
  skill="competitive-research",
  args="competitor:[Name] website:[URL if known] product_context:[from product-info.md if exists]"
)
```

**Example with 3 competitors**:
```
I'm using the competitive-research skill to analyze Stripe
I'm using the competitive-research skill to analyze Square
I'm using the competitive-research skill to analyze PayPal
```

Then invoke all three skills simultaneously:
```
Skill(skill="competitive-research", args="competitor:Stripe website:stripe.com")
Skill(skill="competitive-research", args="competitor:Square website:squareup.com")
Skill(skill="competitive-research", args="competitor:PayPal website:paypal.com")
```

**Note**: Each skill invocation is independent. They can run in parallel.

---

## Step 3: Monitor Completion & Handle Errors

Wait for all competitive-research skill invocations to complete.

**Track results**:
- Which competitors completed successfully
- Which failed (if any)
- Where reports were saved

**Error handling**:
- If a competitor research fails: Note which failed, continue with successful results
- If all fail: Report error to user, suggest troubleshooting (check competitor names, URLs)
- Don't block entire workflow on individual failures

**Example output during monitoring**:
```
✅ Stripe analysis complete → knowledge/references/competitor-stripe-comparison.md
✅ Square analysis complete → knowledge/references/competitor-square-comparison.md
❌ PayPal analysis failed (website not found)
✅ Adyen analysis complete → knowledge/references/competitor-adyen-comparison.md
```

---

## Step 4: Aggregate Results

After all (or most) competitor analyses complete, read the individual reports to extract data for the comparison matrix.

### Read All Generated Reports

Use `Glob` to find all competitor reports:
```
Glob(pattern="competitor-*-comparison.md", path="knowledge/references/")
```

Use `Read` to load each report and extract:

**From each report, extract**:
1. **Executive summary** (key takeaways)
2. **Product features** (from Feature Comparison table)
3. **Pricing** (from Pricing Tiers table)
4. **Strengths** (top 2-3)
5. **Weaknesses** (top 2-3)
6. **Target customers** (ICP)
7. **Market positioning** (tagline, value prop)

### Synthesize Cross-Competitor Insights

Analyze patterns across all competitors:
- **Common features**: What features do ALL competitors have?
- **Unique features**: What does only ONE competitor have?
- **Pricing patterns**: Range, typical tiers, value metrics
- **Shared strengths**: What are competitors good at (threats)?
- **Common gaps**: What do ALL competitors lack (opportunities)?
- **Market positioning clusters**: Are they all positioned similarly or differently?

---

## Step 5: Generate Comparison Matrix

Create a comprehensive comparison document that synthesizes all individual reports.

### Matrix Structure

**Filename**: `knowledge/references/competitor-comparison-matrix-2026-01-11.md`

**Sections**:

1. **Executive Summary** (3-5 key insights)
   - Top insight from synthesizing all reports
   - Major market gaps identified
   - Primary threats identified
   - Strategic recommendations

2. **Feature Comparison Matrix**
   - Table format with competitors as columns
   - Feature categories as rows
   - Use ✅/⚠️/❌ for quick scanning
   - Include "Us" column if product-info.md exists

3. **Pricing Comparison Matrix**
   - Table with pricing tiers as rows
   - Competitors as columns
   - Note patterns (all offer annual discounts, etc.)

4. **Target Customer Comparison**
   - Table showing each competitor's ICP
   - Company size, industry, use cases

5. **Positioning Map**
   - Text-based or simple ASCII positioning
   - Show how competitors differ in positioning

6. **Competitive Strengths** (by competitor)
   - Bulleted list of top 2-3 strengths per competitor

7. **Competitive Weaknesses** (by competitor)
   - Bulleted list of top 2-3 weaknesses per competitor
   - Include "Opportunity for us" for each

8. **Market Gaps & Opportunities**
   - Synthesized gaps across ALL competitors
   - Strategic opportunities to exploit

9. **Competitive Threats**
   - Aggregated threats from competitor strengths
   - Severity assessment (High/Medium/Low)

10. **Strategic Recommendations**
    - Immediate actions (0-3 months)
    - Short-term strategy (3-6 months)
    - Long-term positioning (6-12 months)

11. **Links to Individual Reports**
    - Markdown links to each competitor's full report

12. **Aggregated Sources**
    - Count of total sources used
    - Breakdown by type (web, Notion, knowledge base)

### Matrix Template Format

```markdown
# Competitive Landscape Analysis

**Date**: 2026-01-11
**Competitors Analyzed**: [List]
**Our Product**: [Name if product-info.md exists, otherwise "Not specified"]

---

## Executive Summary

**Key Insight 1**: [Major finding across all competitors]

**Key Insight 2**: [Market gap or opportunity identified]

**Key Insight 3**: [Primary threat identified]

**Key Insight 4**: [Strategic recommendation]

---

## Feature Comparison Matrix

| Feature | Us | [Competitor 1] | [Competitor 2] | [Competitor 3] |
|---------|----|----|----|----|
| [Feature 1] | [✅/⚠️/❌] | [✅/⚠️/❌] | [✅/⚠️/❌] | [✅/⚠️/❌] |
| [Feature 2] | [✅/⚠️/❌] | [✅/⚠️/❌] | [✅/⚠️/❌] | [✅/⚠️/❌] |

**Legend**: ✅ Full support | ⚠️ Partial/Limited | ❌ Not available

**Insights**:
- **Common features**: [Features all competitors have]
- **Unique capabilities**: [Features only 1 competitor has]
- **Market gaps**: [Features NO competitors have well]

---

## Pricing Comparison Matrix

| Tier | [Competitor 1] | [Competitor 2] | [Competitor 3] |
|------|-----|-----|-----|
| **Entry/Free** | [Price/Terms] | [Price/Terms] | [Price/Terms] |
| **Mid-Tier** | [Price/Terms] | [Price/Terms] | [Price/Terms] |
| **Enterprise** | [Price/Terms] | [Price/Terms] | [Price/Terms] |

**Pricing Insights**:
- **Range**: Entry tier ranges from $X to $Y
- **Common patterns**: [e.g., "All offer annual discounts around 20%"]
- **Value metrics**: [e.g., "Mix of per-user and transaction-based"]
- **Our positioning**: [If product-info.md exists]

---

## Target Customer Comparison

| Competitor | Primary Target | Company Size | Industry Focus |
|------------|---------------|--------------|----------------|
| [Competitor 1] | [Persona] | [SMB/MM/ENT] | [Industries] |
| [Competitor 2] | [Persona] | [SMB/MM/ENT] | [Industries] |
| Us | [If known] | [If known] | [If known] |

---

## Positioning Map

[Text-based positioning visualization]

**High-Touch / Enterprise**
```
                [Competitor 4]
                     |
  [Competitor 1]    Us?    [Competitor 3]
                     |
                [Competitor 2]
```
**Self-Service / SMB**

**Positioning Analysis**:
- **[Competitor 1]**: [How they position - their tagline]
- **[Competitor 2]**: [How they position]
- **Us**: [Our positioning if known]

---

## Competitive Strengths (by Competitor)

### [Competitor 1]
- [Strength 1]
- [Strength 2]

### [Competitor 2]
- [Strength 1]
- [Strength 2]

**Cross-Competitor Threat Assessment**:
- **Major threat**: [Aggregated primary threat]
- **Emerging threat**: [Pattern identified]

---

## Competitive Weaknesses (by Competitor)

### [Competitor 1]
- [Weakness 1] → **Our opportunity**: [How we capitalize]
- [Weakness 2] → **Our opportunity**: [How we capitalize]

### [Competitor 2]
- [Weakness 1] → **Our opportunity**: [How we capitalize]

**Cross-Competitor Gap Assessment**:
- **Common weakness**: [What ALL competitors struggle with]
- **Opportunity**: [How we can differentiate here]

---

## Market Gaps & Opportunities

### Unmet Customer Needs
1. **[Gap 1]**: [Description]
   - **Evidence**: [From multiple competitor analyses]
   - **Opportunity**: [How we could fill this]

2. **[Gap 2]**: [Description]
   - **Evidence**: [From analyses]
   - **Opportunity**: [How we could fill this]

### Differentiation Angles
- [Angle 1]: [Based on common competitor weaknesses]
- [Angle 2]: [Based on market gaps]

---

## Competitive Threats

### Immediate Threats
1. **[Threat 1]**: [Competitor + their advantage]
   - **Impact on us**: [How this threatens our position]
   - **Severity**: High / Medium / Low
   - **Mitigation**: [Recommended response]

2. **[Threat 2]**: [Competitor + their advantage]
   - **Impact on us**: [How this threatens our position]
   - **Severity**: High / Medium / Low
   - **Mitigation**: [Recommended response]

---

## Strategic Recommendations

### Immediate (0-3 months)
1. [Action based on competitive intelligence]
2. [Action based on identified threats]

### Short-term (3-6 months)
1. [Strategic move based on market gaps]
2. [Feature/positioning recommendation]

### Long-term (6-12 months)
1. [Strategic initiative based on landscape analysis]

---

## Individual Competitor Reports

For detailed analysis of each competitor:
- [Competitor 1 - competitor-stripe-comparison.md](competitor-stripe-comparison.md)
- [Competitor 2 - competitor-square-comparison.md](competitor-square-comparison.md)
- [Competitor 3 - competitor-paypal-comparison.md](competitor-paypal-comparison.md)

---

## Next Steps

- [ ] Review comparison matrix with product team
- [ ] Update product roadmap based on identified gaps
- [ ] Consider creating product positioning strategy (use product-strategy skill when available)
- [ ] Schedule follow-up research in 3-6 months to track changes

---

## Research Metadata

**Research Date**: 2026-01-11
**Competitors Analyzed**: [N] competitors
**Individual Reports Generated**: [N] reports
**Data Sources Used**:
- Web sources: [N]
- Notion pages: [N if applicable]
- Knowledge base files: [N if applicable]
- User-provided: [N if applicable]

**Next Research Recommended**: [Date 3-6 months from now]
```

---

## Step 6: Present Results to User

After generating the comparison matrix, provide a concise summary:

### Summary Format

```
✅ Completed competitive research for [N] competitors

**Individual Reports**:
- knowledge/references/competitor-stripe-comparison.md
- knowledge/references/competitor-square-comparison.md
- knowledge/references/competitor-paypal-comparison.md

**Comparison Matrix**:
- knowledge/references/competitor-comparison-matrix-2026-01-11.md

**Key Insights**:
1. [Top strategic insight from matrix]
2. [Major opportunity identified]
3. [Primary threat to monitor]

**Next Steps**:
- Review comparison matrix for strategic planning
- Consider updating product roadmap based on identified gaps
- Schedule re-research in 3-6 months to track landscape changes
```

---

## Error Handling

### If competitors.md Not Found and No Arguments
→ Prompt user for competitor list
→ Don't fail - just ask

### If Product-info.md Not Found
→ Proceed without product comparison
→ Note in matrix: "Our product context not available for comparison"

### If Skill Invocation Fails for Some Competitors
→ Continue with successful results
→ Note failures in summary: "Note: Research for [Competitor X] could not be completed"
→ Still generate comparison matrix with available data

### If No Competitors Successfully Researched
→ Report error to user
→ Suggest: Check competitor names/URLs, try again with specific websites
→ Don't generate empty comparison matrix

### If WebSearch Unavailable
→ Competitive-research skill will handle this gracefully
→ May result in less comprehensive reports
→ Note in summary: "Note: Some web sources unavailable"

---

## Best Practices

1. **Always tell user which skill you're using**: "I'm using the competitive-research skill to analyze [Competitor]"

2. **Invoke skills in parallel**: All competitor analyses can run simultaneously - invoke them in the same message

3. **Don't block on failures**: If one competitor research fails, continue with others

4. **Synthesize, don't just aggregate**: The comparison matrix should provide insights, not just combine reports

5. **Link to individual reports**: Matrix is high-level; link to detailed reports for deep dives

6. **Make recommendations actionable**: Don't just describe the landscape - suggest what to do about it

7. **Note data currency**: Competitive landscapes change - note when research was done

---

## Integration Points

**With competitive-research skill**:
- This workflow invokes that skill multiple times in parallel
- Each invocation analyzes one competitor
- This workflow then synthesizes the results

**With product-strategy skill** (when available):
- Strategy documents can reference the comparison matrix
- Use comparison matrix as input for positioning strategy

**With BACKLOG.md**:
- User may add "Research [Competitor]" to backlog
- `/process-backlog` can extract this and suggest `/competitor-research [Competitor]`
