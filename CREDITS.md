# Credits, Notes, and Reference

## Flask

  + http://flask.pocoo.org/
  + http://flask.pocoo.org/docs/1.0/installation/#create-an-environment
  + http://flask.pocoo.org/docs/1.0/quickstart/

## Virtual Environments

  + https://docs.python.org/3/library/venv.html#module-venv

## Deployment Environments

  + http://flask.pocoo.org/docs/1.0/deploying/#deployment
  + https://devcenter.heroku.com/articles/getting-started-with-python#introduction

## Dev Process

Setup repo:

```sh
python3 --version
#> Python 3.6.5
mkdir my-flask-app
cd my-flask-app
```

Generate new virtual env:

```sh
python3 -m venv venv
. venv/bin/activate
# subsequent commands which start with (venv) denote commands run from inside the virtual env.
```

Install flask:

```sh
(venv) pip3 install flask
```

Run a local web server:

```sh
(venv) flask run
```

## Deployment Process

Create a new heroku app:

```sh
heroku login
heroku create
heroku apps:rename nyu-info-2335-flask-test -a my-app
git remote -v
#> heroku	https://git.heroku.com/nyu-info-2335-flask-test.git (fetch)
#> heroku	https://git.heroku.com/nyu-info-2335-flask-test.git (push)
```
