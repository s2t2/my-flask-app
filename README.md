# My Flask App

## Installation

Prerequisites: Install Git and Python (~> 3.6.5) and Pipenv (~> 11.10.1).

Install source code:

```sh
git clone git@github.com:s2t2/my-flask-app.git
cd my-flask-app/
```

Install package dependencies:

```sh
pipenv install
```

## Usage

The following commands assume you are running them inside a pipenv shell. Get into one by typing `pipenv shell`.

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
