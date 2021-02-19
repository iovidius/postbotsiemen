# Postbot Siemen
## Introduction
[@PostbotSiemen](https://twitter.com/postbotsiemen) is a Twitter bot based on Postbode Siemen (Zaai). He can:
  1. Give the translation of any word to the secret code of ['Wokkie Tokkie'](https://www.youtube.com/watch?v=uQf88h1ludk), and also decipher Wokkie Tokkie.
  2. Tell people who are being bored that he has to work, and provide them with something to watch.
  3. Post a Postbode Siemen quote every week.

## How does it work?
This bot makes use of the [Tweepy library](https://www.tweepy.org/). It scans for mentions every 15 seconds and generates a reply automatically. 

## How to run?
Run **main.py**.

Don't forget to update the _lastTweet_ and _lastQuote_ entry in **data/data.json** in order to prevent Siemen from replying to old tweets and tweeting the same quote in a row. In a future release this should be done automatically upon initializing.
