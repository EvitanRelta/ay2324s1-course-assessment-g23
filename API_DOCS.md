# Makeshift docs for all APIs

# Todo
- For each API, write the error payload format.
- Implement/Ensure all APIs follow the status codes.

<br>

# API format
All the APIs have the form: `/api/[SERVICE_NAME]/[API_PATH]`

For example:
- Frontend: `GET /api/questions/questions_all` where:
  - `/api` indicates request to backend
  - `/questions` indicates request to "questions" service
  - `/questions_all` is the API-endpoint in "questions" service
- Which maps to `GET /questions_all` in questions-service


<br>

<br>

# API-endpoints

`GET` and `DELETE` HTTP requests will not have any request-payload.

"Protection" can be either:
- None (anyone can access)
- Must be logged in
- Must be maintainer (have "maintainer" role)
- Must be same user or maintainer
  (for APIs with `user_id` like `"/users/{user_id}"`, `user_id` must belong to user)

<br>

## Users service

Prefix for API path: `/api/users`

<br>

### `POST /users`
Signup/Creates a new user.

Protection: None

Request payload:
```json
{
    "username": "string",
    "password": "string",
    "email": "string",
}
```

Response payload:
```json
{
    "message": "Signup message",
}
```

Cases & status codes:
- Success: `201 Created`
- Error:
    - Invalid data: `400 Bad Request`
    - Username/email already exists: `409 Conflict`

<br>

### `GET /user_me`
Get user details of the currently logged-in user.

Protection: Must be logged in

Response payload:
```json
{
    "user_id": "string",
    "username": "string",
    "email": "string",
    "role": "normal or maintainer",
}
```

Cases & status codes:
- Success: `200 OK`
- Error:
    - Not logged in / Invalid JWT token: `401 Unauthorized`
    - User not found: `404 Not Found`

<br>

### `GET /users/{user_id}`
Get user details of a specific user by their user ID.

Protection: Must be logged in

Response payload:
```json
{
    "user_id": "string",
    "username": "string",
    "email": "string",
    "role": "normal or maintainer",
}
```

Cases & status codes:
- Success: `200 OK`
- Error:
    - Not logged in / Invalid JWT token: `401 Unauthorized`
    - User not found: `404 Not Found`

<br>

### `GET /users_all`
Get list of all users' details.

Protection: Must be maintainer

Response payload:
```json
[
    {
        "user_id": "string",
        "username": "string",
        "email": "string",
        "role": "normal or maintainer",
    },
]
```

Cases & status codes:
- Success: `200 OK`
- Error:
    - Not logged in / Invalid JWT token: `401 Unauthorized`
    - Not a maintainer: `403 Forbidden`

<br>

### `DELETE /users_all`
Delete all users.

Protection: Must be maintainer

Response payload:
```json
{
    "message": "Delete all users message",
}
```

Cases & status codes:
- Success: `200 OK`
- Error:
    - Not logged in / Invalid JWT token: `401 Unauthorized`
    - Not a maintainer: `403 Forbidden`

<br>

### `DELETE /users/{user_id}`
Delete specific user by their user ID.

Protection: Must be same user or maintainer

Response payload:
```json
{
    "message": "Delete user message",
}
```

Cases & status codes:
- Success: `200 OK`
- Error:
    - Not logged in / Invalid JWT token: `401 Unauthorized`
    - Not same user nor maintainer: `403 Forbidden`
    - User not found: `404 Not Found`
    - Attempting to delete last maintainer: `409 Conflict`

<br>

### `PUT /users/{user_id}`
Update a specific user's details.

Protection: Must be same user or maintainer

Request payload:
```json
{
    "username": "string (OPTIONAL)",
    "password": "string (OPTIONAL)",
    "email": "string (OPTIONAL)",
}
```

Response payload:
```json
{
    "message": "Update user message",
}
```

Cases & status codes:
- Success:
    - With some or all fields: `200 OK`
    - With no fields: `200 OK`
- Error:
    - Not logged in / Invalid JWT token: `401 Unauthorized`
    - Not same user nor maintainer: `403 Forbidden`
    - User not found: `404 Not Found`
    - Invalid data: `400 Bad Request`
    - Username/email already exists: `409 Conflict`

<br>

### `PUT /users_role/{user_id}`
Update a specific user's role.

Protection: Must be maintainer

Request payload:
```json
{
    "role": "string",
}
```

Response payload:
```json
{
    "message": "Update user message",
}
```

Cases & status codes:
- Success: `200 OK`
- Error:
    - Not logged in / Invalid JWT token: `401 Unauthorized`
    - Not a maintainer: `403 Forbidden`
    - User not found: `404 Not Found`
    - Invalid role: `400 Bad Request`
    - Attempting to revoke permission of last maintainer: `409 Conflict`

<br>

### `POST /token`
Login a user. (sets JWT `access_token` & `refresh_token` cookies)

Protection: None

Request payload:
```json
{
    "username": "string",
    "password": "string",
}
```

Response payload:
```json
{
    "message": "string",
}
```

Cases & status codes:
- Success: `200 OK`
- Error:
    - Invalid credentials: `401 Unauthorized`

<br>

### `DELETE /token`
Logout a user. (unsets JWT `access_token` & `refresh_token` cookies)

Protection: None

Response payload: None

Cases & status codes:
- Always: `204 No Content`

<br>

### `GET /refresh`
Refresh JWT access token. (gets new `access_token` cookie using `refresh_token` cookie)

Protection: Must be logged in

Response payload: None

Cases & status codes:
- Success: `204 No Content`
- Error:
    - Not logged in / Invalid JWT token: `401 Unauthorized`
    - Invalid refresh token: `403 Forbidden`

<br>

## Questions service

Prefix for API path: `/api/questions`

<br>

### `POST /questions`
Creates a new question.

Protection: Must be maintainer

Request payload:
```json
{
    "title": "string",
    "description": "string",
    "category": "string",
    "complexity": "string",
}
```

Response payload:
```json
{
    "message": "string",
}
```

Cases & status codes:
- Success: `201 Created`
- Error:
    - Not logged in / Invalid JWT token: `401 Unauthorized`
    - Not a maintainer: `403 Forbidden`
    - Invalid data: `400 Bad Request`
    - Title already exists: `409 Conflict`

<br>

### `GET /questions/{question_id}`
Get specific question by its question ID.

Protection: Must be logged in

Response payload:
```json
{
    "question_id": "string",
    "title": "string",
    "description": "string",
    "category": "string",
    "complexity": "string",
}
```

Cases & status codes:
- Success: `200 OK`
- Error:
    - Not logged in / Invalid JWT token: `401 Unauthorized`
    - Question not found: `404 Not Found`

<br>

### `GET /questions_all`
Get list of all questions.

Protection: Must be logged in

Response payload:
```json
[
    {
        "question_id": "string",
        "title": "string",
        "description": "string",
        "category": "string",
        "complexity": "string",
    },
]
```

Cases & status codes:
- Success: `200 OK`
- Error:
    - Not logged in / Invalid JWT token: `401 Unauthorized`

<br>

### `PUT /questions`
Update a specific question by its question ID (which is in the payload).

Protection: Must be maintainer

Request payload:
```json
{
    "question_id": "string",
    "title": "string",
    "description": "string",
    "category": "string",
    "complexity": "string",
}
```

Response payload:
```json
{
    "message": "Update question message",
}
```

Cases & status codes:
- Success: `200 OK`
- Error:
    - Not logged in / Invalid JWT token: `401 Unauthorized`
    - Not a maintainer: `403 Forbidden`
    - Question not found: `404 Not Found`
    - Invalid data: `400 Bad Request`
    - Title already exists: `409 Conflict`

<br>

### `DELETE /questions/{question_id}`
Delete a question by its question ID.

Protection: Must be maintainer

Response payload:
```json
{
    "message": "Delete question message",
}
```

Cases & status codes:
- Success: `200 OK`
- Error:
    - Not logged in / Invalid JWT token: `401 Unauthorized`
    - Not a maintainer: `403 Forbidden`
    - Question not found: `404 Not Found`
