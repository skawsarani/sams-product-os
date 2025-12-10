## Metrics Expert

Expert workflow for tracking, analyzing, and querying metrics. Can directly query metrics stored in `knowledge/product-analytics/` for answers.

---

### Define Success Metrics

```
Define success metrics for [feature/project]
```

**What it does**:
- Suggests relevant metrics (usage, engagement, business)
- Defines targets and timeframes
- Explains measurement methodology
- References existing metrics from `knowledge/product-analytics/`

**When to use**: Feature kick-off, goal setting

---

### Analyze Metrics

```
Analyze the metrics in @knowledge/product-analytics/[file] and tell me what's working
```

**What it does**:
- Identifies trends and anomalies
- Compares to targets
- Suggests hypotheses for changes
- Recommends next steps

**When to use**: Weekly/monthly reviews

---

### Query Metrics

```
What are the current [metric name] numbers?
```

**What it does**:
- Queries metrics files in `knowledge/product-analytics/`
- Finds relevant metric data
- Provides current values and trends
- Answers questions about metrics directly

**When to use**: Quick metric lookups, answering questions about product performance

**Detailed Steps**:

1. **Search Metrics Files**: Look in `knowledge/product-analytics/` for relevant data
2. **Extract Values**: Find current metric values
3. **Provide Context**: Show trends, comparisons, targets
4. **Answer Question**: Directly answer the metric question

---

### Create a Metrics Dashboard

```
Design a metrics dashboard for [project/feature]
```

**What it does**:
- Identifies key metrics to track
- Organizes into hierarchy (North Star → Leading → Lagging)
- Suggests visualization approaches

**When to use**: Project kick-off

---

### Compare Metrics

```
Compare [metric A] vs [metric B] from @knowledge/product-analytics/
```

**What it does**:
- Queries both metrics from knowledge base
- Compares values and trends
- Identifies relationships
- Provides insights

**When to use**: Understanding metric relationships

---

### Answer Metric Questions

```
[Question about product performance/metrics]
```

**What it does**:
- Queries relevant metrics from `knowledge/product-analytics/`
- Synthesizes data to answer the question
- Provides supporting evidence
- Suggests follow-up questions

**When to use**: Any question about product metrics or performance

**Examples**:
- "What's our current user retention rate?"
- "How are mobile metrics performing vs desktop?"
- "What metrics improved this quarter?"
- "Which features have the highest engagement?"

---

### Prepare Interac Metrics Write-Up

```
Prepare Interac metrics write-up for this week
```

**What it does**:
- Reviews this week's metric notes from `knowledge/product-analytics/interac-metrics/`
- Analyzes previous weeks for patterns and trends
- Creates both long-form and TL;DR versions for Slack sharing
- Formats according to Interac metrics standards
- Remains neutral while covering all numbers

**When to use**: Weekly metrics review and stakeholder communication

**Detailed Steps**:

1. **Check This Week's Metric Notes**: 
   - Review metric notes in `knowledge/product-analytics/interac-metrics/`
   - Look for files in format `Metrics YYYY-MM-DD` (representing the start of the week)
   - Identify the current week's metrics file

2. **Review Previous Weeks for Patterns**:
   - Review previous weeks' metrics in `knowledge/product-analytics/interac-metrics/`
   - Identify patterns, trends, and anomalies
   - Exclude incident-related trends from patterns (incidents are handled separately)
   - Create a dedicated "Patterns" section highlighting notable trends

3. **Identify Incidents and Impact**:
   - Check for any incidents that occurred during the week
   - Document each incident and its specific impact on metrics
   - Include incident details: what happened, duration, affected metrics, and magnitude of impact
   - Create a dedicated "Incidents" section in the write-up

4. **Remain Neutral and Comprehensive**:
   - Cover all numbers in the metrics list
   - Be positive where appropriate but maintain neutrality
   - Don't hide negative trends, present them factually

5. **Generate Both Versions**:
   - Create a long-form version with full context
   - Create a TL;DR version for quick consumption
   - Both versions follow the format structure below

6. **Preserve Original Notes**:
   - Do NOT modify the original metric notes files
   - Only generate new write-up content

**Format Structure**:
- **Header:** "Week of [date range]"
- **Opening:** 1-2 sentence summary with key headline metrics and context
- **Incidents (if applicable):** List incidents and their specific impact on metrics for the week
- **Performance Highlights:** Bullet list, data-forward, grouped by theme
- **Currently Monitoring Items:** Bullet list, diagnosis-first, specific
- **Patterns (if applicable):** Dedicated section for multi-week trends (exclude incident-related patterns)
- **Footer:** Links to reports/dashboards

**Style Rules**:
- Use color-coded arrows: 🔼 for positive, 🔻 for negative
- Format: metric name + percentage + (arrow + change)
- No em dashes, use commas or periods
- Lead with insight, not observation verbs ("Hit a high" not "We observe")
- Consolidate related metrics (don't repeat similar points)
- Keep opening under 3 sentences
- Rename "Concerns" to "Currently Monitoring Items" when trends are mostly positive

**Tone**:
- Professional but conversational
- Concise, no filler phrases
- Active voice, tight sentences
- Assume savvy, time-constrained audience

**Data Presentation**:
- Use | for inline metric separation
- Bold key merchants/flows
- Include context (26-week high, below norm, etc.)
- Percentage changes in parentheses with arrows
