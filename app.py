# -*- coding: utf-8 -*-


import json
import urllib.request
import tweepy
import time
from datetime import datetime
from pytz import timezone
from os import environ

twitch_api = 'https://api.twitch.tv/kraken/streams'
onlySC2 = '?game=StarCraft+II'  # SC2を配信しているか
isJapanese = '&language=ja'  # 日本語での配信
limit = '&limit=5'  # 5人も同時に配信はしないでしょうという偏見
client_id = environ['TWITCH_CLIENT_ID']  # twitchAPIのクライアントID


consumer_key = environ['TWITTER_CONSUMER_KEY']
consumer_secret = environ['TWITTER_CONSUMER_SECRET']
access_token = environ['TWITTER_ACCESS_TOKEN']
access_token_secret = environ['TWITTER_ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


last_hour = datetime.now(timezone('Asia/Tokyo')).hour
while True:
    jst_now = datetime.now(timezone('Asia/Tokyo'))
    if jst_now.hour != last_hour: # hourが変わるたびにツイートする
        now = jst_now.strftime('%m/%d %X')
        res = urllib.request.urlopen(twitch_api + onlySC2 + limit + isJapanese + client_id)
        j = json.loads(res.read().decode('utf8'))
        if j['_total'] == 0:  # 該当配信が0の場合

            api.update_status(str(now) + "\n" + "no one streaming. ")
        else:  # 配信の数をカウント
            total = j['_total']
            list = []
            for x in range(total):
                name = j['streams'][x]['channel']['name']
                url = j['streams'][x]['channel']['url']
                line = name + ":" + url
                list.append(line)
                s = '\n'.join(list)
            # 同じツイートをすると怒られるので申し訳程度にnow()を添える
            api.update_status(str(now) + "\n" + s)
    last_hour = jst_now.hour
    time.sleep(600)
