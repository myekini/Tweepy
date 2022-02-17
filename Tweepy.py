import tweepy
import os 

consumer_key = 'bhbL9Xe1jp9BoWKRuJwCnaH2b'
consumer_secret = 'eql1G0u54iCktpZhNNT1ZC9NE7wCjByqOQhhOqENkG56LB5oAL'
access_token = '349508797-sdVG2k5MpHJUy2OtJcxJiChsluvt3LtFhxaRgRpM'
access_token_secret = 'Yh9K3nPyipPqfdufE59EUCONWOJ4W9DqQsQi8tuJiEzh7'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)