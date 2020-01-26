# atlas-api

## Overview

## Running locally

```
python3 -m venv env
. env/bin/activate
```

Install requirements
`pip install -r requirements.txt`

### Set up MySQL

Download MySQL Community Server: https://dev.mysql.com/downloads/mysql/

Add mysql to your $PATH:
```
echo 'export PATH="/usr/local/mysql/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile
```

Connect to mysql through the command line (prompted for password):
```
mysql -u<user> -p
```

Add a `.env` file under `/project/project` with the database env vars `MYSQL_USER` and `MYSQL_PASSWORD`

### Django and MySQL

Change to the project directory to make all database migrations and to run the server
`cd project`

View a changelog of database models changes:
`python manage.py makemigrations`

Commit database changes:
`python manage.py migrate`

To run the Django development server:
`python manage.py runserver`

To create an admin superuser to use the /admin dashboard:
`python manage.py createsuperuser`

If you get an error about `mysqlclient 1.3.13 or newer is required; you have 0.9.3`, this is a bug, you need to edit this file:
`env/lib/python3.7/site-packages/django/db/backends/mysql/base.py` and search for this block:

```
if version < (1, 3, 13):
    raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
```
and make it look like this:

```
if version < (1, 3, 13):
    pass
    # raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
```

