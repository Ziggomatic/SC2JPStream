# -*- coding: utf-8 -*-

import twitch
import twitter
import nico
import openrec
from datetime import datetime
from pytz import timezone
from time import sleep

def shorten_url(url):
    if url.startswith("http://"):
        return url[7:]
    if url.startswith("https://"):
        return url[8:]
    return url

def post(now, streams, header):
    streams = list(streams)
    if len(streams) <= 0:
        return
    lines = [now.strftime('%m/%d %X'), header]
    lines.extend("{}:{}".format(label, shorten_url(url)) for (label, url) in streams)
    twitter.update_status('\n'.join(lines))

def post_twitch(now):
    post(now, twitch.streams(limit=3), '[Twitch]')

def post_nico(now):
    post(now, nico.streams(limit=2), '[ニコ生]')

def post_openrec(now):
    post(now, openrec.streams(limit=3), '[OPENREC]')

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
