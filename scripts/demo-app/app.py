import os
import boto3
from flask import Flask, request, render_template, jsonify
from twitter import TwitterClient

app = Flask(__name__)
# Setup the client <query string, retweets_only bool, with_sentiment bool>
api = TwitterClient('@gofornaman')
app.config.from_object('app.settings')

def strtobool(v):
    return v.lower() in ["yes", "true", "t", "1"]


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/s3', methods = ['POST'])
def s3():
    s3 = boto3.resource(
        's3',
        region_name='eu-west-1',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=ACCESS_SECRET
    )
    bucket = S3_BUCKET
    folder = S3_FOLDER
    body = request.get_json()
    s3.Object(bucket, folder + '/' + body['file']).put(Body=body['content'])

@app.route('/tweets')
def tweets():
        retweets_only = request.args.get('retweets_only')
        api.set_retweet_checking(strtobool(retweets_only.lower()))
        with_sentiment = request.args.get('with_sentiment')
        api.set_with_sentiment(strtobool(with_sentiment.lower()))
        query = request.args.get('query')
        api.set_query(query)

        tweets = api.get_tweets()
        return jsonify({'data': tweets, 'count': len(tweets)})


port = int(os.environ.get('PORT', 80))
app.run(host="0.0.0.0", port=port, debug=True)
