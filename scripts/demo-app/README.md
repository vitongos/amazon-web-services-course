# Demo App

A real time sentiment analysis on tweets using Python, Flask-API, Gunicorn, Tweepy &amp; TextBlob

*Forked from a @gofornaman work*

## User data for EC2 provisioning

Check user data [here](https://github.com/vitongos/amazon-web-services-course/blob/master/scripts/demo-app-user-data.sh)

## Launch applicationas root on port 80

```console
root:~$ cd /var/www/demo
root:~$ FLASK_APP=app.py CONFIG=app.settings flask run --host=0.0.0.0 --port=80
```
