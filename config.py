from dotenv import load_dotenv
load_dotenv()

import tweepy
import os
from flask import Flask

# Authenticate to Twitter and create API object
def create_api():
    #app = Flask(__name__)
    #app.run(host= '0.0.0.0', port=os.getenv('PORT'))

    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)

    api.verify_credentials()

    return api