# -*- coding: utf-8 -*-

import tweepy
import twitch
import nico
from datetime import datetime
from os import environ
from pytz import timezone
from time import sleep

consumer_key = environ['TWITTER_CONSUMER_KEY']
consumer_secret = environ['TWITTER_CONSUMER_SECRET']
access_token = environ['TWITTER_ACCESS_TOKEN']
access_token_secret = environ['TWITTER_ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def post_twitch(now):
    streams = twitch.streams(limit=5)
    if len(streams) > 0:
        lines = [now.strftime('%m/%d %X'), '[Twitch]']
        lines.extend("{}:{}".format(x[0], x[1]) for x in streams)
        api.update_status('\n'.join(lines))

def post_nico(now):
    streams = nico.streams(limit=5)
    if len(streams) > 0:
        lines = [now.strftime('%m/%d %X'), '[ニコ生]']
        lines.extend("{}:{}".format(x[0], x[1]) for x in streams)
        api.update_status('\n'.join(lines))

# hourが変わるたびに投稿する
last_hour = datetime.now(timezone('Asia/Tokyo')).hour
while True:
    now = datetime.now(timezone('Asia/Tokyo'))
    if now.hour != last_hour:
        post_twitch(now)
        post_nico(now)
    last_hour = now.hour
    sleep(600)
