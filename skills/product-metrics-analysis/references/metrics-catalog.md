# Product Metrics Catalog

Quick reference for common product metrics, formulas, and benchmarks.

## User Engagement

### Daily Active Users (DAU)
- **Formula**: Count of unique users active on a given day
- **Good for**: Apps with daily use case (social, messaging, productivity)

### Monthly Active Users (MAU)
- **Formula**: Count of unique users active in a 30-day period
- **Good for**: Lower-frequency products (marketplaces, B2B tools)

### DAU/MAU Ratio (Stickiness)
- **Formula**: DAU ÷ MAU
- **Benchmark**: 20%+ is good, 50%+ is excellent
- **Interpretation**: Higher = more frequent usage

### Session Frequency
- **Formula**: Total sessions ÷ unique users
- **Good for**: Understanding usage patterns

### Session Duration
- **Formula**: Average time per session
- **Caution**: Longer isn't always better (depends on use case)

---

## Acquisition

### Customer Acquisition Cost (CAC)
- **Formula**: Total sales & marketing spend ÷ new customers acquired
- **Benchmark**: Varies widely by industry
- **Key ratio**: LTV/CAC should be > 3

### Conversion Rate
- **Formula**: Conversions ÷ total visitors × 100
- **Benchmark**: 2-5% is typical for SaaS trials
- **Context matters**: Landing page vs. in-app vs. checkout

### Traffic Sources
- **Metrics**: % of traffic by channel (organic, paid, referral, direct)
- **Good for**: Understanding acquisition channels

---

## Activation

### Onboarding Completion Rate
- **Formula**: Users who complete onboarding ÷ total sign-ups × 100
- **Benchmark**: 40-60% is typical
- **Critical**: Strong predictor of retention

### Time to Value (TTV)
- **Formula**: Time from sign-up to first key action
- **Good for**: Identifying onboarding friction
- **Goal**: Minimize this

### Activation Rate
- **Formula**: Users who reach "aha moment" ÷ total sign-ups × 100
- **Example**: Created first project, sent first message, etc.

---

## Retention

### Retention Rate
- **Formula**: Users active in period N ÷ users from cohort × 100
- **Timeframes**: D1, D7, D30, D90
- **Benchmark**: Varies widely (20-30% D30 is decent for consumer apps)

### Churn Rate
- **Formula**: Users lost ÷ users at start of period × 100
- **Benchmark**: <5% monthly for SaaS B2B, <10% for consumer
- **Note**: Monthly churn for subscription products

### Cohort Retention
- **Formula**: Track retention for cohorts over time
- **Good for**: Understanding if product improvements help retention

---

## Revenue

### Average Revenue Per User (ARPU)
- **Formula**: Total revenue ÷ total users
- **Good for**: Tracking monetization over time

### Customer Lifetime Value (LTV)
- **Formula**: ARPU × average customer lifespan (in months)
- **Alternative**: ARPU ÷ churn rate
- **Benchmark**: LTV/CAC should be > 3

### Conversion to Paid
- **Formula**: Paying users ÷ total users × 100
- **Benchmark**: 2-5% for freemium SaaS

### Monthly Recurring Revenue (MRR)
- **Formula**: Sum of all monthly subscriptions
- **Good for**: SaaS financial health

### MRR Growth Rate
- **Formula**: (MRR this month - MRR last month) ÷ MRR last month × 100
- **Benchmark**: 10-20% monthly for early-stage SaaS

---

## Feature Adoption

### Feature Adoption Rate
- **Formula**: Users who used feature ÷ total users × 100
- **Good for**: Understanding feature value

### Feature Usage Frequency
- **Formula**: Feature uses ÷ users who used it
- **Good for**: Understanding feature stickiness

### Time to Feature Adoption
- **Formula**: Days from sign-up to first feature use
- **Good for**: Identifying discovery issues

---

## Funnel Metrics

### Funnel Conversion Rate
- **Formula**: Users completing step N ÷ users starting funnel × 100
- **Good for**: Identifying drop-off points

### Step-by-Step Drop-off
- **Formula**: (Users at step N - users at step N+1) ÷ users at step N × 100
- **Good for**: Pinpointing friction points

---

## Payments & Fintech Metrics

### Total Payment Volume (TPV)
- **Formula**: Sum of all payment transaction amounts in a period
- **Good for**: Overall business scale and growth tracking
- **Note**: Different from revenue (which is take rate × TPV)

### Gross Merchandise Value (GMV)
- **Formula**: Total value of goods/services transacted through platform
- **Good for**: Marketplace platforms (GMV includes full transaction value)
- **Note**: For marketplaces, GMV > TPV if only facilitating payment

### Take Rate / Monetization Rate
- **Formula**: Revenue ÷ TPV × 100
- **Benchmark**: 1-3% for payment processors, 5-20% for marketplaces
- **Interpretation**: Higher = better monetization per dollar processed

### Payment Acceptance Rate / Authorization Rate
- **Formula**: Approved transactions ÷ total transaction attempts × 100
- **Benchmark**: 85-95% is typical (varies by region, payment method)
- **Critical**: Low rates indicate fraud controls too strict or technical issues

### Payment Success Rate
- **Formula**: Completed payments ÷ initiated payments × 100
- **Note**: Includes both authorization and settlement
- **Target**: >95% for good user experience

### Failed Payment Rate
- **Formula**: Failed transactions ÷ total transaction attempts × 100
- **Breakdown**: Decline by issuer, technical error, fraud block, insufficient funds
- **Action**: Categorize failures to identify root causes

### Average Transaction Value (ATV)
- **Formula**: TPV ÷ number of transactions
- **Good for**: Understanding customer spending patterns
- **Trend analysis**: Increasing ATV may indicate higher-value use cases

### Transaction Frequency
- **Formula**: Total transactions ÷ unique paying users
- **Good for**: Understanding repeat purchase behavior
- **Benchmark**: Varies widely by vertical (daily for food delivery, monthly for utilities)

### Chargeback Rate
- **Formula**: Chargebacks ÷ total transactions × 100
- **Benchmark**: <0.5% is good, >1% is concerning
- **Critical**: High rates can lead to merchant account termination

### Refund Rate
- **Formula**: Refunded transactions ÷ total successful transactions × 100
- **Benchmark**: 2-5% typical for e-commerce, <1% for digital goods
- **Good for**: Product quality and customer satisfaction indicator

### Fraud Rate
- **Formula**: Fraudulent transactions ÷ total transactions × 100
- **Benchmark**: <0.1% is excellent, >0.5% needs attention
- **Balance**: With false positive rate (don't over-block legitimate transactions)

### False Positive Rate (Fraud Detection)
- **Formula**: Legitimate transactions blocked ÷ total legitimate transactions × 100
- **Trade-off**: Lower fraud rate vs. lower false positive rate
- **Target**: <1% false positives while maintaining fraud rate <0.5%

### Net Revenue
- **Formula**: Gross revenue - processing fees - chargebacks - refunds
- **Good for**: Understanding true profitability
- **Critical**: Account for all payment costs

### Payment Processing Cost per Transaction
- **Formula**: Total processing costs ÷ number of transactions
- **Good for**: Unit economics and profitability analysis
- **Include**: Gateway fees, card network fees, fraud tools

### Processing Time / Settlement Time
- **Formula**: Average time from payment initiation to funds settled
- **Benchmark**: Instant to T+2 days depending on payment method
- **Good for**: Cash flow planning and user experience

### Cross-Border Transaction Rate
- **Formula**: Cross-border transactions ÷ total transactions × 100
- **Good for**: International expansion tracking
- **Note**: Higher fees and failure rates for cross-border

### Payment Method Mix
- **Formula**: % of TPV by payment method (card, ACH, wallet, BNPL, etc.)
- **Good for**: Understanding user preferences and optimizing costs
- **Action**: Promote lower-cost methods when possible

### Repeat Transaction Rate
- **Formula**: Users with 2+ transactions ÷ total users with transactions × 100
- **Benchmark**: >40% indicates good retention
- **Critical**: Strong indicator of product-market fit for payments

### First Payment Conversion Rate
- **Formula**: Users who complete first payment ÷ users who initiate first payment × 100
- **Benchmark**: >90% for good checkout experience
- **Drop-offs**: Analyze by step (cart → checkout → payment → confirmation)

### Customer Acquisition Cost (Fintech-specific)
- **Formula**: Total acquisition spend ÷ new funded accounts
- **Note**: "Funded" is key qualifier (not just sign-ups)
- **Benchmark**: Varies widely by product type

### LTV for Fintech
- **Formula**: (Average take rate per transaction × transactions per user × user lifespan)
- **Alternative**: Sum of net revenue per user over lifetime
- **Target**: LTV/CAC > 3 for sustainable growth

### Funding Time (Neobanks/Wallets)
- **Formula**: Time from account creation to first deposit
- **Benchmark**: <24 hours is good, <1 hour is excellent
- **Critical**: Faster funding = higher activation

### Active Funding Sources
- **Formula**: Users with valid payment method on file ÷ total users × 100
- **Good for**: Understanding payment readiness
- **Target**: >80% for high-intent products

---

## Statistical Concepts

### Growth Rate
- **Formula**: (New value - old value) ÷ old value × 100
- **Timeframes**: Week-over-week (WoW), month-over-month (MoM), year-over-year (YoY)

### Percentage Point Change
- **Note**: Different from percentage change
- **Example**: 20% → 25% is a 5 percentage point increase, but a 25% relative increase

### Sample Size Considerations
- Small samples (<100): Be cautious with conclusions
- Medium samples (100-1000): Directional insights OK
- Large samples (>1000): More confidence in patterns

### Outliers
- Check for data quality issues
- Decide whether to include or exclude based on context
- Document decisions
