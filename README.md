# 30daysofcode

## data persistence

### endpoint

`https://data-persistence.heroku.com`

### usage

`/polulate GET 201 created`

```json
{
  "message": "data store populated",
  "data": [
    {
      "id": "user_id",
      "name": "user's name",
      "username": "user's username",
      "email": "user_email"
    },
    {
      "id": "user_id",
      "name": "user's name",
      "username": "user's username",
      "email": "user_email"
    }
  ]
}
```

`/delete DELETE 200 ok`

```json
{
  "message": "resource deleted",
  "deleted user": [
    {
      "id": "user_id",
      "name": "user's name",
      "username": "user's username",
      "email": "user_email"
    }
  ]
}
```

`/signup POST 201 created`

```json
{
  "message": "new user created",
  "created user": {
    "username": "user's username",
    "name": "user's name",
    "email": "user's email"
  } 
}
```

### db credentials
- username = bc1b301810a782
- password = a9287c9e
- host = us-cdbr-east-06.cleardb.net