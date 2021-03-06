# Prerequisites

- Python 3.9
- Pipenv
- Docker
- Docker Compose

# How to run?

Confidential keys have to be loaded as environment variables.


## First run

```
$ docker-compose up -d db
$ cd backend
$ pipenv install --dev
$ pipenv shell
$ python manage.py createsuperuser
$ python manage.py runserver
```

## Development

### Database

```
$ docker-compose up -d db
```

### Backend

```
$ cd backend
$ pipenv install --dev
$ pipenv shell
$ python manage.py runserver
```

## Production

```
$ docker-compose up -d --build
```
## Manage db

```
$ docker exec -it <container_id> psql -U <database> -W <user>
```

