# Postbot Siemen is a Twitter bot based on Postbode Siemen (Zaai). He can:
#   1) Give the translation of any word to the secret code of 'Wokkie Tokkie' 
#   2) Send people who are bored YT links
#   3) Posts a quote every week 

from data import getData, setData

import tweets
from config import create_api

import random
from datetime import datetime, timedelta
from timeloop import Timeloop

tl = Timeloop()

# Main function
print("Started!")
api = create_api()
print("Connected!")
since_id = getData('lastTweet')
last_quote = getData('lastQuote')


@tl.job(interval=timedelta(seconds=15))
def MentionsJob():
    global since_id
    since_id = tweets.reply_to_mentions(api, since_id)
    
        
@tl.job(interval=timedelta(hours=5))
def tweet_quote(api):
    # Select a random quote
    with open("data/siemen.txt") as f:
        lines = f.readlines()
        oldQuote = getData('lastQuote')
        tweet = api.update_status(random.choice(x for x in lines if x != oldQuote))
        setData('lastQuote', tweet.text)

tl.start(block=True)
