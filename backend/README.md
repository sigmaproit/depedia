A lite weight service to fix the version update issue in large scale projects for its dependencies

steps to run
```
$ virtualenv venv  
$ source venv/bin/activate  
$ pip install -r requirements.txt

$ export APP_SETTINGS="config.DevelopmentConfig"
$ export DATABASE_URL="postgresql://farid02:mma@localhost/flaskdb"
```
set up migrations
```
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```
run celery

```

celery -A app.celery  worker -l info

```