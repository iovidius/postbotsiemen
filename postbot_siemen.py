# Postbot Siemen is a Twitter bot based on Postbode Siemen (Zaai). He can:
#   1) Give the translation of any word to the secret code of 'Wokkie Tokkie' 
#   2) Tell people who are being bored that he has to work

from dotenv import load_dotenv
load_dotenv()

import tweepy
import os


# Authenticate to Twitter
#auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
#auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))

# Create API object
#api = tweepy.API(auth)

# Create a tweet
#api.update_status("Hooooooooooi!")


vowels = {
  'a': '1',
  'e': '2',
  'i': '3',
  'o': '4',
  'u': '5'
}

def wokkie_tokkie(input):
    # Returns the translation of a string to 'wokkie tokkie'
    output = ''
    for c in input:
        if (c in vowels):
            output += vowels[c] + ' '
        else:
            output += c + 'okkie '
    return output.strip()

print(wokkie_tokkie('hut'))
