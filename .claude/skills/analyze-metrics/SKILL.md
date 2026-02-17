---
name: analyze-metrics
description: Analyzes product metrics (usage, adoption, conversion, retention, revenue, payments/fintech) and identifies patterns in user behavior. Invoked when asked to interpret metrics, identify trends, assess feature adoption, evaluate funnel performance, or analyze payment data from CSV/Excel exports, SQL results, or analytics dashboards.
---

# Product Metrics Analysis

Analyze product data to surface insights, identify patterns, and provide actionable recommendations. Apply appropriate PM frameworks based on the question and data at hand.

## Core Capabilities

1. **Pattern Recognition** - Identify trends, anomalies, and insights in product data
2. **Framework Application** - Apply AARRR, North Star, PMF metrics, or cohort analysis as appropriate
3. **Metric Calculation** - Calculate growth rates, conversion rates, retention, and other key metrics
4. **Actionable Insights** - Surface specific, concrete recommendations based on the data

## Analysis Workflow

### 1. Understand the Context

Before diving into data, clarify:
- What question is being asked?
- What type of data is available?
- What time period or cohorts are relevant?
- What product/feature is being analyzed?

### 2. Choose the Right Framework

Select the framework that best fits the question:

- **AARRR (Pirate Metrics)** - For full-funnel analysis or identifying bottlenecks
- **Product-Market Fit Metrics** - For evaluating early traction or new feature adoption
- **Cohort Analysis** - For understanding retention or behavior over time
- **North Star Framework** - For strategic alignment or prioritization decisions

**→ Read `references/frameworks.md`** for detailed framework guidance and when to use each.

### 3. Calculate Metrics

Use `scripts/calculate_metrics.py` for common calculations:

```bash
# Core product metrics
python scripts/calculate_metrics.py growth_rate <old_value> <new_value>
python scripts/calculate_metrics.py conversion_rate <conversions> <total>
python scripts/calculate_metrics.py retention_rate <active_users> <cohort_size>
python scripts/calculate_metrics.py churn_rate <churned_users> <starting_users>
python scripts/calculate_metrics.py dau_mau_ratio <dau> <mau>
python scripts/calculate_metrics.py ltv <arpu> <churn_rate>
python scripts/calculate_metrics.py ltv_cac_ratio <ltv> <cac>
python scripts/calculate_metrics.py arpu <total_revenue> <total_users>
python scripts/calculate_metrics.py funnel <step1> <step2> <step3> ...

# Fintech/Payments metrics
python scripts/calculate_metrics.py take_rate <revenue> <tpv>
python scripts/calculate_metrics.py payment_acceptance_rate <approved> <total_attempts>
python scripts/calculate_metrics.py chargeback_rate <chargebacks> <total_transactions>
python scripts/calculate_metrics.py atv <tpv> <num_transactions>
python scripts/calculate_metrics.py fraud_rate <fraudulent> <total_transactions>
python scripts/calculate_metrics.py net_revenue <gross_revenue> <processing_fees> <chargebacks> <refunds>
```

**→ Read `references/metrics-catalog.md`** for formulas, benchmarks, and definitions of 50+ metrics.

### 4. Identify Patterns

Look for:
- **Trends** - Growth, decline, or plateaus over time
- **Anomalies** - Unexpected spikes or drops
- **Segments** - Differences between cohorts, user types, or time periods
- **Drop-offs** - Where users leave funnels
- **Correlations** - Related behaviors or metrics

**→ Read `references/analysis-patterns.md`** for detailed guides on funnel analysis, cohort retention, feature adoption, growth analysis, revenue analysis, and payments analysis.

### 5. Generate Outputs

Provide analysis in this structure:

**Summary** - 2-3 sentence overview of what the data shows

**Key Metrics** - Formatted table with calculated metrics, include benchmarks or context when relevant

**Insights** - 3-5 bullet points highlighting patterns, focus on "what this means" not just "what the numbers are"

**Recommendations** - Specific, actionable next steps, prioritized by expected impact, include what to measure to validate success

## Statistical Rigor

**Default approach:** Quick directional insights with appropriate caveats

**Sample size considerations:**
- <100: Note limited confidence, directional only
- 100-1000: Reasonable confidence for trends
- >1000: High confidence in patterns

**When uncertain:** State assumptions and ask for more data

## Reference Files

### frameworks.md
Detailed guide to AARRR, Product-Market Fit metrics, Cohort Analysis, and North Star framework.

**Read when:** Applying a specific framework or need refresh on methodology

### metrics-catalog.md
Formulas, benchmarks, and definitions for 50+ product and fintech metrics (DAU, MAU, retention, churn, ARPU, LTV, TPV, GMV, take rate, payment acceptance rate, chargeback rate, fraud rate, etc.).

**Read when:** Need formula reference or benchmark context for specific metrics

### analysis-patterns.md
Detailed step-by-step guides for common analysis patterns (funnel, cohort, feature adoption, growth, revenue, payments), data handling approaches, and tips for effective analysis.

**Read when:** Performing specific analysis type or need example outputs and best practices
