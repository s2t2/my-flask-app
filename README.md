# My Flask App

## Prerequisites

Requires:

  + Git
  + Python (~> 3.6.5) and Pipenv (~> 11.10.1).
  + PostgreSQL

Create a development environment database:

```sh
psql -c "CREATE DATABASE my_flask_app;"
```

## Installation

Install source code:

```sh
git clone git@github.com:s2t2/my-flask-app.git
cd my-flask-app/
```

Install package dependencies:

```sh
pipenv install
```

All following commands assume you are running them inside a pipenv shell:

```sh
pipenv shell
```

Migrate and seed the database:

```sh
python migrate.py
python seed.py
```

## Usage

Run webserver:

```sh
FLASK_ENV=development flask run # then visit localhost:5000 in a browser...
```

Run tests:

```sh
# todo
```

## Contributing

## Deploying

```sh
git push heroku mybranch:master # -a nyu-info-2335-flask-test
```
