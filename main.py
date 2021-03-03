# Postbot Siemen is a Twitter bot based on Postbode Siemen (Zaai). He can:
#   1) Give the translation of any word to the secret code of 'Wokkie Tokkie' 
#   2) Send people who are bored YT links
#   3) Posts a quote every week 

import datetime
from types import LambdaType

import tweets
from config import create_api
import random
from datetime import timedelta, date
from timeloop import Timeloop

tl = Timeloop()

# Main function
print("Started!")
api = create_api()
print("Connected!")

# retrieve lastTweet
statuses = api.home_timeline()
since_id = statuses[0].id
print("Last tweet: " + statuses[0].text)

def tweet_quote():
    # Select a random quote
    with open("data/siemen.txt") as f:
        lines = f.readlines()
        tweet = api.update_status(random.choice(lines))
        print('Sent quote: ' + tweet.text)

# send quote. Since Heroku is restarted every day (and 0-216 mins), and we want to tweet a quote every week,
# we'll check the date against a start date
startdate = date(2021,2,16)
d = (date.today() - startdate).days
if d % 7 == 0: # once in approx. 12 weeks, Siemen skips a week (depending on the random Heroku restart times)
    tweet_quote()


@tl.job(interval=timedelta(seconds=15))
def MentionsJob():
    global since_id
    since_id = tweets.reply_to_mentions(api, since_id)
    
        
tl.start(block=True)