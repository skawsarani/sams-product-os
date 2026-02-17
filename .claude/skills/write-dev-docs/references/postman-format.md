# Postman Collection Format Guide

Standards for building Postman v2.1 collections with test scripts and variable chaining.

## Collection Architecture

### Schema

Always use Postman Collection v2.1:
```
https://schema.getpostman.com/json/collection/v2.1.0/collection.json
```

### Auth Inheritance

- Set auth at the **collection level** — all requests inherit automatically
- Use Bearer token auth with `{{secret_key}}` variable
- Never hard-code credentials in individual requests
- Individual requests only override auth when they need a different method (e.g., publishable key for client-side endpoints)

### Environment File

Ship the environment file **separately** from the collection:

```json
{
  "name": "[API Name] - Sandbox",
  "values": [
    {
      "key": "secret_key",
      "value": "sk_test_your_secret_key",
      "type": "secret",
      "enabled": true
    },
    {
      "key": "publishable_key",
      "value": "pk_test_your_publishable_key",
      "type": "default",
      "enabled": true
    }
  ]
}
```

Rules:
- Secret keys use `"type": "secret"` (masked in Postman UI)
- Non-secret values use `"type": "default"`
- Include a `_description` field or README request explaining setup

### Variable Scoping

| Level | Variables | Purpose |
|-------|-----------|---------|
| **Environment** | `secret_key`, `publishable_key` | Credentials that change per environment |
| **Collection** | `base_url`, resource IDs | URLs and auto-populated IDs from test scripts |
| **Request** | One-off overrides | Rarely used — prefer collection vars |

## Variable Naming

- `snake_case` for all variable names
- Prefix resource IDs with the resource name: `payment_id`, `merchant_id`, `refund_id`
- Use `base_url` (not `baseUrl` or `BASE_URL`)
- Use `secret_key` and `publishable_key` (not `apiKey` or `token`)

## Test Script Standards

### Minimum 3 Tests Per Request

Every request must have at least 3 test assertions:

1. **Status code check** — Verify the expected HTTP status
2. **Content type or structure check** — Verify response format
3. **Business logic check** — Verify a specific field value or behavior

### Test Script Template

```javascript
// Test 1: Status code
pm.test('Status code is 201', function () {
    pm.response.to.have.status(201);
});

// Test 2: Response structure
pm.test('Content-Type is application/json', function () {
    pm.response.to.have.header('Content-Type', 'application/json');
});

// Test 3: Business logic
pm.test('Response has expected fields', function () {
    const body = pm.response.json();
    pm.expect(body).to.have.property('id');
    pm.expect(body).to.have.property('status', 'pending');
});
```

### Variable Chaining in Tests

When a Create request returns an ID, save it for subsequent requests:

```javascript
// Chain: Save ID for subsequent requests
const body = pm.response.json();
if (body.id) {
    pm.collectionVariables.set('resource_id', body.id);
    console.log('Saved resource_id:', body.id);
}
```

Rules:
- Only save variables in the test script (not pre-request)
- Always check the field exists before saving (`if (body.id)`)
- Log what was saved for debugging (`console.log`)
- Use `pm.collectionVariables.set()` (not `pm.environment.set()` — collection vars travel with the collection)

### Delete Request Cleanup

Delete requests should clean up their variables:

```javascript
pm.test('Clean up resource_id variable', function () {
    pm.collectionVariables.unset('resource_id');
});
```

## Pre-Request Scripts

Use pre-request scripts for:

### Idempotency Keys

```javascript
pm.collectionVariables.set(
    'idempotency_key',
    pm.variables.replaceIn('{{$guid}}')
);
```

### Timestamps

```javascript
pm.collectionVariables.set(
    'timestamp',
    new Date().toISOString()
);
```

### Dynamic Test Data

```javascript
pm.collectionVariables.set(
    'test_amount',
    Math.floor(Math.random() * 10000) + 100  // 100-10099 cents
);
```

Rules:
- Keep pre-request scripts short (setup only, no assertions)
- Document what the script generates in the request description
- Use Postman dynamic variables where possible (`{{$guid}}`, `{{$timestamp}}`, `{{$randomInt}}`)

## Request Body Format

- Always use **raw JSON** (not form-data or x-www-form-urlencoded)
- Pre-fill with realistic test values (not empty objects or `"string"` placeholders)
- Include 2-space indentation in the raw body
- Add comments in the request description explaining each field (JSON doesn't support comments)

### Good Body

```json
{
  "amount": 1000,
  "currency": "cad",
  "description": "Test payment from Postman",
  "metadata": {
    "order_id": "ord_test_001",
    "source": "postman_collection"
  }
}
```

### Bad Body

```json
{
  "amount": 0,
  "currency": "",
  "description": ""
}
```

## Folder Ordering

Organize requests in CRUD order within each resource folder:

1. **Create** — POST
2. **Retrieve** — GET by ID
3. **Update** — PATCH/PUT by ID
4. **List** — GET collection
5. **Delete** — DELETE by ID

This ordering ensures variable chaining works when running the folder sequentially (Create produces the ID used by all subsequent requests).

### Multi-Resource Collections

For APIs with multiple resources:

```
Collection
├── Authentication (if separate auth flow)
├── Resource A
│   ├── Create Resource A
│   ├── Retrieve Resource A
│   ├── Update Resource A
│   ├── List Resource As
│   └── Delete Resource A
├── Resource B
│   ├── Create Resource B (may reference Resource A ID)
│   └── ...
└── Webhooks (if applicable)
    ├── Simulate Webhook
    └── Verify Webhook Signature
```

## Request Descriptions

Every request needs a description explaining:
1. What the request does (1 sentence)
2. Any auto-populated variables it uses
3. Any variables it sets in test scripts
4. Special behavior or prerequisites

Example:
```
Creates a new payment. The response ID is automatically saved as
`{{payment_id}}` for use in subsequent requests.

Requires `{{secret_key}}` in your environment.
```

## Export Guidance

When generating a Postman collection:

1. **Export format**: Always Postman v2.1 (`collection.json`)
2. **Environment file**: Ship separately as `environment.json`
3. **README request**: Optionally include a "README" request at the top of the collection with setup instructions in the description (no actual URL — just docs)
4. **File naming**: `[api-name]-collection.json` and `[api-name]-sandbox-environment.json`
5. **Validation**: The JSON must be valid and importable — test by parsing with `JSON.parse()` before presenting
