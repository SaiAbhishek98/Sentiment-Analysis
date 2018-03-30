import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

consumer_key = 'mvzp1bHYFrllRPOlztJr5hAf4'
consumer_secret = '0a2hQ6EblrCWRd7fPHmgxJterHagfko6MWLgJCOm6kMReiVN28'
access_token = '463677903-4yL7Lj4WvzD9DOw0JXJWydUwmo6bjCO5nSeJd1k8'
access_token_secret = 'VwT17ydddNmF8s6yfNO2KXFfLTqy32gfnP9SUVZCgSn0C'

def fetch_tweets(request):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    tweets = api.search(q='Telangana',count = '100')
    for tweet in tweets:
        print(tweet.text)
        print(TextBlob(tweet.text).sentiment.polarity)


        