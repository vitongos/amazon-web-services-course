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

