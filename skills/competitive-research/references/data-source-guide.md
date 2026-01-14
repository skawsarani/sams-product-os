# Data Source Guide: How to Use Each Source Type

This guide explains how to prioritize, search, and use each data source effectively for competitive research.

---

## Source Priority Strategy

Use sources in this order to maximize quality while minimizing effort:

```
1. Knowledge Base (user-provided) → Most reliable, most contextual
2. Notion (internal research) → Semi-curated, may have analysis
3. Web Search (public info) → Most current, needs validation
4. User Input (direct questions) → Fills gaps, clarifies ambiguity
```

**Why this order?**
- Start with what the user already knows (highest trust)
- Then check what the team has researched (internal context)
- Then gather public information (broad coverage)
- Finally, ask user to fill remaining gaps (targeted questions)

---

## Source 1: Knowledge Base Files

### What It Is
Markdown files in `knowledge/references/` and `knowledge/transcripts/` that contain user-provided research, notes, or interview transcripts.

### When to Use
- **Always check first** before searching externally
- User may have already researched this competitor
- May contain proprietary insights not available publicly

### How to Search

**Step 1: Use Glob for pattern matching**
```
Glob(pattern="*[competitor-name]*.md", path="knowledge/references/")
Glob(pattern="*[competitor-name]*.md", path="knowledge/transcripts/")
```

**Step 2: Try variations if nothing found**
```
Glob(pattern="*competitive*.md", path="knowledge/references/")
Glob(pattern="*market*.md", path="knowledge/references/")
```

**Step 3: Read any matches**
```
Read(file_path="knowledge/references/competitor-analysis-2025.md")
```

### What to Extract
- Existing competitor profiles
- Pricing information user has gathered
- Interview insights about competitors
- Competitive positioning notes
- Feature comparisons user has made

### Citation Format
```markdown
**Source**: knowledge/references/competitive-analysis-2025.md (Internal Research, Dec 2025)
```

### Red Flags
- File is more than 12 months old → data may be stale
- File is incomplete or has TODOs → gaps in research
- No author or date → hard to assess reliability

---

## Source 2: Notion Workspace

### What It Is
Internal Notion pages where the team may have documented competitive research, meeting notes, or strategic analysis.

### When to Use
- After checking knowledge base files
- Before web searching (internal research may have context)
- If team collaborates in Notion

### How to Search

**Step 1: Check if Notion MCP is available**
```
# If MCP tools are available, proceed
# If not available, skip gracefully to next source
```

**Step 2: Search with targeted queries**
```
Notion:notion-search(query="[Competitor Name]")
Notion:notion-search(query="[Competitor Name] pricing")
Notion:notion-search(query="[Competitor Name] features")
Notion:notion-search(query="competitive analysis [Competitor Name]")
```

**Step 3: Fetch relevant pages**
```
Notion:notion-fetch(page_id="...")
```

### Search Query Patterns

**Broad queries** (start here):
- `[Competitor Name]`
- `competitive analysis`
- `market research [category]`

**Specific queries** (if broad search succeeds):
- `[Competitor Name] pricing`
- `[Competitor Name] features`
- `[Competitor Name] customers`
- `[Competitor Name] vs us`

### What to Extract
- Team's analysis and opinions
- Meeting notes from competitor discussions
- Pricing information gathered by team
- Customer feedback mentioning competitors
- Strategic decisions related to competitors

### Citation Format
Use Notion mention format:
```markdown
<mention-page url="https://notion.so/page-id">Competitive Analysis: Stripe</mention-page>
```

Or simpler markdown link:
```markdown
**Source**: [Competitive Analysis: Stripe](https://notion.so/page-id) (Notion, last updated Jan 2026)
```

### Red Flags
- Page hasn't been updated in >6 months → may be stale
- Page has TODO sections → incomplete analysis
- Page conflicts with other sources → verify externally

### If Notion MCP Unavailable
- Don't fail - proceed to web search
- Note in final report: "Notion research not performed (MCP unavailable)"
- Suggest user manually check Notion if they have relevant pages

---

## Source 3: Web Search

### What It Is
Public information available via search engines: competitor websites, review sites, blogs, news articles, forums.

### When to Use
- After knowledge base and Notion
- For most current public information
- For broad coverage of all research categories

### Search Query Patterns

**Company Overview**:
- `[Competitor Name] company profile`
- `[Competitor Name] about funding employees`
- `[Competitor Name] crunchbase` (for funding data)

**Product Features**:
- `[Competitor Name] features`
- `[Competitor Name] capabilities`
- `[Competitor Name] product tour`
- `[Competitor Name] vs [Category Leader]` (competitors often list features)

**Pricing**:
- `[Competitor Name] pricing 2026`
- `[Competitor Name] cost`
- `[Competitor Name] pricing tiers`
- `[Competitor Name] free trial`

**Customer Reviews**:
- `[Competitor Name] G2 reviews`
- `[Competitor Name] Capterra reviews`
- `[Competitor Name] reviews`
- `[Competitor Name] reddit` (for unfiltered opinions)

**Target Customers**:
- `[Competitor Name] customers`
- `[Competitor Name] case studies`
- `[Competitor Name] testimonials`
- `[Competitor Name] who uses`

**Positioning**:
- `[Competitor Name]` (read their homepage)
- `[Competitor Name] about`
- `[Competitor Name] mission vision`

### Best Sites to Prioritize

**Tier 1 (Highest credibility)**:
- Competitor's official website
- G2.com, Capterra.com, TrustRadius.com (verified reviews)
- Crunchbase (funding, company data)
- LinkedIn Company Page (official)

**Tier 2 (Good credibility)**:
- Reddit discussions (r/[industry], r/startups)
- Hacker News discussions
- Industry blogs (if reputable)
- News articles (TechCrunch, etc.)

**Tier 3 (Use with caution)**:
- Comparison sites (may have affiliate incentives)
- Unverified blog posts
- Social media mentions
- Forum posts

### WebFetch Targets

After searching, use WebFetch to retrieve specific pages:

**Must-fetch pages**:
- Competitor's homepage (`https://competitor.com`)
- Pricing page (`https://competitor.com/pricing`)
- Features page (`https://competitor.com/features` or `/product`)

**Optional-fetch pages**:
- About page (for company background)
- Customer page (for case studies, testimonials)
- Blog (for recent announcements)
- Comparison pages (e.g., `/vs-competitor`)

### What to Extract

**From competitor website**:
- Value proposition (homepage hero)
- Feature list (product/features page)
- Pricing (pricing page)
- Target persona (about, customer pages)
- Tagline and positioning

**From review sites**:
- Overall rating (e.g., 4.5/5 stars)
- Number of reviews (more = more reliable)
- Pros (common themes in positive reviews)
- Cons (common themes in negative reviews)
- Verbatim quotes (positive and critical)

**From forums/Reddit**:
- Unfiltered customer opinions
- Common complaints not in official reviews
- Workarounds for limitations
- Comparison discussions ("Stripe vs Square")

### Citation Format
```markdown
**Source**: [Company Website](https://competitor.com) (Accessed Jan 11, 2026)
**Source**: [G2 Reviews - Stripe](https://g2.com/products/stripe/reviews) (Accessed Jan 11, 2026)
**Source**: Reddit discussion - [r/startups](https://reddit.com/r/startups/comments/...) (Posted Dec 2025)
```

### Red Flags
- Information older than 12 months (may be outdated)
- Single source for important claim (cross-reference)
- Conflicting information across sources (investigate further)
- No sources found (competitor may be very small/new/private)

---

## Source 4: User Input

### What It Is
Direct questions to the user to clarify ambiguities, fill gaps, or get specific sources they want included.

### When to Use
- **Initial clarification**: If competitor name is ambiguous
- **Gap filling**: If key information not found in other sources
- **Source suggestion**: User may know specific URLs or resources
- **Focus areas**: What aspects they care most about

### Question Patterns

**Initial clarification**:
- "I found two companies named '[Name]' - which one should I research? [Option 1 URL] or [Option 2 URL]?"
- "What's the website URL for [Competitor]? I want to ensure I research the right company."

**Gap filling**:
- "I couldn't find pricing information for [Competitor]. Do you have any pricing data or should I note it as unavailable?"
- "I found limited customer reviews for [Competitor]. Do you have any customer feedback or testimonials to include?"

**Source suggestions**:
- "Are there any specific sources you'd like me to include in this research (URLs, documents, people to reference)?"
- "Do you have any internal notes or research on [Competitor] I should incorporate?"

**Focus areas**:
- "Which aspects of [Competitor] should I focus on most: pricing, features, customers, or positioning?"
- "Are there specific features or capabilities you want me to compare against our product?"

### What to Extract
- URLs or documents user provides
- Pricing or feature details user knows
- Strategic context (why researching this competitor)
- Priorities (what matters most in analysis)

### How to Use Input
- Incorporate user-provided information into relevant sections
- Always cite when information comes from user
- If user provides a document, read it using Read tool
- If user provides a URL, fetch it using WebFetch

### Citation Format
```markdown
**Source**: User-provided (Jan 2026)
**Source**: User-provided document - insights-from-competitor-demo.pdf (Jan 2026)
```

---

## Multi-Source Validation

For critical claims, validate across multiple sources:

### High-Priority Validations
- **Pricing**: Confirm on official website + recent reviews
- **Key features**: Confirm on product page + customer reviews
- **Company size**: Confirm on LinkedIn + Crunchbase
- **Strengths/weaknesses**: Confirm across 3+ reviews

### How to Validate
1. Find claim in Source A
2. Search specifically for that claim in Source B
3. If confirmed → cite both sources
4. If conflicting → note the conflict and investigate
5. If only one source → note "single-source claim, verify"

### Example: Validating Pricing
- Check official pricing page (primary source)
- Check G2 reviews for pricing mentions (validation)
- Check Reddit for real user experiences (validation)
- If all agree → high confidence
- If mixed → note: "Pricing varies; official pricing is $X, but users report paying $Y"

---

## Handling Source Failures

### If Knowledge Base is Empty
- Not a problem - proceed to Notion
- Note: "No existing research found in knowledge base"

### If Notion MCP Unavailable
- Not a problem - proceed to web search
- Note: "Notion research not performed (MCP unavailable)"
- Suggest user manually check if they have relevant Notion pages

### If Web Search Returns Nothing
- Try variations of competitor name
- Try broader queries (industry category)
- If still nothing: ask user for website URL
- Last resort: note "Limited public information available"

### If All Sources Fail
- Don't give up on creating report
- Create report with available information
- Clearly mark sections as "Information not available"
- Suggest next steps: user interviews, sales calls, direct competitor contact

---

## Source Selection Decision Tree

```
Start
 ↓
Is competitor in knowledge base files?
├─ Yes → Read files, extract info → Continue to Notion
└─ No → Continue to Notion

Is Notion MCP available?
├─ Yes → Search Notion → Found pages?
│         ├─ Yes → Fetch and extract → Continue to Web
│         └─ No → Continue to Web
└─ No → Continue to Web (note MCP unavailable)

Run Web Search
 ↓
Found useful results?
├─ Yes → WebFetch key pages → Extract info → Done with sources
└─ No → Try alternative search queries → Still nothing?
          ├─ Ask user for sources
          └─ If user has none → Note gaps, proceed with available data

Generate Report
```

---

## Best Practices Summary

1. **Always start with knowledge base** - respect what user already knows
2. **Check Notion if available** - leverage team's internal research
3. **Web search strategically** - use targeted queries, not generic searches
4. **Cross-reference important claims** - validate pricing, key features, company data
5. **Quote verbatim** - especially for testimonials and reviews
6. **Cite everything** - every fact should trace to a source
7. **Note dates** - data freshness matters
8. **Flag gaps** - be explicit about missing information
9. **Don't fail on source unavailability** - proceed gracefully
10. **Ask user when stuck** - they may have information you can't find
