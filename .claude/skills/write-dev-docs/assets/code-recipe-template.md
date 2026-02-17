# [Outcome-Oriented Title — e.g., "Accept a Payment"]

[1-2 sentences describing what this recipe accomplishes and when to use it.]

---

## When to Use This

- [Scenario 1 — e.g., "You need to charge a customer for a one-time purchase"]
- [Scenario 2 — e.g., "You're building a checkout flow"]

## What You'll Need

- API secret key (starts with `sk_test_` for sandbox)
- [Any other prerequisites — e.g., "A customer ID from the Create Customer recipe"]

---

## Code

### cURL

```bash
curl -X POST https://sandbox.api.example.com/v1/[resources] \
  -H "Authorization: Bearer sk_test_your_secret_key" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $(uuidgen)" \
  -d '{
    "amount": 1000,
    "currency": "cad",
    "description": "Order #1234",
    "metadata": {
      "order_id": "ord_1234"
    }
  }'
```

### Node.js

```javascript
const fetch = require('node-fetch');

const SECRET_KEY = 'sk_test_your_secret_key';
const BASE_URL = 'https://sandbox.api.example.com/v1';

async function createResource() {
  const response = await fetch(`${BASE_URL}/[resources]`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${SECRET_KEY}`,
      'Content-Type': 'application/json',
      'Idempotency-Key': crypto.randomUUID(),
    },
    body: JSON.stringify({
      amount: 1000,
      currency: 'cad',
      description: 'Order #1234',
      metadata: {
        order_id: 'ord_1234',
      },
    }),
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(`API error: ${error.code} — ${error.message}`);
  }

  const resource = await response.json();
  console.log('Created:', resource.id);
  console.log('Status:', resource.status);
  return resource;
}

createResource().catch(console.error);
```

### Python

```python
import requests
import uuid

SECRET_KEY = "sk_test_your_secret_key"
BASE_URL = "https://sandbox.api.example.com/v1"

response = requests.post(
    f"{BASE_URL}/[resources]",
    headers={
        "Authorization": f"Bearer {SECRET_KEY}",
        "Content-Type": "application/json",
        "Idempotency-Key": str(uuid.uuid4()),
    },
    json={
        "amount": 1000,
        "currency": "cad",
        "description": "Order #1234",
        "metadata": {
            "order_id": "ord_1234",
        },
    },
)

response.raise_for_status()
resource = response.json()
print(f"Created: {resource['id']}")
print(f"Status: {resource['status']}")
```

---

## What This Does

1. Sends a POST request to create a new [resource] with the specified amount and currency
2. Includes an idempotency key to prevent duplicate creation on retries
3. Attaches metadata for your internal tracking (e.g., order ID)
4. Returns the created [resource] with a `pending` status

---

## Expected Response

```json
{
  "id": "prefix_abc123def456",
  "object": "[resource]",
  "created_at": 1700000000,
  "status": "pending",
  "amount": 1000,
  "currency": "cad",
  "description": "Order #1234",
  "metadata": {
    "order_id": "ord_1234"
  }
}
```

---

## Variations

### With a different currency

Change the `currency` parameter:

```diff
  {
    "amount": 1000,
-   "currency": "cad",
+   "currency": "usd",
    "description": "Order #1234"
  }
```

### With expanded related objects

Add the `expand` parameter to include full objects instead of IDs:

```diff
  {
    "amount": 1000,
    "currency": "cad",
+   "expand": ["customer", "source"],
    "description": "Order #1234"
  }
```

---

## Error Handling

| Error Code | HTTP Status | What Happened | What to Do |
|-----------|------------|---------------|------------|
| `invalid_amount` | 400 | Amount is zero, negative, or not an integer | Pass a positive integer in cents (e.g., `1000` = $10.00) |
| `invalid_currency` | 400 | Currency code not recognized | Use a three-letter ISO code: `cad`, `usd`, `eur` |
| `authentication_failed` | 401 | API key is invalid or missing | Check the `Authorization` header uses `Bearer sk_test_...` |
| `idempotency_conflict` | 409 | Same idempotency key used with different params | Generate a new idempotency key for different requests |
| `rate_limit_exceeded` | 429 | Too many requests | Implement exponential backoff; retry after `Retry-After` header |

---

## Related Recipes

| Recipe | Description |
|--------|-------------|
| [Retrieve a Resource](link) | Fetch a resource by ID to check its status |
| [List Resources](link) | Get a filtered, paginated list of resources |
| [Handle Webhooks](link) | React to resource status changes in real-time |
