# -*- coding: utf-8 -*-

import afreeca
import nico
import openrec
import sys
import traceback
import twitch
import twitter
from datetime import datetime
from pytz import timezone
from time import sleep

def post_base(now, streams, header):
    streams = list(streams)
    if len(streams) <= 0:
        return
    lines = [now.strftime('%m/%d %X'), header]
    lines.extend("{}:{}".format(label, url) for (label, url) in streams)
    twitter.update_status('\n'.join(lines))

def post_twitch(now):
    post_base(now, twitch.streams(limit=3), '[Twitch]')

def post_nico(now):
    post_base(now, nico.streams(limit=2), '[ニコ生]')

def post_openrec(now):
    post_base(now, openrec.streams(limit=3), '[OPENREC]')

def post_afreeca(now):
    post_base(now, afreeca.streams(), '[AfreecaTV]')

def post_safe(postfunc, now):
    try:
        postfunc(now)
    except Exception as e:
        print("Unknown exception: {}".format(e), file=sys.stderr)
        traceback.print_exc(file=sys.stderr)

# hourが変わるたびに投稿する
last_hour = datetime.now(timezone('Asia/Tokyo')).hour
while True:
    now = datetime.now(timezone('Asia/Tokyo'))
    if now.hour != last_hour:
        post_safe(post_twitch, now)
        post_safe(post_nico, now)
        post_safe(post_openrec, now)
        post_safe(post_afreeca, now)
    last_hour = now.hour
    sleep(600)
