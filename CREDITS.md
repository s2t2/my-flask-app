# Credits, Notes, and Reference

## Flask

  + http://flask.pocoo.org/
  + http://flask.pocoo.org/docs/1.0/installation/#create-an-environment
  + http://flask.pocoo.org/docs/1.0/quickstart/

## Virtual Environments

  + https://docs.python.org/3/library/venv.html#module-venv

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
