# -*- coding: utf-8 -*-

import json
from os import environ
from urllib.request import urlopen

GAME = 'StarCraft+II'
LANGUAGE = 'ja'
CLIENT_ID = environ['TWITCH_CLIENT_ID'] # twitchAPIのクライアントID

# Twitch配信を検索
# (name, url)のタプル配列を返す
def streams(limit=5):
    url = "https://api.twitch.tv/kraken/streams"
    url += "?game={}".format(GAME) # ゲーム
    url += "&language={}".format(LANGUAGE) # 言語
    url += "&limit={}".format(limit) # 件数
    url += "&client_id={}".format(CLIENT_ID)
    res = urlopen(url)
    if res.getcode() != 200:
        return []
    j = json.loads(res.read().decode('utf8'))
    return [(x['channel']['name'], x['channel']['url']) for x in j['streams']]
