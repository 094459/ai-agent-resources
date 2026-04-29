---
inclusion: fileMatch
fileMatchPattern: "api/**,**/handlers/**,*.py,**/routes/**"
---

# API Design Conventions

## REST API Standards

### URL Patterns
- Use nouns, not verbs: `/users`, `/orders` — never `/getUsers`
- Plural resource names: `/items`, `/documents`
- Nested resources for relationships: `/users/{userId}/orders`
- Use kebab-case for multi-word paths: `/risk-scores`
- Version APIs in the path: `/v1/users`

### HTTP Methods
- `GET` — Read (no side effects, cacheable)
- `POST` — Create new resource
- `PUT` — Full update (replace entire resource)
- `PATCH` — Partial update
- `DELETE` — Remove resource

### Response Format
All API responses must follow this structure:
```json
{
  "data": {},
  "meta": {
    "requestId": "uuid",
    "timestamp": "ISO-8601"
  }
}
```

### Error responses:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human-readable description",
    "details": []
  },
  "meta": {
    "requestId": "uuid",
    "timestamp": "ISO-8601"
  }
}
```

### HTTP Status Codes

- 200 — Success (GET, PUT, PATCH)
- 201 — Created (POST)
- 204 — No Content (DELETE)
- 400 — Bad Request (validation errors)
- 401 — Unauthorized (missing/invalid auth)
- 403 — Forbidden (valid auth, insufficient permissions)
- 404 — Not Found
- 409 — Conflict (duplicate resource)
- 429 — Too Many Requests (rate limited)
- 500 — Internal Server Error (never expose stack traces)

### Input Validation

- Validate ALL inputs at the API boundary. Never trust client data.
- Use schema validation: Pydantic (Python) or Zod/Joi (Node.js)
- Return specific validation errors, not generic "bad request"
- Sanitize inputs to prevent injection attacks

### Frontend-Backend Contract

- Define API contracts using OpenAPI/Swagger specifications
- Frontend and backend must agree on the contract before implementation
- Use TypeScript types or Pydantic models as the single source of truth
- Never return more data than the frontend needs (minimize payload)

### CORS

- Configure CORS explicitly — never use * for allowed origins in production. Specify exact allowed origins, methods, and headers.
- Set appropriate max-age for preflight caching
