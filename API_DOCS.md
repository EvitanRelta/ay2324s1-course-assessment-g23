# Makeshift docs for all APIs

<br>

## API format
All the APIs have the form: `/api/[SERVICE_NAME]/[API_PATH]`

For example:
- Frontend: `GET /api/questions/questions_all` where:
  - `/api` indicates request to backend
  - `/questions` indicates request to "questions" service
  - `/questions_all` is the API-endpoint in "questions" service
- Which maps to `GET /questions_all` in questions-service


<br>

<br>

## API-endpoints

`GET` and `DELETE` HTTP requests will not have any request-payload.

"Protection" can be either:
- None (anyone can access)
- Must be logged in
- Must be maintainer (have "maintainer" role)
- Must be same user or maintainer
  (for APIs with `user_id` like `"/users/{user_id}"`, `user_id` must belong to user)

<br>

### Users service

Prefix for API path: `/api/users`

<br>

#### `POST /users`
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

<br>

#### `GET /user_me`
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

<br>

#### `GET /users/{user_id}`
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

<br>

#### `GET /users_all`
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

<br>

#### `DELETE /users_all`
Delete all users.

Protection: Must be maintainer

Response payload:
```json
{
    "message": "Delete all users message",
}
```

<br>

#### `DELETE /users/{user_id}`
Delete specific user by their user ID.

Protection: Must be same user or maintainer

Response payload:
```json
{
    "message": "Delete user message",
}
```


<br>

#### `PUT /users/{user_id}`
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

<br>

#### `PUT /users_role/{user_id}`
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


<br>

#### `POST /token`
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


<br>

#### `DELETE /token`
Logout a user. (unsets JWT `access_token` & `refresh_token` cookies)

Protection: None

Response payload: None


<br>

#### `GET /refresh`
Refresh JWT access token. (gets new `access_token` cookie using `refresh_token` cookie)

Protection: Must be logged in

Response payload: None


<br>

### Questions service

Prefix for API path: `/api/questions`

<br>

#### `POST /questions`
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


dependencies=[Depends(require_maintainer_role)])
async def create_question(r: CreateQuestionRequest) -> CreateQuestionResponse:
    question_id = str(uuid.uuid4())


<br>

#### `GET /questions/{question_id}`
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


<br>

#### `GET /questions_all`
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


<br>

#### `PUT /questions`
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


<br>

#### `DELETE /questions/{question_id}`
Delete a question by its question ID.

Protection: Must be maintainer

Response payload:
```json
{
    "message": "Delete question message",
}
```
