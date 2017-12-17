import tweepy
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# For loop to iterate over tweets with #ocean, limit to 10
for tweet in tweepy.Cursor(api.search,q='#gonzaga').items(10):

# Print out usernames of the last 10 people to use #ocean
    print('Tweet by: @' + tweet.user.screen_name)
