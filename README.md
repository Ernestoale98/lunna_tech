# Local

Copy .env.example to .env and fill SECRET_KEY,EMAIL_HOST_USER,EMAIL_HOST_PASSWORD
you can use [mailtrap.io](https://mailtrap.io/blog/django-send-email/) to catch emails

```bash
cp backend/.env.example backend/.env
```

### Run docker

```bash
docker-compose up
```

### Run migrations

```bash
docker exec -it lunna_tech-web-1 python3 manage.py migrate
```

### Create admin user

```bash
docker exec -it lunna_tech-web-1 python manage.py createsuperuser --email admin@example.com --username admin
```

### Usage in localhost

[Admin panel](http://127.0.0.1:8000/admin/login)

[API](http://127.0.0.1:8000/api)

# Real environment

Go to [Admin panel](https://lunnatech.herokuapp.com/admin/login) and login using:

```bash
username: admin
password: pass
```

go to users and create new user, next edit that user with real email and with
permissions Staff status and Superuser status, this is to receive emails

# Update product

Use
de [API Product Update](https://documenter.getpostman.com/view/10080431/2s93CLsDKE#f6859aea-1490-43ed-aa05-02d06da04425)
to receive notification about the changes in the product

### API Documentation with Postman

[Postman](https://documenter.getpostman.com/view/10080431/2s93CLsDKE)

# Architecture design

When I work with Django I use the Django applications with the Domain-Driven Design bases,
each one of the applications contains a domain with a single layer of the business model, so although it is a monolithic
project, we have a good code structure by containing everything in domains. If in the future it is necessary to migrate
to a microservices project, each of the domains already created would be a microservice since with Domain-Driven Design
it is much easier to identify the boundary context of each of the microservices.
