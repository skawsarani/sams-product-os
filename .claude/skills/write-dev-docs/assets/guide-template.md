# [Guide Title]

By the end of this guide, you'll have [specific outcome — e.g., "a working integration that accepts payments and handles webhooks"].

**Time to complete:** ~[N] minutes
**Difficulty:** [Beginner / Intermediate / Advanced]

---

## Overview

[2-3 sentences explaining what this guide covers and why it matters. Focus on the developer's goal, not the technology.]

**What you'll build:**
- [Specific capability 1]
- [Specific capability 2]
- [Specific capability 3]

---

## Prerequisites

Before you begin, make sure you have:

- [ ] **Account**: A sandbox account with API credentials ([sign up here](link))
- [ ] **Secret key**: Available in your dashboard under Settings → API Keys (starts with `sk_test_`)
- [ ] **Node.js** v18+ installed (`node --version`)
- [ ] **npm** or **yarn** package manager

```bash
# Verify prerequisites
node --version    # Should output v18.x or higher
npm --version     # Should output 9.x or higher
```

---

## Step 1: [Verb + Object — e.g., "Install the SDK"]

[1-2 sentences explaining why this step is necessary.]

```bash
npm install @example/sdk
```

**Expected output:**

```
added 1 package in 2s
```

> **NOTE**: If you're using yarn, run `yarn add @example/sdk` instead.

---

## Step 2: [Verb + Object — e.g., "Configure Your API Key"]

[1-2 sentences explaining what this step accomplishes.]

Create a `.env` file in your project root:

```bash
# .env
SECRET_KEY=sk_test_your_secret_key
```

Then load it in your application:

```javascript
require('dotenv').config();

const client = new ExampleClient({
  secretKey: process.env.SECRET_KEY,
});
```

> **SECURITY**: Never hard-code your secret key. Always use environment variables.

**Expected output:** No errors. The client initializes silently.

---

## Step 3: [Verb + Object — e.g., "Create Your First Resource"]

[1-2 sentences explaining what this step does and why.]

```javascript
const resource = await client.resources.create({
  amount: 1000,
  currency: 'cad',
  description: 'Test resource from quickstart',
});

console.log('Created:', resource.id);
console.log('Status:', resource.status);
```

**Expected output:**

```
Created: prefix_abc123def456
Status: pending
```

**If you see an error:**

| Error | Cause | Fix |
|-------|-------|-----|
| `authentication_failed` | Invalid API key | Check your `.env` file has the correct `sk_test_` key |
| `invalid_amount` | Amount is not a positive integer | Ensure amount is in cents (e.g., `1000` for $10.00) |

---

## Step 4: [Verb + Object — e.g., "Handle the Response"]

[1-2 sentences explaining this step.]

```javascript
if (resource.status === 'pending') {
  console.log('Resource created successfully. Waiting for processing...');

  // Poll for status update (in production, use webhooks instead)
  const updated = await client.resources.retrieve(resource.id);
  console.log('Updated status:', updated.status);
}
```

**Expected output:**

```
Resource created successfully. Waiting for processing...
Updated status: active
```

> **TIP**: In production, use webhooks instead of polling. See the [Webhooks Guide](link) for setup instructions.

---

## Step 5: [Verb + Object — e.g., "Verify in the Dashboard"]

[1-2 sentences explaining how to verify the integration worked.]

1. Open your [Sandbox Dashboard](link)
2. Navigate to [Resources] in the left sidebar
3. You should see your test resource with status "active"

---

## Testing Your Integration

Run these scenarios in sandbox to verify your integration works correctly:

| Scenario | Test Input | Expected Result |
|----------|-----------|-----------------|
| Successful creation | `amount: 1000, currency: "cad"` | Status: `active` |
| Invalid amount | `amount: -1` | Error: `invalid_amount` |
| Missing auth | Remove `Authorization` header | Error: `authentication_failed` |
| Rate limit | Send 200 requests in 1 minute | Error: `rate_limit_exceeded` (429) |

```bash
# Run the complete test
node test-integration.js
```

---

## Full Code

Here's the complete working example:

```javascript
require('dotenv').config();

const ExampleClient = require('@example/sdk');

const client = new ExampleClient({
  secretKey: process.env.SECRET_KEY,
});

async function main() {
  // Create a resource
  const resource = await client.resources.create({
    amount: 1000,
    currency: 'cad',
    description: 'Test resource from quickstart',
  });

  console.log('Created:', resource.id);
  console.log('Status:', resource.status);

  // Retrieve and verify
  const retrieved = await client.resources.retrieve(resource.id);
  console.log('Retrieved:', retrieved.id);
  console.log('Final status:', retrieved.status);
}

main().catch(console.error);
```

---

## Next Steps

Now that you have a working integration:

- **[Handle webhooks](link)** — Get real-time notifications instead of polling
- **[Go live](link)** — Switch from sandbox to production credentials
- **[API Reference](link)** — Explore all available endpoints and parameters
- **[Error handling guide](link)** — Build robust error handling for production

---

## Related Resources

| Resource | Description |
|----------|-------------|
| [API Reference](link) | Full endpoint documentation |
| [Code Recipes](link) | Copy-paste snippets for common tasks |
| [Postman Collection](link) | Test the API interactively |
| [Changelog](link) | API updates and new features |
