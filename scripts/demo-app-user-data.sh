#!/bin/bash

# User Data

curl -O https://bootstrap.pypa.io/get-pip.py
python get-pip.py 

yum install -y git

mkdir -p /var/www/demo

pip install click
pip install Flask
pip install itsdangerous
pip install Jinja2
pip install MarkupSafe
pip install nltk
pip install oauthlib
pip install requests
pip install requests-oauthlib
pip install six
pip install textblob
pip install tweepy --ignore-installed six requests
pip install Werkzeug
pip install boto3

cd /var/www/demo
git clone https://github.com/gofornaman/Real-Time-Sentiment-Analysis.git ./

# Run app
cd /var/www/demo
FLASK_APP=app.py CONFIG=app.settings flask run --host=0.0.0.0 --port=80
