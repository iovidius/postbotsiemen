import wokkietokkie
import replies
import tweepy

from replies import Template, Word
import data

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