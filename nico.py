# -*- coding: utf-8 -*-

import json
from urllib.request import urlopen

TAG = 'StarCraft2'

# ニコ生配信を検索
# (title, url)のタプル配列を返す
def streams(limit=5):
    url = "http://api.search.nicovideo.jp/api/v2/live/contents/search"
    url += "?q={}&targets=tags".format(TAG) # タグ
    url += "&filters[liveStatus][0]=onair" # 放送中のみ
    url += "&fields=contentId,title" # 欲しいデータ
    url += "&_sort=-startTime" # 開始時間でソート
    url += "&_limit={}".format(limit) # 件数
    url += "&_context=apiguide"
    res = urlopen(url)
    j = json.loads(res.read().decode('utf8'))
    if res.getcode() != 200:
        return []
    return [(x['title'], live_url(x['contentId'])) for x in j['data']]

def live_url(content_id):
    return 'http://live.nicovideo.jp/watch/' + content_id
