# -*- coding: utf-8 -*-

import tweepy
import twitch
import nico
import openrec
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

def shorten_url(url):
    if url.startswith("http://"):
        return url[7:]
    if url.startswith("https://"):
        return url[8:]
    return url

def post(now, streams, header):
    streams = list(streams)
    if len(streams) > 0:
        lines = [now.strftime('%m/%d %X'), header]
        lines.extend("{}:{}".format(label, shorten_url(url)) for (label, url) in streams)
        s = '\n'.join(lines)
        print(s)
        api.update_status(s)

def post_twitch(now):
    post(now, twitch.streams(limit=5), '[Twitch]')

def post_nico(now):
    post(now, nico.streams(limit=5), '[ニコ生]')

def post_openrec(now):
    post(now, openrec.streams(limit=5), '[OPENREC]')

# hourが変わるたびに投稿する
last_hour = datetime.now(timezone('Asia/Tokyo')).hour
while True:
    now = datetime.now(timezone('Asia/Tokyo'))
    if now.hour != last_hour:
        post_twitch(now)
        post_nico(now)
        post_openrec(now)
    last_hour = now.hour
    sleep(600)
