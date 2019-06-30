# Demo App

A real time sentiment analysis on tweets using Python, Flask-API, Gunicorn, Tweepy &amp; TextBlob

*Forked from a @gofornaman work*

## User data for EC2 provisioning

```bash
#!/bin/bash

curl -O https://bootstrap.pypa.io/get-pip.py
python get-pip.py

yum install -y git
amazon-linux-extras install postgresql10 vim epel -y

mkdir -p /var/www/demo

pip install -r requirements.txt

cd /var/www/demo
git clone https://github.com/vitongos/amazon-web-services-course /tmp/demo
mv /tmp/demo/scripts/demo-app/* /var/www/demo/
```

## Launch application on port 80

```console
root:~$ cd /var/www/demo
root:~$ FLASK_APP=app.py flask run
```
