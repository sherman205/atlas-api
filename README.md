# atlas-api

## Overview

## Running locally

```
python3 -m venv env
. env/bin/activate
```

Install requirements
`pip install -r requirements.txt`

### Set up mysql

Download MySQL Community Server: https://dev.mysql.com/downloads/mysql/

Add mysql to your $PATH:
```
echo 'export PATH="/usr/local/mysql/bin:$PATH"' >> ~/.bash_profile
source .~/.bash_profile
```

Connect to mysql through the command line:
```
mysql -u <user> -p
```

Add a `.env` file under `/project` with the database env vars `MYSQL_USER` and `MYSQL_PASSWORD`

### Running Django

To run the Django development server:

`python manage.py runserver`

