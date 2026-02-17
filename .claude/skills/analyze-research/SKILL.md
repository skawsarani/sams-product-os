---
name: analyze-research
description: Analyzes user interviews, research transcripts, and feedback to extract themes, generate insights, create personas, and synthesize findings into actionable reports. Invoked when asked to analyze interviews, synthesize research, identify pain points, or produce research synthesis.
---

# User Research Analysis

## Overview

Systematically analyze user interviews, research transcripts, surveys, and feedback to extract themes, identify patterns, generate actionable insights, and create comprehensive synthesis reports or personas.

## Analysis Workflow

### 1. Understand the Request

Clarify what type of analysis is needed:
- **Theme extraction**: Identify recurring topics and patterns
- **Insight generation**: Synthesize findings into actionable recommendations
- **Persona creation**: Build user profiles from research data
- **Quick synthesis**: Summarize key findings
- **Full report**: Comprehensive research synthesis document

Determine the source materials:
- Location of transcripts (typically `meetings/`)
- Related documents in `initiatives/`
- Timeframe or specific interviews to analyze

Use `qmd query "research topic"` to find related transcripts and documents across meetings/ and initiatives/.
- Any specific questions to answer

### 2. Review Source Materials

Read through all relevant materials:
- Interview transcripts
- Survey responses
- Feedback forms
- Meeting notes
- Related product specs, opportunities, or initiatives

**Use the analysis framework** by reading `references/analysis-framework.md` for systematic guidance on:
- How to extract themes
- How to categorize findings
- How to quote effectively
- How to generate insights from observations

### 3. Perform Analysis

Based on the analysis framework, systematically:

**Extract themes:**
- Identify recurring pain points, feature requests, behaviors
- Quote verbatim with source attribution
- Note frequency (how many users mentioned it)
- Assess intensity (how strongly they felt about it)

**Categorize findings:**
- Pain Points
- Feature Requests
- Workflow Patterns
- Usability Issues
- Jobs to be Done
- Competitive Insights

**Generate insights:**
- Transform observations into implications
- Connect findings to product strategy
- Recommend next steps
- Prioritize based on frequency, intensity, and strategic fit

### 3b. Multiple Transcript Analysis (Parallel Processing)

When analyzing 3+ transcripts, use parallel processing for efficiency:

1. **Launch parallel Explore agents** (max 3 concurrent) to analyze transcripts independently:
   ```
   Task(subagent_type="Explore", prompt="Analyze transcript [path] and extract: themes, verbatim quotes, pain points, opportunities, feature requests. Return structured findings.")
   ```

2. **Each agent extracts**:
   - Recurring themes with frequency
   - Verbatim quotes with attribution
   - Pain points with intensity assessment
   - Opportunities and feature requests
   - Jobs to be done

3. **Aggregate results** from parallel analyses:
   - Merge themes, combining frequency counts
   - Deduplicate quotes (keep best examples)
   - Cross-reference patterns that appear in multiple transcripts
   - Identify themes with highest frequency AND intensity

4. **Synthesize into unified findings**:
   - Prioritize themes by: (frequency across transcripts) x (intensity)
   - Note contradictions or outliers
   - Flag themes that only appear in 1 transcript vs. widespread patterns

**When to use parallel processing:**
- 3+ transcripts to analyze
- Transcripts are independent (different interviews, not parts of same session)
- Time efficiency is important

**When to use sequential processing:**
- 1-2 transcripts
- Transcripts are related/continuation of same session
- Deep analysis of a single interview is needed

### 4. Create Deliverable

Choose the appropriate output format:

#### Full Research Synthesis Report

Use the template at `assets/synthesis-report-template.md` when creating comprehensive reports. Copy the template structure and populate with:
- Executive summary with top 3 insights
- Detailed findings with supporting quotes
- User segments identified
- Pain points summary table
- Feature requests and opportunities
- Behavioral patterns and workflows
- Competitive insights
- Recommendations (immediate, short-term, long-term)
- Open questions and next steps

Save synthesis reports to appropriate location:
- Related to initiative: `initiatives/[initiative-name]/research-synthesis-YYYY-MM-DD.md` (or wherever user stores initiatives)
- General research: `initiatives/research-synthesis-[topic]-YYYY-MM-DD.md`

#### Insight Cards (Quick Summaries)

Use the template at `assets/insight-card-template.md` for stakeholder-friendly summaries. Each card includes:
- Priority level (High/Medium/Low)
- Category (Pain Point/Feature Request/etc.)
- Clear one-sentence insight
- Supporting quotes with sources
- Frequency data
- Why it matters
- Recommended action

Save insight cards to:
- `initiatives/insight-[brief-title]-YYYY-MM-DD.md`

#### User Personas

**Read the persona guide** at `references/persona-guide.md` for detailed instructions on creating research-based personas. The guide covers:
- What makes a good persona
- Required components (goals, pain points, behaviors, context)
- How to segment users from research
- Persona format template
- Anti-patterns to avoid

Save personas to:
- `initiatives/persona-[name].md`
- Or within relevant initiative folder (wherever user stores initiatives)

### 5. Link to Source Materials

Always reference source materials in the output:
- Link to specific transcript files
- Attribute quotes with dates and participant roles
- Note sample size and methodology
- Flag any biases or limitations

## Best Practices

**Quote liberally:**
- Use participants' exact words for authenticity
- Always attribute (Interview YYYY-MM-DD with [Role])
- Preserve emotional tone in brackets [frustrated], [excited]

**Be systematic:**
- Follow the analysis framework for consistency
- Don't cherry-pick only data that supports assumptions
- Note contradictions or surprising findings
- Track frequency and intensity of themes

**Make it actionable:**
- Connect findings to product implications
- Suggest concrete next steps
- Prioritize recommendations
- Flag what requires further research

**Stay grounded in data:**
- Don't extrapolate beyond what research supports
- Distinguish between edge cases and patterns
- Note sample size and limitations
- Challenge confirmation bias

## Quick Reference

- **Analysis framework**: See `references/analysis-framework.md`
- **Persona creation**: See `references/persona-guide.md`
- **Full report template**: `assets/synthesis-report-template.md`
- **Insight card template**: `assets/insight-card-template.md`
