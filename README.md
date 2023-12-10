### to build and run via Docker
```commandline
cd app
docker-compose up -d --build
```

copy `dist.env.dev` to `.env.dev` file

### to migrate
```commandline
docker-compose exec web python manage.py flush --no-input
docker-compose exec web python manage.py migrate
```

### to connect to database with credentials
via `docker-compose exec` command
```commandline
docker-compose exec db psql --username=hello_django --dbname=hello_django_dev
```
