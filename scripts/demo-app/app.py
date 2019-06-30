import os
import boto3
import psycopg2
from flask import Flask, request, render_template, jsonify
from twitter import TwitterClient

app = Flask(__name__)
# Setup the client <query string, retweets_only bool, with_sentiment bool>
api = TwitterClient('@gofornaman')
app.config.from_envvar('CONFIG')

def strtobool(v):
    return v.lower() in ["yes", "true", "t", "1"]


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/s3', methods = ['POST'])
def s3():
    s3 = boto3.client(
        's3',
        region_name='eu-west-1',
        aws_access_key_id=app.config['ACCESS_KEY'],
        aws_secret_access_key=app.config['ACCESS_SECRET']
    )
    bucket = app.config['S3_BUCKET']
    folder = app.config['S3_FOLDER']
    body = request.get_json()
    s3.put_object(Bucket=bucket, Key=folder + '/' + body['file'], Body=body['content'])
    return jsonify({'result': 'OK'})

@app.route('/tweets')
def tweets():
        retweets_only = request.args.get('retweets_only')
        api.set_retweet_checking(strtobool(retweets_only.lower()))
        with_sentiment = request.args.get('with_sentiment')
        api.set_with_sentiment(strtobool(with_sentiment.lower()))
        query = request.args.get('query')
        api.set_query(query)

        tweets = api.get_tweets()
        store(tweets)
        return jsonify({'data': tweets, 'count': len(tweets)})


def store(tweets):
    connection = None
    try:
        connection = psycopg2.connect(user=app.config['RDS_USER'],
                                        password=app.config['RDS_PASSWORD'],
                                        host=app.config['RDS_HOST'],
                                        port=app.config['RDS_PORT'],
                                        dbname=app.config['RDS_DATABASE'])
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO search (sentiment, message, user_name) VALUES (%s,%s,%s)"""
        for record in tweets:
            print(record)
            cursor.execute(postgres_insert_query, record)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into search table")
    except (Exception, psycopg2.Error) as error :
        print("Failed to insert record into search table", error)
    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

port = int(os.environ.get('PORT', 80))
app.run(host="0.0.0.0", port=port, debug=False)
