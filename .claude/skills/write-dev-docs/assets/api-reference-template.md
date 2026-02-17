# [Resource Name]

**API Version:** v1
**Base URL:** `https://api.example.com/v1`
**Last Updated:** YYYY-MM-DD

---

## Authentication

All API requests require authentication via Bearer token in the `Authorization` header.

```
Authorization: Bearer sk_test_your_secret_key
```

| Environment | Key Prefix | Base URL |
|-------------|-----------|----------|
| Sandbox | `sk_test_` | `https://sandbox.api.example.com/v1` |
| Production | `sk_live_` | `https://api.example.com/v1` |

> **SECURITY**: Never expose your secret key in client-side code. All API calls must be made server-side.

---

## Rate Limits

| Tier | Requests/min | Burst |
|------|-------------|-------|
| Standard | 100 | 20 |
| Enterprise | 1,000 | 100 |

Rate limit headers are included in every response:
- `X-RateLimit-Limit` — Maximum requests per window
- `X-RateLimit-Remaining` — Requests remaining in current window
- `X-RateLimit-Reset` — Unix timestamp when the window resets

---

## The [Resource] Object

A [resource] represents [what it models in the real world].

### Attributes

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier with `prefix_` prefix. |
| `object` | string | Always `"[resource]"`. |
| `created_at` | integer | Unix timestamp of creation. |
| `updated_at` | integer | Unix timestamp of last update. |
| `status` | string | Current status. One of: `pending`, `active`, `completed`, `failed`. |
| `amount` | integer | Amount in cents (e.g., `1000` = $10.00). |
| `currency` | string | Three-letter ISO currency code (e.g., `cad`). |
| `metadata` | object | Set of key-value pairs for storing additional information. |

### Example Object

```json
{
  "id": "prefix_abc123def456",
  "object": "[resource]",
  "created_at": 1700000000,
  "updated_at": 1700000000,
  "status": "active",
  "amount": 1000,
  "currency": "cad",
  "metadata": {}
}
```

---

## Create a [Resource]

Creates a new [resource].

```
POST /v1/[resources]
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `amount` | integer | **Required** | Amount in cents. Must be greater than 0. |
| `currency` | string | **Required** | Three-letter ISO currency code. |
| `description` | string | Optional | Arbitrary string for your records. Max 500 characters. |
| `metadata` | object | Optional | Key-value pairs. Max 20 keys, 500 char values. |

### Request Examples

**cURL**

```bash
curl -X POST https://sandbox.api.example.com/v1/[resources] \
  -H "Authorization: Bearer sk_test_your_secret_key" \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 1000,
    "currency": "cad",
    "description": "Test [resource]"
  }'
```

**Node.js**

```javascript
const response = await fetch('https://sandbox.api.example.com/v1/[resources]', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer sk_test_your_secret_key',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    amount: 1000,
    currency: 'cad',
    description: 'Test [resource]',
  }),
});

const resource = await response.json();
console.log(resource.id);
```

**Python**

```python
import requests

response = requests.post(
    "https://sandbox.api.example.com/v1/[resources]",
    headers={
        "Authorization": "Bearer sk_test_your_secret_key",
        "Content-Type": "application/json",
    },
    json={
        "amount": 1000,
        "currency": "cad",
        "description": "Test [resource]",
    },
)

resource = response.json()
print(resource["id"])
```

### Response

Returns the created [resource] object.

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier for the created [resource]. |
| `object` | string | `"[resource]"` |
| `status` | string | `"pending"` on creation. |

```json
{
  "id": "prefix_abc123def456",
  "object": "[resource]",
  "created_at": 1700000000,
  "updated_at": 1700000000,
  "status": "pending",
  "amount": 1000,
  "currency": "cad",
  "description": "Test [resource]",
  "metadata": {}
}
```

### Errors

| Code | HTTP Status | Description | Resolution |
|------|------------|-------------|------------|
| `invalid_amount` | 400 | Amount must be a positive integer. | Ensure `amount` is greater than 0 and is an integer (cents, not dollars). |
| `invalid_currency` | 400 | Currency code not supported. | Use a supported three-letter ISO currency code (e.g., `cad`, `usd`). |
| `authentication_failed` | 401 | Invalid or missing API key. | Check your API key is correct and included in the `Authorization` header. |
| `rate_limit_exceeded` | 429 | Too many requests. | Wait for the `X-RateLimit-Reset` window and implement exponential backoff. |

---

## Retrieve a [Resource]

Retrieves an existing [resource] by its ID.

```
GET /v1/[resources]/{id}
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | **Required** | The [resource] ID (path parameter). |

### Request Examples

**cURL**

```bash
curl https://sandbox.api.example.com/v1/[resources]/prefix_abc123def456 \
  -H "Authorization: Bearer sk_test_your_secret_key"
```

**Node.js**

```javascript
const response = await fetch(
  'https://sandbox.api.example.com/v1/[resources]/prefix_abc123def456',
  {
    headers: {
      'Authorization': 'Bearer sk_test_your_secret_key',
    },
  }
);

const resource = await response.json();
console.log(resource.status);
```

**Python**

```python
import requests

response = requests.get(
    "https://sandbox.api.example.com/v1/[resources]/prefix_abc123def456",
    headers={"Authorization": "Bearer sk_test_your_secret_key"},
)

resource = response.json()
print(resource["status"])
```

### Response

Returns the [resource] object.

```json
{
  "id": "prefix_abc123def456",
  "object": "[resource]",
  "created_at": 1700000000,
  "updated_at": 1700000000,
  "status": "active",
  "amount": 1000,
  "currency": "cad",
  "description": "Test [resource]",
  "metadata": {}
}
```

### Errors

| Code | HTTP Status | Description | Resolution |
|------|------------|-------------|------------|
| `not_found` | 404 | No [resource] with that ID exists. | Verify the ID is correct and belongs to your account. |
| `authentication_failed` | 401 | Invalid or missing API key. | Check your API key. |

---

## Update a [Resource]

Updates an existing [resource]. Only provided parameters are changed.

```
PATCH /v1/[resources]/{id}
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | **Required** | The [resource] ID (path parameter). |
| `description` | string | Optional | Updated description. Max 500 characters. |
| `metadata` | object | Optional | Updated key-value pairs. Set a key to `null` to remove it. |

### Request Examples

**cURL**

```bash
curl -X PATCH https://sandbox.api.example.com/v1/[resources]/prefix_abc123def456 \
  -H "Authorization: Bearer sk_test_your_secret_key" \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Updated description",
    "metadata": {"order_id": "ord_789"}
  }'
```

**Node.js**

```javascript
const response = await fetch(
  'https://sandbox.api.example.com/v1/[resources]/prefix_abc123def456',
  {
    method: 'PATCH',
    headers: {
      'Authorization': 'Bearer sk_test_your_secret_key',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      description: 'Updated description',
      metadata: { order_id: 'ord_789' },
    }),
  }
);

const resource = await response.json();
console.log(resource.updated_at);
```

**Python**

```python
import requests

response = requests.patch(
    "https://sandbox.api.example.com/v1/[resources]/prefix_abc123def456",
    headers={
        "Authorization": "Bearer sk_test_your_secret_key",
        "Content-Type": "application/json",
    },
    json={
        "description": "Updated description",
        "metadata": {"order_id": "ord_789"},
    },
)

resource = response.json()
print(resource["updated_at"])
```

### Response

Returns the updated [resource] object.

```json
{
  "id": "prefix_abc123def456",
  "object": "[resource]",
  "created_at": 1700000000,
  "updated_at": 1700000100,
  "status": "active",
  "amount": 1000,
  "currency": "cad",
  "description": "Updated description",
  "metadata": {"order_id": "ord_789"}
}
```

### Errors

| Code | HTTP Status | Description | Resolution |
|------|------------|-------------|------------|
| `not_found` | 404 | No [resource] with that ID exists. | Verify the ID. |
| `invalid_status` | 400 | Cannot update a [resource] in `completed` or `failed` status. | Only `pending` and `active` [resources] can be updated. |

---

## List [Resources]

Returns a paginated list of [resources].

```
GET /v1/[resources]
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `limit` | integer | Optional | Number of results per page. Default: 10, max: 100. |
| `starting_after` | string | Optional | Cursor for forward pagination. Pass the `id` of the last item. |
| `ending_before` | string | Optional | Cursor for backward pagination. Pass the `id` of the first item. |
| `status` | string | Optional | Filter by status: `pending`, `active`, `completed`, `failed`. |
| `created_at[gte]` | integer | Optional | Filter by creation date (Unix timestamp, inclusive). |
| `created_at[lte]` | integer | Optional | Filter by creation date (Unix timestamp, inclusive). |

### Request Examples

**cURL**

```bash
curl "https://sandbox.api.example.com/v1/[resources]?limit=10&status=active" \
  -H "Authorization: Bearer sk_test_your_secret_key"
```

**Node.js**

```javascript
const params = new URLSearchParams({ limit: '10', status: 'active' });
const response = await fetch(
  `https://sandbox.api.example.com/v1/[resources]?${params}`,
  {
    headers: {
      'Authorization': 'Bearer sk_test_your_secret_key',
    },
  }
);

const list = await response.json();
console.log(`Found ${list.data.length} [resources]`);
```

**Python**

```python
import requests

response = requests.get(
    "https://sandbox.api.example.com/v1/[resources]",
    headers={"Authorization": "Bearer sk_test_your_secret_key"},
    params={"limit": 10, "status": "active"},
)

list_response = response.json()
print(f"Found {len(list_response['data'])} [resources]")
```

### Response

Returns a list object with a `data` array of [resource] objects.

```json
{
  "object": "list",
  "data": [
    {
      "id": "prefix_abc123def456",
      "object": "[resource]",
      "status": "active",
      "amount": 1000,
      "currency": "cad"
    }
  ],
  "has_more": true,
  "url": "/v1/[resources]"
}
```

### Pagination

Use cursor-based pagination for stable results:

```bash
# First page
curl "https://sandbox.api.example.com/v1/[resources]?limit=10" \
  -H "Authorization: Bearer sk_test_your_secret_key"

# Next page (use the last item's ID)
curl "https://sandbox.api.example.com/v1/[resources]?limit=10&starting_after=prefix_abc123def456" \
  -H "Authorization: Bearer sk_test_your_secret_key"
```

---

## Delete a [Resource]

Permanently deletes a [resource]. This cannot be undone.

```
DELETE /v1/[resources]/{id}
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | **Required** | The [resource] ID (path parameter). |

### Request Examples

**cURL**

```bash
curl -X DELETE https://sandbox.api.example.com/v1/[resources]/prefix_abc123def456 \
  -H "Authorization: Bearer sk_test_your_secret_key"
```

**Node.js**

```javascript
const response = await fetch(
  'https://sandbox.api.example.com/v1/[resources]/prefix_abc123def456',
  {
    method: 'DELETE',
    headers: {
      'Authorization': 'Bearer sk_test_your_secret_key',
    },
  }
);

// 204 No Content on success
console.log(response.status);
```

**Python**

```python
import requests

response = requests.delete(
    "https://sandbox.api.example.com/v1/[resources]/prefix_abc123def456",
    headers={"Authorization": "Bearer sk_test_your_secret_key"},
)

# 204 No Content on success
print(response.status_code)
```

### Response

Returns `204 No Content` on success. No response body.

### Errors

| Code | HTTP Status | Description | Resolution |
|------|------------|-------------|------------|
| `not_found` | 404 | No [resource] with that ID exists. | Verify the ID. |
| `cannot_delete` | 400 | [Resource] in `active` status cannot be deleted. | Cancel or complete the [resource] before deleting. |

---

## Related Endpoints

| Endpoint | Description |
|----------|-------------|
| `POST /v1/[related-resource]` | Create a related resource |
| `GET /v1/events?type=[resource].*` | List events for this resource type |
