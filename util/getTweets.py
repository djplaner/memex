#
# getTweets.py
# - eventually get a tweet and associated replies and output to markdown

import tweepy
from simple_settings import settings


auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
auth.set_access_token(settings.access_token, settings.access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)