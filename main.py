# Postbot Siemen is a Twitter bot based on Postbode Siemen (Zaai). He can:
#   1) Give the translation of any word to the secret code of 'Wokkie Tokkie' 
#   2) Tell people who are being bored that he has to work


import wokkietokkie
import replies
from replies import Template, Word
from config import create_api
import tweepy
import time

# Generate a reply to a tweet
def reply(tweet):

    # Check wokkie-tokkie matches
    match = wokkietokkie.match(tweet)
  
    if (match != ''):
         # There has been an instance of 'wokkie tokkie'. Our response is to give a translation.
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
        # Other input
        return replies.generate(Template.dunno)


# Check mentions
def reply_to_mentions(api, since_id):
 
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        
        # preprocess
        input = tweet.text.replace('@PostbotSiemen', '').strip()
        reply = '@' + tweet.user.screen_name + ' ' + reply(input)
        if len(reply) > 280:
            reply = '@' + tweet.user.screen_name + ' ' + replies.generate(Template.too_long)

        api.update_status(reply, tweet.id)

    return new_since_id


# Main function
def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = reply_to_mentions(api, since_id)
        time.sleep(60)


main()