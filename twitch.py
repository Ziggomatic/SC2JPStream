# -*- coding: utf-8 -*-

import json
import sys
from os import environ
from urllib.error import HTTPError
from urllib.request import urlopen

# Twitch配信を検索
# (name, url)のタプルイテレータを返す
def streams(game='StarCraft+II', language='ja', limit=5):
    # client_id
    try:
        client_id = environ['TWITCH_CLIENT_ID']
    except KeyError:
        print("TWITCH_CLIENT_ID not found in environment variables", file=sys.stderr)
        return

    # urlopen
    url = "https://api.twitch.tv/kraken/streams"
    url += "?game={}".format(game)
    url += "&language={}".format(language)
    url += "&limit={}".format(limit)
    url += "&client_id={}".format(client_id)

    # request
    try:
        res = urlopen(url)
    except HTTPError as e:
        print("twitch.streams failure: {} {}".format(e.code, e.reason), file=sys.stderr)
        return

    # parse
    j = res.read().decode('utf8')
    root = json.loads(j)
    for st in root['streams']:
        name = st['channel']['name']
        url = st['channel']['url']
        yield (name, url)

if __name__ == '__main__':
    for (name, url) in streams(language='en'):
        print("{}:{}".format(name, url))
