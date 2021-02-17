from typing import Pattern
import wokkietokkie
import replies
import tweepy
from replies import Template, Word
import data
from regex_methods import match, trans_pattern, quotes_pattern, wt_pattern, bored_pattern

# Check if user asks for translation (e.g. 'wat is X?')
def ask_for_translation(tweet):
    if not ' ' in tweet:
        return tweet

    term = match(tweet.lower(), trans_pattern)
    if term != '':
        return term
    
    term = match(tweet.lower(), quotes_pattern)
    if term != '':
        return term[1:-1]
    
    return ''


# Check if user says he's bored (e.g. ik verveel me)
def ask_for_bored(tweet):
    return match(tweet, bored_pattern) != ''

# Generate a reply to a tweet
def reply(tweet):

    # Check wokkie-tokkie matches
    term = match(tweet, wt_pattern).lower()
  
    translated_part = ask_for_translation(tweet)

    if (term != ''):
         # There has been an instance of 'wokkie tokkie'. Our response is to give a translation.
        translation = wokkietokkie.decipher(term)
        
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
    elif translated_part != '':
        # Translate
       return replies.generate(Template.translation, wokkietokkie.encipher(translated_part))
    elif ask_for_bored(tweet):
        return replies.generate(Template.bored)
    else:
        # Other input
        return replies.generate(Template.dunno)


# Check mentions
def reply_to_mentions(api, since_id):
    print("Retrieving mentions...")
    new_since_id = since_id

    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        try:
            new_since_id = max(tweet.id, new_since_id)
            if tweet.in_reply_to_status_id is not None:
                continue
            
            # preprocess
            input = tweet.text.replace('@PostbotSiemen', '').strip()
            rep = '@' + tweet.user.screen_name + ' ' + reply(input)

            if len(rep) > 280:
                rep = '@' + tweet.user.screen_name + ' ' + replies.generate(Template.too_long)

            print("Replying to " + tweet.user.screen_name)
            api.update_status(rep, tweet.id)

            data.setData('lastTweet', new_since_id)
            
        except tweepy.TweepError as e:
            print(e.reason)

    return new_since_id