# Code Recipe Format Guide

Standards for writing multi-language code recipes.

## Naming Conventions

### Recipe Titles

- **Outcome-oriented**: Describe what the developer accomplishes, not the HTTP method
- **Start with a verb**: Create, Accept, Refund, List, Cancel, Verify
- **Be specific**: Name the resource and the action

| Good | Bad |
|------|-----|
| Accept a Payment | POST /v1/payments |
| Create a Refund | Refunds API |
| Verify a Payout | Using the Verify Endpoint |
| List Active Merchants | GET merchants |

### File Naming

- Kebab-case matching the title: `accept-a-payment.md`, `create-a-refund.md`
- Group related recipes by resource folder when generating multiple

## Code Quality Requirements

### Completeness

Every code sample must be:
- **Runnable as-is** with test credentials — no missing imports, no placeholder functions
- **Self-contained** — doesn't depend on code from other recipes (unless explicitly noted in "What You'll Need")
- **Error-handled** — includes basic error handling in Node.js and Python (try/catch, raise_for_status)

### No Shortcuts

- Never use `...` or `// ...` to truncate code
- Never use `// TODO` or placeholder comments
- Never omit headers, auth, or content type
- Never use `var` in JavaScript (use `const`/`let`)
- Never skip the response parsing step

### Descriptive Names

Use meaningful variable names that are consistent across all three languages:

| Concept | cURL | Node.js | Python |
|---------|------|---------|--------|
| API response | N/A (raw output) | `response` | `response` |
| Parsed object | N/A | `resource` / `payment` / `refund` | `resource` / `payment` / `refund` |
| API key | Inline in header | `SECRET_KEY` | `SECRET_KEY` |
| Base URL | Inline | `BASE_URL` | `BASE_URL` |
| Resource ID | Inline in URL | `resourceId` | `resource_id` |

## Language-Specific Conventions

### cURL

```bash
curl -X POST https://sandbox.api.example.com/v1/resources \
  -H "Authorization: Bearer sk_test_your_secret_key" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: unique-key-here" \
  -d '{
    "amount": 1000,
    "currency": "cad"
  }'
```

Rules:
- Always use `-X METHOD` explicitly
- Line continuation with ` \` (space before backslash)
- Headers (`-H`) before body (`-d`)
- JSON body with 2-space indentation
- Single quotes around the JSON body
- Double quotes inside JSON

### Node.js

```javascript
const fetch = require('node-fetch');

const SECRET_KEY = 'sk_test_your_secret_key';
const BASE_URL = 'https://sandbox.api.example.com/v1';

async function createResource() {
  const response = await fetch(`${BASE_URL}/resources`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${SECRET_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      amount: 1000,
      currency: 'cad',
    }),
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(`API error: ${error.code} — ${error.message}`);
  }

  const resource = await response.json();
  console.log('Created:', resource.id);
  return resource;
}

createResource().catch(console.error);
```

Rules:
- `require` for imports (widest compatibility, no build step)
- `async/await` for all async operations (not `.then()`)
- `const` for all declarations
- Single quotes for strings
- Trailing commas in objects and arrays
- `console.log` with descriptive label
- Wrap in named async function with `.catch(console.error)`
- Include basic error check (`if (!response.ok)`)

### Python

```python
import requests
import uuid

SECRET_KEY = "sk_test_your_secret_key"
BASE_URL = "https://sandbox.api.example.com/v1"

response = requests.post(
    f"{BASE_URL}/resources",
    headers={
        "Authorization": f"Bearer {SECRET_KEY}",
        "Content-Type": "application/json",
    },
    json={
        "amount": 1000,
        "currency": "cad",
    },
)

response.raise_for_status()
resource = response.json()
print(f"Created: {resource['id']}")
```

Rules:
- Use `requests` library (standard HTTP client)
- Synchronous style (no `asyncio`, no `aiohttp`)
- Double quotes for strings
- `f-strings` for interpolation
- `response.raise_for_status()` for error checking
- `json=` parameter for POST bodies (not `data=json.dumps()`)
- `print()` with f-string for output
- Top-level script style (not wrapped in functions unless needed)

## Variations Rules

Variations show how to modify the base recipe for different use cases.

### Format

Use diff-style to highlight what changes:

```diff
  {
    "amount": 1000,
-   "currency": "cad",
+   "currency": "usd",
    "description": "Order #1234"
  }
```

### Rules

- **Additive, not full rewrites**: Only show what changes from the base
- **One variation per concept**: Don't combine multiple changes
- **Title describes the variation**: "With a different currency", "With metadata"
- **Max 3-4 variations per recipe**: More than that → write a separate recipe

## Response Display

- Always show the **complete** JSON response (not truncated)
- Format with 2-space indentation
- Include all fields the developer might reference
- Use realistic but obviously test data (`prefix_abc123def456`, not `12345`)

## Error Handling Table

Every recipe ends with an error table:

| Column | Required | Description |
|--------|----------|-------------|
| Error Code | Yes | Machine-readable code (snake_case) |
| HTTP Status | Yes | Status code |
| What Happened | Yes | Plain-English explanation |
| What to Do | Yes | Specific fix — actionable, not vague |

Include the 3-5 most likely errors for that operation. Always include:
- Auth errors (401)
- Validation errors (400) specific to the params used
- Rate limiting (429)

## Related Recipes

End with a table linking to 2-4 related recipes:
- The logical next operation (Create → Retrieve)
- The reverse operation (Create → Cancel/Delete)
- A complementary feature (Create Payment → Handle Webhook)

Each link gets a 1-sentence description.
