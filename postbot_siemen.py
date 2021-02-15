# Postbot Siemen is a Twitter bot based on Postbode Siemen (Zaai). He can:
#   1) Give the translation of any word to the secret code of 'Wokkie Tokkie' 
#   2) Tell people who are being bored that he has to work


import wokkietokkie
import replies
from replies import Template, Word
from config import create_api
import tweepy
import time



# Generate a reply to a tweet.
def reply(tweet):

    # Check wokkie-tokkie matches
    match = wokkietokkie.match(tweet)
  
    if (match != ''):
         # There has been an instance of 'wokkie tokkie'. Our response is to give a translation.
         # First check if the translation is a bad word, then check if the user has 
         # put it there (e.g. "does X translate to Y?")
        translation = wokkietokkie.decipher(match)
        
        # Check if bad word
        if (replies.isBad(translation) == Word.bad_en):
            return replies.generate(Template.bad_en)
        elif (replies.isBad(translation) == Word.bad_nl):
            return replies.generate(Template.bad_nl)

        # Check if user already gave translation
        if (translation in tweet):
            return replies.generate(Template.confirmation)
        
        # Return translation
        return replies.generate(Template.translation, translation)
    elif not ' ' in tweet:
        # This is just one word. Translate it.
       return replies.generate(Template.translation, wokkietokkie.encipher(tweet))
    else:
        # No idea
        return replies.generate(Template.dunno)


# Main function
def main():
    api = create_api()
    while True:
        #follow_followers(api)
        time.sleep(60)


#print(reply('Wat is gokkie 2 sokkie 4 dokkie 2 mokkie 3 2 tokkie 2 rokkie?'))
#print(reply('heeey siemen, wat is kokkie 5 tokkie?'))
print(replies.isBad("hoi"))