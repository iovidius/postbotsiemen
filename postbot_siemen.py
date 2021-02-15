# Postbot Siemen is a Twitter bot based on Postbode Siemen (Zaai). He can:
#   1) Give the translation of any word to the secret code of 'Wokkie Tokkie' 
#   2) Tell people who are being bored that he has to work

from dotenv import load_dotenv
load_dotenv()

import tweepy
import os
import wokkietokkie
import replies
from replies import Template, generate

# Authenticate to Twitter
#auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
#auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))

# Create API object
#api = tweepy.API(auth)

# Create a tweet
#api.update_status("Hooooooooooi!")




# Generate a reply to a tweet.
def reply(tweet):

    # Check wokkie-tokkie matches
    match = wokkietokkie.match(tweet)
  
    if (match != ''):
         # There has been an instance of 'wokkie tokkie'. Our response is to give a translation.
         # First check if the translation is already there!
        translation = wokkietokkie.decipher(match)
    
        if (translation in tweet):
            return replies.generate(Template.confirmation)
        else:
            return replies.generate(Template.translation, translation)
    elif not ' ' in tweet:
        # This is just one word. Translate it.
       return replies.generate(Template.translation, wokkietokkie.encipher(tweet))
    else:
        # No idea
        return replies.generate(Template.dunno)



print(reply("Wat is gokkie 2 sokkie 4 dokkie 2 mokkie 3 2 tokkie 2 rokkie?"))
print(reply("is gokkie 4 2 dokkie goed?"))