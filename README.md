GrowTweet
=========

It is a simple application which uses Twitter API. It allows users to see their “second line” followers, in other words - followers, of their followers.

### Common scenario:
- I go to “/” page
- I see “Connect Twitter account” button
- I press “Connect Twitter account” button
- I see Twitter popup, I follow oAuth flow authorizing app
- I get redirected to “/followers/followers” page
- There is AJAX request to the server and after a while we get table with data
- I see a list of my “2nd line” followers. Each contains
- A Twitter handle, like “@madonna”
- A number of my followers, that this person follows (example, Bob and Rick follow me, Andrew follows both of them, the number is 2). 

### API

API details can be viewed under URL `/api/`. Special library called Swagger handles it. 

**1. get-followers**
A browser calls AJAX request under URL `/getfollowers/`. It takes new 'followers of my followers' data from Twitter server via the Twitter's API.
For the call some variables are taken from the browsers session.

**2. current-followers**
URL request under `/currentfollowers/{user_name}/` with GET method returns JSON data with the latest 'followers of my followers' for the user_name.


Installation
============

GrowTweet is a Django project.
It can be deployed with uWSGI: https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/uwsgi/

Application requires Python 3.5 and Django 1.11

All requirements are stored in `requirements.txt` file and can be install with:
```
pip -r requirements.txt
```

You must copy `config_example.ini` file to `config.ini` and change its values to your own.

When application is set up and configured (check Configuration section)
you can create database and copy static files with commands:
```
python manage.py migrate
python manage.py collectstatic --noinput
```

Now the easiest way to start the server is to use Django runserver
```
python manage.py runserver
```

For more information refer to Django documentation.

Configuration
=============

All advanced configuration options are stored in `growtweet/settings.py`.
It is recommended to make any changes not directly in the `settings.py` file but in created locally `growtweet/local_settings.py`.
The file will override the parameters from the `setting.py` file.

Most of the settings are standard `Django` settings. The most important are:

- DEBUG - when turned off (False) optimizations are turn on and debug info aren't printed.
- DATABASES - configuration of database engine. Default is SQLite.

Check Django docs for more info: https://docs.djangoproject.com/en/1.11/ref/settings/#databases

Tox
===

You can run unit tests and flake8 by simply running command `tox`.
It will check PEP8 and run unit tests.

If you run
```
tox coverage html
```

You can generate HTML files with unit tests coverage statistics. 
