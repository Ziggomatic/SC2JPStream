# -*- coding: utf-8 -*-

import sys
import tweepy
import linecache

consumer_key = linecache.getline('TOKENS',1)
consumer_secret = linecache.getline('TOKENS',2)
access_token = linecache.getline('TOKENS',3)
access_token_secret = linecache.getline('TOKENS',4)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def update_status(s):
    print(s)
    api.update_status(s)
