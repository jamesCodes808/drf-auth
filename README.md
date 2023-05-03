# Permissions & Postgresql

Django application using Django Rest Frameworks API Views and authentication.
Using Docker as containerization.
Using Postgresql as database

## Set up

```
$ python3 -m venv .venv
$ pip3 install requirements.txt
$ pip freeze > requirements.txt
$ docker compose up --build
```

When running you will be met with a `This site can't be reached` as the path
is `http://0.0.0.0:8000/`

Manually change it to
`http://localhost:8000/`

then to 

`http://localhost:8000/api/v1/games/`

to see API GUI

If met with errors, user might need to run migrations in the docker container and create a superuser to create 
objects from database models

```
# First shut down the docker container

$ docker compose up -d
$ docker compose run web python manage.py migrate
$ docker compose run web python manage.py createsuperuser
```

Now user can use following paths to perform CRUD after logging into superuser account

```
# Go to List View
http://localhost:8000/api/v1/games/

# Go to Create View
http://localhost:8000/api/v1/games/create

# Go to detail view (Update or Delete)
http://localhost:8000/api/v1/games/
```

## Shut down

```
$ ctrl+c
$ docker compose down
```