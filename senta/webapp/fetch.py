import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

consumer_key = "loPKijQxm9HvnFvW47TYKYMx3"
consumer_secret = "KMPdYuiZD3qsRg9hI3Zvhk38UIsaQa01fpZp6etLUN1FTEPIaQ"
access_key = "593403483-XUxnDy6azxMojMuCwowo8gtZQ36u0AF5TNEk5d6j"
access_secret = "YDvzRQ3jeJinaUYZpPEkoOzOMBclLaBMzEzHGyw2iNcBR"

def fetch_tweets():
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    tweets = api.search(q='Telangana',count = '100')
    fetched_tweets = []
    for tweet in tweets:
        req_fields = { 'text' : tweet.text.encode('utf-8'),
         'location' : tweet.user.location,
         'time': tweet.user.created_at,
         'verfied':tweet.user.verified,
         'id': tweet.id,
         'hashtag': tweet.entities['hashtags'],
         'people:':tweet.entities['user_mentions'],
         'sentiment':TextBlob(tweet.text).sentiment.polarity,
            }
        # fetched_tweets.append(tweet.text.encode('utf-8'))
        # fetched_tweets.append(TextBlob(tweet.text).sentiment.polarity) 
        fetched_tweets.append(req_fields)
        fetched_tweets.append('<br>')
        print(tweet.text.encode('utf-8'))
        print(TextBlob(tweet.text).sentiment.polarity)

    return fetched_tweets

        