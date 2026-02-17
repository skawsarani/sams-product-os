# API Reference Format Guide

Standards for writing Stripe-quality API endpoint documentation.

## Philosophy

- **Docs are a product.** Developer documentation is the first impression of your API. Treat it with the same rigor as the API itself.
- **Stripe is the benchmark.** Clear, complete, copy-paste ready. Every endpoint is self-contained — a developer should never need to leave the page.
- **Developers scan, then read.** Structure for scanning (tables, headers, code blocks), then provide depth for those who need it.

## Page Structure Per Resource

Every resource page follows this order:

1. **Page header** — Resource name, API version, base URL, last updated date
2. **Authentication block** — How to auth, key formats, environments (sandbox/production)
3. **Rate limits table** — Requests/min by tier, rate limit headers, backoff guidance
4. **The [Resource] Object** — Full attribute table with types, descriptions, constraints
5. **Endpoint sections** (one per operation, in CRUD order):
   - Create → Retrieve → Update → List → Delete
   - Each follows the endpoint section template below

## Endpoint Section Template

Each endpoint section contains:

1. **Title**: Verb + Resource (e.g., "Create a Payment")
2. **HTTP method and path**: `POST /v1/payments`
3. **Description**: 1-2 sentences — what it does and primary use case
4. **Parameters table**: Every param with name, type, required/optional, description
5. **Request examples**: cURL, Node.js, Python (in that order, always)
6. **Response table**: Key fields in the response with types and descriptions
7. **Response JSON**: Complete example response
8. **Error table**: All possible errors with code, HTTP status, description, resolution
9. **Related endpoints**: Links to related operations

## Parameter Table Conventions

### Required vs Optional vs Conditional

| Marker | Meaning | Example |
|--------|---------|---------|
| **Required** | Must be included in every request | `amount` |
| Optional | Can be omitted; note default if any | `description` (default: `null`) |
| Conditional | Required only when another condition is true | `province` (required when `country` is `CA`) |

### Parameter Descriptions

- Start with a noun or verb, not "The" or "A"
- Include constraints: min/max, character limits, allowed values
- Note defaults explicitly: "Default: `10`"
- For enums, list all values: "One of: `pending`, `active`, `completed`, `failed`"

**Good:** `Amount in cents. Must be a positive integer greater than 0.`
**Bad:** `The amount field.`

## Code Sample Conventions

### Language Order

Always: cURL → Node.js → Python. No exceptions.

### Rules

- **Use test keys**: Always `sk_test_your_secret_key`, never real credentials
- **Complete requests**: Include all headers, auth, content type — no shortcuts
- **Show the full request**: Don't truncate with `...` or `// more params`
- **Variable naming**: Consistent across languages (`resource`, not `res`/`r`/`result`)
- **Error handling**: Include in Node.js and Python samples (try/catch, raise_for_status)
- **Console output**: Print the key identifier and status after every request

### cURL Conventions

```bash
curl -X POST https://sandbox.api.example.com/v1/resources \
  -H "Authorization: Bearer sk_test_your_secret_key" \
  -H "Content-Type: application/json" \
  -d '{
    "key": "value"
  }'
```

- Use `-X METHOD` explicitly (even for GET for clarity in docs)
- Line continuation with `\` for readability
- Headers before body (`-H` before `-d`)
- JSON body with proper indentation

### Node.js Conventions

```javascript
const response = await fetch('https://sandbox.api.example.com/v1/resources', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer sk_test_your_secret_key',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ key: 'value' }),
});

const resource = await response.json();
console.log(resource.id);
```

- Use `fetch` (native, no SDK dependency)
- `async/await` (not `.then()` chains)
- `const` for all declarations
- Single quotes for strings

### Python Conventions

```python
import requests

response = requests.post(
    "https://sandbox.api.example.com/v1/resources",
    headers={"Authorization": "Bearer sk_test_your_secret_key"},
    json={"key": "value"},
)

resource = response.json()
print(resource["id"])
```

- Use `requests` library (standard, no SDK dependency)
- Synchronous style (not `asyncio`)
- `f-strings` for string interpolation
- Double quotes for strings

## Error Documentation Standards

Every error must include:

| Column | Required | Description |
|--------|----------|-------------|
| Code | Yes | Machine-readable error code (snake_case) |
| HTTP Status | Yes | Status code (400, 401, 404, 429, etc.) |
| Description | Yes | Human-readable explanation of what went wrong |
| Resolution | Yes | Specific steps to fix the error — not just "check your input" |

**Good resolution:** `Ensure amount is a positive integer in cents (e.g., 1000 = $10.00). Minimum: 100 ($1.00).`
**Bad resolution:** `Check the amount field.`

### Standard Error Response Format

```json
{
  "error": {
    "code": "invalid_amount",
    "message": "Amount must be a positive integer greater than 0.",
    "param": "amount",
    "type": "invalid_request_error"
  }
}
```

## Authentication Block Template

Every page includes this near the top:

- Auth method (Bearer token, API key header, etc.)
- Key format and prefix (`sk_test_` for sandbox, `sk_live_` for production)
- Where to find keys (dashboard location)
- Security warning (never expose in client-side code)
- Environment table (sandbox vs production URLs and key prefixes)

## Rate Limits

- Specify limits per tier (standard, enterprise)
- List rate limit response headers (`X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`)
- Recommend exponential backoff for 429 responses
- Note if specific endpoints have different limits

## Pagination

- Use cursor-based pagination (not offset) for stable results
- Document `limit`, `starting_after`, `ending_before` params
- Show the list response wrapper: `{ object: "list", data: [...], has_more: true }`
- Include a pagination code example

## Idempotency

- Document `Idempotency-Key` header support for POST requests
- Explain behavior: same key + same params = same response (no duplicate creation)
- Note key expiration (typically 24 hours)
- Warn about key reuse with different params (409 Conflict)
