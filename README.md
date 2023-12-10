### to build and run via Docker
```commandline
cd app
docker-compose up -d --build
```

### to migrate
```commandline
docker-compose exec web python manage.py migrate --noinput
```

### to connect to database with credentials
via `docker-compose exec` command
```commandline
docker-compose exec db psql --username=hello_django --dbname=hello_django_dev
```
