# Credits, Notes, and Reference

## Flask

  + http://flask.pocoo.org/
  + http://flask.pocoo.org/docs/1.0/installation/#create-an-environment
  + http://flask.pocoo.org/docs/1.0/quickstart/
  + http://flask.pocoo.org/docs/1.0/quickstart/#debug-mode

## Virtual Environments

  + https://docs.python.org/3/library/venv.html#module-venv

## Deployment Environments (Heroku)

  + http://flask.pocoo.org/docs/1.0/deploying/#deployment
  + https://devcenter.heroku.com/articles/getting-started-with-python#introduction
  + https://devcenter.heroku.com/articles/python-support
  + https://devcenter.heroku.com/articles/git
  + https://help.heroku.com/W23OAFGK/why-am-i-seeing-couldn-t-find-that-process-type-when-trying-to-scale-dynos
  + https://devcenter.heroku.com/articles/procfile

## Package Dependencies (Pipenv)

  + https://github.com/pypa/pipfile
  + https://docs.pipenv.org/
  + https://docs.pipenv.org/install/#installing-pipenv
  + https://stackoverflow.com/questions/990754/how-to-leave-exit-deactivate-a-python-virtualenv







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

Deploy:

```sh
git push heroku master
#> error: No default language could be detected for this app.
#> HINT: This occurs when Heroku cannot detect the buildpack to use for this application automatically.
#> See https://devcenter.heroku.com/articles/buildpacks
```

Fix deployment issues (need `Pipfile` or `requirements.txt` to signal that this is a python app):

```sh
pip3 install pipenv # also available: brew install pipenv
pipenv install
```

Try again to deploy:

```sh
git push heroku deploy:master # (from a "deploy" branch where I had been making changes)
heroku open #> https://nyu-info-2335-flask-test.herokuapp.com/
#> Application Error
```

Deploy succeeded but there is an application error, so check the logs:

```sh
heroku logs
#> No web processes running
```

Start a web process:

```sh
heroku ps #> No dynos on ⬢ nyu-info-2335-flask-test
heroku ps:scale web=1 #> Couldn't find that process type.
# hmm...
touch Procfile # and paste inside... web: python app.py
```

Try to deploy again:

```sh
git push heroku deploy:master
heroku open
heroku logs #> ModuleNotFoundError: No module named 'flask'
# oh that's right because its not in the Pipfile...
pipenv install flask
```

Try to deploy again:

```sh
git push heroku deploy:master
heroku open
heroku logs #> ModuleNotFoundError: No module named 'flask'
# hmmm let's try using a gunicorn server
pipenv install gunicorn
gunicorn app:app # then visit on localhost:8000 to verify
```

Try to deploy again:

```sh
git push heroku deploy:master
heroku open

```
