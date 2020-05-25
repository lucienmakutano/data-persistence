# 30daysofcode

## data persistence

### endpoint

`https://data-persistence.heroku.com`

### usage

`/polulate GET 201 created`

```json
{
  "message": "data store populated"
}
```

`/delete DELETE 200 ok`

```json
{
  "message": "resource deleted"
}
```

`/signup POST 201 created`

```json
{
  "message": "new user created"
}
```

### db credentials
- username = bc1b301810a782
- password = a9287c9e
- host = us-cdbr-east-06.cleardb.net
- port = 3306
