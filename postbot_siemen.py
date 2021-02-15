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
  'u': '5',
  '1':'a',
  '2':'e',
  '3':'i',
  '4':'o',
  '5':'u'
}

# Returns the translation of an input string to 'wokkie tokkie'
def to_wokkietokkie(input): 
    output = ''
    for c in input:
        if (c in vowels):
            output += vowels[c] + ' '
        else:
            output += c +  'okkie ' if c.isalpha() else c
    return output.strip()

# Returns the translation of a 'wokkie tokkie' string to a normal string
# Expects an input in wokkie tokkie format.
def from_wokkietokkie(input):

    # remove spaces
    output = input.replace(' ','')

    # replace all consonants
    output = output.replace('okkie','')

    # replace all numbers
    for c in output:
        if (c in vowels):
            output = output.replace(c,vowels[c])

    return output