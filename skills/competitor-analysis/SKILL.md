---
name: competitor-analysis
description: Comprehensively analyze a single competitor including features, pricing, target customers, strengths, gaps, testimonials, and market positioning. Use when asked to "research [competitor]", "analyze [competitor]", "compare us to [competitor]", or "what does [competitor] offer". Pulls from web search, Notion workspace, and knowledge base files. Outputs structured competitor analysis report.
---

# Competitor Analysis Skill

Perform comprehensive competitive analysis of a single competitor, gathering intelligence from multiple sources to create a structured research report.

## Overview

This skill analyzes ONE competitor at a time. For analyzing multiple competitors in parallel, use the `/competitor-research` workflow instead.

**Output**: Structured markdown report saved to `knowledge/references/competitor-[NAME]-comparison.md`

**Data sources** (in priority order):
1. Knowledge base files (knowledge/references/, knowledge/transcripts/)
2. Notion workspace (if MCP available)
3. Web search (pricing pages, reviews, testimonials)
4. User-provided sources

---

## Workflow

### Step 1: Understand the Request

Gather essential information:

**Required**:
- Competitor name
- Website URL (or prompt user if not provided)

**Optional**:
- Our product context from `knowledge/references/product-info.md` (for comparison)
- Specific focus areas (e.g., "focus on pricing" or "analyze their enterprise features")
- Output location (default: `knowledge/references/competitor-[name]-comparison.md`)

**If product-info.md exists**: Read it to understand our product for comparison purposes.

---

### Step 2: Gather Information (Multi-Source Strategy)

Follow this prioritized approach to gather comprehensive competitive intelligence:

#### Source 1: Knowledge Base (Check First)
- Use `Glob` to search for existing research: `knowledge/references/*[competitor-name]*.md`
- Use `Glob` to find transcripts: `knowledge/transcripts/*[competitor-name]*.md`
- Use `Read` to load any existing research notes
- **Why first**: User-provided research is most reliable and contextual

#### Source 2: Notion Workspace (If Available)
- Check if Notion MCP tools are available
- Use `Notion:notion-search` with queries like:
  - `[Competitor Name]`
  - `[Competitor Name] pricing`
  - `[Competitor Name] features`
  - `[Competitor Name] customers`
- Use `Notion:notion-fetch` to retrieve relevant pages
- **Why second**: Internal research may contain analysis and context

#### Source 3: Web Search (Public Information)
- Use `WebSearch` for targeted queries:
  - `[Competitor Name] pricing 2026`
  - `[Competitor Name] features`
  - `[Competitor Name] customers case studies`
  - `[Competitor Name] reviews`
  - `[Competitor Name] vs competitors`
- Use `WebFetch` to retrieve specific pages:
  - Competitor's official pricing page
  - Competitor's features/product page
  - Review sites (G2, Capterra, TrustRadius)
  - Customer testimonial pages
- **Why third**: Most current public information, but needs validation

#### Source 4: User Input (Always Available)
- Ask user if they have specific sources to include
- Ask about particular aspects to focus on
- Clarify any ambiguous information
- **Why last**: Fill gaps identified in other sources

**Research Categories to Cover**:

For each source, extract information in these categories:

1. **Company Overview**:
   - Mission/vision statements
   - Founded date, headquarters
   - Company size (employees, funding, revenue if public)
   - Recent news or developments

2. **Product Features**:
   - Core capabilities
   - Unique differentiators
   - Feature list (organize by category)
   - Technical architecture/approach
   - Integrations and ecosystem

3. **Pricing Model**:
   - Pricing tiers (Free, Starter, Pro, Enterprise)
   - Cost per tier
   - What's included in each tier
   - Free trial details
   - Hidden fees or additional costs
   - Discounts (annual, volume, non-profit)

4. **Target Customers**:
   - Ideal customer profile (company size, industry, role)
   - Named customers (from case studies, logos on website)
   - Target markets/geographies
   - Use cases they optimize for

5. **Strengths & Competitive Advantages**:
   - What they do better than alternatives
   - Market position (leader, challenger, niche)
   - Brand strength
   - Network effects or moats
   - Technology advantages

6. **Weaknesses & Gaps**:
   - Common complaints (from reviews, Reddit, forums)
   - Missing features (compared to competitors or our product)
   - Scalability issues
   - Customer support problems
   - Pricing concerns

7. **Customer Testimonials & Reviews**:
   - Positive quotes (verbatim from reviews, case studies)
   - Critical feedback (verbatim from reviews)
   - Overall sentiment (ratings on review sites)
   - Common praise themes
   - Common criticism themes

8. **Market Positioning**:
   - How they describe themselves (tagline, value prop)
   - Key messaging themes
   - Positioning vs competitors
   - Marketing approach
   - Target personas they emphasize

---

### Step 3: Analyze and Synthesize

After gathering raw data, analyze it:

**Extract Evidence**:
- Quote liberally with attribution (never paraphrase reviews)
- Use specific data points (numbers, percentages, dates)
- Note conflicting information from different sources
- Flag assumptions vs. facts

**Identify Patterns**:
- Themes across multiple reviews
- Consistency between marketing claims and customer feedback
- Feature gaps relative to our product (if product-info.md exists)
- Pricing positioning in market

**Assess Data Quality**:
- Note data freshness (when was it published?)
- Flag outdated information (pricing from 2 years ago)
- Identify information gaps (missing pricing, no customer testimonials)
- Mark speculative vs. confirmed information

**Load Analysis Framework**:
- Read `references/research-methodology.md` for systematic analysis approach
- Follow credibility checks and validation steps
- Apply framework to ensure comprehensive coverage

---

### Step 4: Generate Report

Use the structure from `assets/competitor-profile-template.md` to create the report.

**Report Sections** (in order):

1. **Executive Summary** (2-3 key takeaways)
   - Most important insights for strategic decision-making
   - What makes this competitor unique or threatening
   - Key gaps or opportunities identified

2. **Company Overview**
   - Background, size, mission
   - Recent developments
   - Market position

3. **Product Features** (use table format)
   - Feature comparison table (if product-info.md exists)
   - Unique capabilities we don't have
   - Missing features they don't have

4. **Pricing Model** (use table format)
   - Pricing tiers table
   - Comparison to our pricing (if known)
   - Notes on discounts, free trials

5. **Target Customers**
   - Ideal customer profile
   - Named customers and case studies
   - Market segments

6. **Strengths & Competitive Advantages**
   - Numbered list with evidence
   - What they do exceptionally well
   - Why customers choose them

7. **Weaknesses & Gaps**
   - Numbered list with evidence
   - Common complaints
   - Opportunities for us to capitalize

8. **Customer Testimonials**
   - Positive quotes (verbatim with source + date)
   - Critical feedback (verbatim with source + date)
   - Overall sentiment summary

9. **Market Positioning**
   - How they position themselves
   - Key messaging themes
   - Differentiation strategy

10. **Strategic Implications**
    - **Threats**: How their strengths threaten us
    - **Opportunities**: Gaps we can exploit
    - **Recommended Response**: Strategic recommendation

11. **Data Sources & Citations**
    - Web sources (URL + date accessed)
    - Notion pages (mention format if used)
    - Knowledge base files (file paths)
    - User-provided sources

12. **Metadata**
    - Last Updated: [YYYY-MM-DD]
    - Data Freshness Assessment
    - Recommended Re-Research Timeline (3-6 months)

**Formatting Best Practices**:
- Use tables for features and pricing (easier to scan)
- Use blockquotes for testimonials with attribution
- Use ✅/⚠️/❌ for feature comparisons
- Include "Comparison to Us" column only if product-info.md exists
- Bold key terms and company names
- Link all sources (URLs, file paths)

---

### Step 5: Save Output

**Default location**: `knowledge/references/competitor-[name]-comparison.md`
- Normalize name to lowercase-with-hyphens
- Example: "Stripe" → `competitor-stripe-comparison.md`

**Custom location**: If user specifies different path, save there instead

**After saving**:
- Confirm save location to user
- Provide 2-3 sentence summary of key findings
- Suggest next steps (research more competitors, create comparison matrix)

---

## Best Practices

**Quote Liberally**:
- Always use verbatim quotes for testimonials and reviews
- Never paraphrase customer feedback
- Always attribute with source and date

**Use Tables**:
- Features comparison: table format
- Pricing tiers: table format
- Makes reports scannable for PMs

**Flag Data Gaps**:
- If pricing not found: note "Pricing not publicly available"
- If few reviews: note "Limited customer feedback found"
- If outdated: note "Data from [year], may be outdated"

**Cite Everything**:
- Every fact should trace to a source
- Use markdown links for web sources
- Use file paths for knowledge base sources
- Use Notion mention format for Notion pages

**Assess Freshness**:
- Note when data was collected
- Flag information older than 6 months
- Recommend re-research timeline (usually 3-6 months)

**Focus on Strategic Value**:
- Don't just list features - analyze what they mean
- Identify gaps that represent opportunities
- Highlight threats from their strengths
- Provide actionable recommendations

---

## Error Handling

**If competitor website not found**:
- Ask user for correct URL
- Try common variations (.com, .io, .co)
- Search for "[Competitor Name] official website"

**If no pricing information found**:
- Note "Pricing not publicly available - likely custom/enterprise only"
- Look for analyst reports or user discussions about pricing
- Ask user if they have pricing information

**If Notion MCP unavailable**:
- Skip Notion search gracefully
- Note in report: "Notion research not performed (MCP unavailable)"
- Proceed with other sources

**If WebSearch fails**:
- Note which searches failed
- Proceed with available sources
- Flag gaps in final report

**If very little information found**:
- Still create report with available information
- Clearly mark data gaps
- Suggest manual research or user interviews
- Recommend researching a different competitor if this one is too obscure

---

## When to Use This Skill vs. Workflow

**Use this skill directly when**:
- User asks to research ONE specific competitor
- Example: "Research Stripe's pricing model"
- Example: "Analyze how Square positions itself"

**Use /competitor-research workflow when**:
- User wants to research MULTIPLE competitors
- User wants a comparison matrix across competitors
- User has a competitors.md file with a list
- Example: "/competitor-research Stripe, Square, PayPal"

---

## Integration with Other Tools

**With /competitor-research workflow**:
- Workflow invokes this skill multiple times in parallel
- Each instance analyzes one competitor
- Workflow aggregates results into comparison matrix

**With product-strategy skill** (when available):
- Strategy documents can reference competitor analysis reports
- Competitive landscape analysis uses these reports as input
- SWOT analysis pulls from competitor strengths/weaknesses

---

## Reference Documents

For detailed guidance during research:
- `references/research-methodology.md` - Systematic competitor analysis framework
- `references/data-source-guide.md` - How to prioritize and use each source type
- `assets/competitor-profile-template.md` - Complete output template
- `assets/analysis-checklist.md` - Quality checklist before finalizing report
