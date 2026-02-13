# Analysis Patterns

Detailed guides for common product metrics analysis patterns.

## Table of Contents
- [Funnel Analysis](#funnel-analysis)
- [Cohort Retention Analysis](#cohort-retention-analysis)
- [Feature Adoption Analysis](#feature-adoption-analysis)
- [Growth Rate Analysis](#growth-rate-analysis)
- [Revenue Analysis](#revenue-analysis)
- [Payments & Fintech Analysis](#payments--fintech-analysis)
- [Data Handling](#data-handling)
- [Tips for Effective Analysis](#tips-for-effective-analysis)

---

## Funnel Analysis

**When to use:** Understanding conversion flow or identifying drop-off points

**Steps:**
1. Calculate conversion rate for each step
2. Identify largest drop-off (step-to-step)
3. Focus recommendations on biggest opportunity

**Example output:**
```markdown
## Funnel Analysis: Sign-up to Active User

| Step | Count | Conversion from Start | Drop-off from Previous |
|------|-------|----------------------|------------------------|
| Landing | 10,000 | 100% | - |
| Sign-up | 2,000 | 20% | 80% |
| Onboarding | 1,500 | 15% | 25% |
| First Action | 900 | 9% | 40% |

**Biggest opportunity:** Landing → Sign-up (80% drop-off). Test value prop clarity.
```

**Common issues to investigate:**
- High drop-off at entry: Value proposition unclear
- High drop-off mid-funnel: Friction in process (too many steps, confusing UX)
- High drop-off at conversion: Payment issues, trust concerns, pricing

---

## Cohort Retention Analysis

**When to use:** Understanding if users stick around, evaluating product changes

**Steps:**
1. Group users by cohort (sign-up month or behavior)
2. Track retention at D1, D7, D30, D90
3. Compare cohorts to spot trends
4. Look for retention curve flattening (PMF signal)

**Pattern to identify:** Are newer cohorts retaining better? (Product improving vs. degrading)

**Example output:**
```markdown
## Cohort Retention Analysis

| Cohort | D1 | D7 | D30 | D90 |
|--------|----|----|-----|-----|
| Jan 2024 | 60% | 35% | 22% | 18% |
| Feb 2024 | 65% | 40% | 28% | 24% |
| Mar 2024 | 68% | 45% | 32% | 28% |

**Trend:** Retention improving month-over-month. Product changes since January are working.
**PMF signal:** Curve flattening at ~28% D90 for March cohort indicates sticky user base.
```

**Key questions:**
- Is the curve flattening? (If drops to zero, no PMF)
- Are newer cohorts better than older? (Product improving)
- What changed between cohorts? (Features, onboarding, marketing)

---

## Feature Adoption Analysis

**When to use:** Evaluating new feature success or prioritizing roadmap

**Steps:**
1. Calculate adoption rate (% of users who used feature)
2. Calculate usage frequency (among adopters)
3. Compare to benchmarks or other features
4. Look at time-to-adoption (discovery issue?)

**Key question:** Is low adoption due to low awareness or low value?

**Example output:**
```markdown
## Feature Adoption: Advanced Search

- **Adoption rate:** 15% of users tried the feature
- **Frequency:** Adopters use it 3.2 times/week
- **Time-to-adoption:** Average 8 days from sign-up

**Diagnosis:** Low adoption (15%) but high frequency (3.2x/week) among users who find it.
**Hypothesis:** Discovery problem, not value problem.
**Recommendation:** Increase visibility in UI, add onboarding tooltip.
```

**Adoption benchmarks:**
- >50%: Core feature, high visibility
- 20-50%: Power user feature, acceptable
- <20%: Niche feature or discovery issue

---

## Growth Rate Analysis

**When to use:** Tracking product momentum or goal progress

**Steps:**
1. Calculate WoW, MoM, or YoY growth
2. Identify acceleration or deceleration
3. Break down by segments (acquisition, retention, monetization)
4. Compare to targets or benchmarks

**Red flag:** Slowing growth rate may indicate PMF issues or market saturation

**Example output:**
```markdown
## Monthly Active Users Growth

| Month | MAU | MoM Growth |
|-------|-----|------------|
| Jan | 10,000 | - |
| Feb | 12,000 | +20% |
| Mar | 13,800 | +15% |
| Apr | 14,900 | +8% |

**Trend:** Growth decelerating from 20% → 8% MoM
**Breakdown:**
- New user acquisition: Still strong (+18% MoM)
- Retention: Declining (D30 retention dropped from 25% → 20%)

**Diagnosis:** Growth slowing due to retention issues, not acquisition.
**Recommendation:** Prioritize retention improvements over new features.
```

---

## Revenue Analysis

**When to use:** Understanding monetization health or optimizing pricing

**Steps:**
1. Calculate ARPU, MRR, LTV
2. Calculate LTV/CAC ratio (should be >3)
3. Identify trends over time
4. Segment by user type or cohort

**Key metrics:** ARPU trend, conversion to paid, churn impact on MRR

**Example output:**
```markdown
## Revenue Health

| Metric | Value | Trend | Target |
|--------|-------|-------|--------|
| MRR | $125K | +12% MoM | +15% |
| ARPU | $25 | Flat | Growing |
| LTV | $600 | - | - |
| CAC | $150 | - | - |
| LTV/CAC | 4.0 | ✓ | >3 |
| Conversion to Paid | 4.2% | -0.3pp | 5% |

**Insights:**
- LTV/CAC ratio healthy at 4.0
- MRR growth below target (12% vs 15%)
- Conversion to paid declining (4.2% down from 4.5%)

**Recommendations:**
1. A/B test pricing page to improve conversion
2. Investigate why ARPU is flat (no upsells?)
3. Consider expansion revenue opportunities
```

---

## Payments & Fintech Analysis

**When to use:** Analyzing payment flows, transaction health, or fintech product performance

**Steps:**
1. Calculate TPV and GMV to understand volume
2. Check payment acceptance rate (target: >90%)
3. Analyze take rate and net revenue after costs
4. Monitor risk metrics (chargeback rate <0.5%, fraud rate <0.1%)
5. Break down by payment method, geography, or merchant segment

**Key questions:**
- Is payment acceptance rate declining? (Could indicate fraud controls too strict or integration issues)
- Are chargebacks trending up? (Product quality or fraud issue)
- How does ATV vary by segment? (Pricing or use case insights)
- Is take rate sustainable given processing costs?

**Example output:**
```markdown
## Payment Health Analysis

| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| TPV | $2.5M | - | - |
| Payment Acceptance Rate | 92% | >90% | ✓ Good |
| Chargeback Rate | 0.8% | <0.5% | ⚠ High |
| Take Rate | 2.5% | 2-3% | ✓ Good |
| Fraud Rate | 0.2% | <0.5% | ✓ Good |
| ATV | $125 | - | - |

**Alert:** Chargeback rate at 0.8% is above healthy threshold.

**Investigation:**
- Breakdown by merchant: 60% of chargebacks from 3 high-risk merchants
- Reason codes: 70% "product not as described"

**Recommendations:**
1. Implement merchant quality review process
2. Add product description requirements for high-risk categories
3. Consider offboarding merchants with >2% chargeback rate
```

**Payment method analysis:**
```markdown
## Payment Method Mix

| Method | % of TPV | Avg Acceptance Rate | Avg Processing Cost |
|--------|----------|---------------------|---------------------|
| Credit Card | 60% | 94% | 2.9% + $0.30 |
| Debit Card | 25% | 96% | 1.5% + $0.25 |
| ACH | 10% | 88% | 0.8% |
| Digital Wallet | 5% | 97% | 2.5% + $0.10 |

**Insight:** ACH has lowest cost but also lowest acceptance rate.
**Opportunity:** Promote ACH for large transactions where acceptance rate improves.
```

---

## Data Handling

### CSV/Excel Files
- Read with pandas or direct file reading
- Extract relevant columns
- Handle missing data appropriately
- Note: Missing data patterns can be insights (e.g., users not filling optional fields)

**Example approach:**
```python
import pandas as pd

# Read CSV
df = pd.read_csv('metrics.csv')

# Check for missing data
print(df.isnull().sum())

# Basic stats
print(df.describe())
```

### JSON/API Responses
- Parse structure first to understand nesting
- Extract metrics at the right level of aggregation
- Handle nested arrays/objects appropriately

**Common sources:**
- Analytics API responses (Mixpanel, Amplitude, Segment)
- Database query results exported as JSON
- Product API endpoints

### SQL Query Results
- Assume data is already aggregated
- Focus on interpretation rather than re-aggregation
- Suggest additional queries if needed for deeper analysis

**If data seems incomplete, ask:**
- "Can you also pull [missing metric]?"
- "What's the breakdown by [segment]?"
- "Can we see this trended over time?"

### Analytics Dashboard Descriptions
- Extract metrics from text/screenshots
- Ask clarifying questions if data is ambiguous
- Calculate derived metrics from raw numbers
- Note limitations (e.g., "This is a point-in-time snapshot, not trended data")

---

## Tips for Effective Analysis

### 1. Start with the Question
Don't calculate every metric. Focus on what matters for the specific question.

**Bad:** "Here's your data. Let me calculate all 50 metrics..."
**Good:** "You asked about conversion. Let me focus on funnel metrics first."

### 2. Context is Critical
Benchmarks vary by industry, stage, and product type.

- B2B SaaS retention ≠ Consumer app retention
- Early-stage growth rates ≠ Mature product growth rates
- High-touch sales CAC ≠ Self-serve CAC

Always caveat with: "For [your product type/stage], this is [good/concerning/typical]"

### 3. Tell a Story
Connect metrics to user behavior and business outcomes.

**Bad:** "DAU/MAU is 23%"
**Good:** "DAU/MAU is 23%, meaning the average user engages about 7 days per month. For a productivity tool, this suggests users engage weekly rather than daily. Consider if that matches your intended use case."

### 4. Be Specific in Recommendations
Generic advice doesn't help. Give concrete next steps.

**Bad:** "Improve onboarding"
**Good:** "Reduce onboarding steps from 5 to 3 by making profile photo optional and pre-filling workspace name from email domain"

### 5. Prioritize Ruthlessly
Flag the 1-2 most impactful opportunities, not 10.

Use framework: Impact × Confidence × Effort
- High impact, high confidence, low effort = Do now
- High impact, low confidence = Test/investigate
- Low impact = Deprioritize regardless of effort

### 6. Show Your Work
Include calculations so users can verify and extend.

**Example:**
```
Conversion rate = 150 conversions ÷ 1,000 visitors × 100 = 15%
vs. industry benchmark of 10-12% → performing well
```

### 7. Caveat Appropriately
Note sample size, data limitations, and assumptions.

**Examples:**
- "Note: Only 80 users in this cohort, so directional only"
- "Assuming churn rate stays constant (may change with product improvements)"
- "Data from past 30 days may include holiday seasonality"

### 8. Look for the "Why" Behind the Numbers
Metrics tell you what happened. Analysis explains why.

**Example:**
- Metric: Retention dropped 5pp
- Surface-level: "Retention is down"
- Better: "Retention dropped after we added required phone verification in onboarding (80% → 75%)"

### 9. Compare Segments
Averages hide important patterns. Always segment when possible.

**Segment by:**
- Time periods (cohorts)
- User types (free vs. paid, power users vs. casual)
- Acquisition channel (organic vs. paid)
- Geography (regions, countries)
- Device/platform (mobile vs. desktop)

### 10. Know When to Stop
Perfect analysis is the enemy of good. Aim for:
- 80% confidence with 20% effort, not 99% confidence with 10x effort
- Actionable insights over comprehensive documentation
- Speed to decision over exhaustive research

**Ask yourself:** "Will more analysis materially change the recommendation?"
If no, ship the insight and move on.
