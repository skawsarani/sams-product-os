# Product Metrics Analysis Frameworks

## Table of Contents
- [AARRR (Pirate Metrics)](#aarrr-pirate-metrics)
- [Product-Market Fit Metrics](#product-market-fit-metrics)
- [Cohort Analysis](#cohort-analysis)
- [North Star Framework](#north-star-framework)

## AARRR (Pirate Metrics)

Five-stage customer lifecycle framework for SaaS and digital products.

### Stages

1. **Acquisition** - How users discover you
   - Traffic sources, CAC, sign-up conversions
   - Key question: Where are users coming from?

2. **Activation** - First user experience
   - Onboarding completion, time-to-value, aha moment
   - Key question: Do users have a great first experience?

3. **Retention** - Do users come back?
   - DAU/MAU, cohort retention curves, churn rate
   - Key question: Are users coming back?

4. **Revenue** - How do you monetize?
   - Conversion rate, ARPU, LTV
   - Key question: Are we making money per user?

5. **Referral** - Do users tell others?
   - K-factor, NPS, viral coefficient
   - Key question: Do users recommend us?

### When to Use
- Analyzing end-to-end user journey
- Identifying funnel bottlenecks
- Prioritizing growth experiments

### Analysis Pattern
1. Calculate metrics for each stage
2. Identify the weakest stage (lowest conversion)
3. Focus optimization efforts there first

---

## Product-Market Fit Metrics

Frameworks for assessing whether a product has achieved product-market fit.

### Sean Ellis Test
- Survey users: "How would you feel if you could no longer use this product?"
- **40%+ saying "very disappointed"** = strong PMF signal
- Below 40% = need to improve core value proposition

### Retention Curves
- **Flattening curve** = PMF achieved (users stay engaged)
- **Declining to zero** = no PMF (users abandon product)
- Look for plateau at 20-30%+ retention

### Engagement Depth
- **Power users**: Use product daily/multiple times per week
- **Core feature adoption**: % of users using key features
- **High engagement** = strong PMF indicator

### When to Use
- Evaluating early-stage product traction
- Deciding whether to scale or iterate
- Assessing new feature adoption

---

## Cohort Analysis

Time-based grouping to understand user behavior patterns over time.

### Types

1. **Acquisition Cohorts** - Group by sign-up date
   - Compare retention across months
   - Identify if product improvements help retention

2. **Behavioral Cohorts** - Group by action taken
   - Users who completed onboarding vs. didn't
   - Users who adopted feature X vs. didn't

### Key Metrics
- Retention rate by cohort (D1, D7, D30, D90)
- Revenue per cohort over time
- Feature adoption by cohort

### When to Use
- Understanding retention trends
- Measuring impact of product changes
- Forecasting LTV

### Analysis Pattern
1. Define cohort grouping (time-based or behavioral)
2. Track key metric over time for each cohort
3. Compare cohorts to spot patterns
4. Investigate anomalies (why is Feb cohort better?)

---

## North Star Framework

Single metric that best captures core value delivered to customers.

### Characteristics of Good North Star Metrics
- **Reflects value delivered** to customers
- **Measurable** and trackable
- **Actionable** by the team
- **Leading indicator** of revenue

### Examples
- Airbnb: Nights booked
- Spotify: Time spent listening
- Slack: Messages sent by teams
- WhatsApp: Number of messages sent

### Supporting Metrics
Break down North Star into 3-5 input metrics that drive it.

Example (Slack):
- North Star: Messages sent
- Inputs: Active teams, messages per team, retention rate

### When to Use
- Aligning team on what matters most
- Prioritizing initiatives by North Star impact
- Tracking overall product health

### Analysis Pattern
1. Calculate North Star metric
2. Analyze trend over time (growing/declining?)
3. Break down by input metrics
4. Identify which inputs are lagging
5. Focus efforts on improving weak inputs
