# -*- coding: utf-8 -*-

import json
from urllib.error import HTTPError
from urllib.request import urlopen

# ニコ生配信を検索
# (title, url)のタプルイテレータを返す
def streams(query='StarCraft2+OR+SC2', targets='tags', limit=5):
    # url
    url = "http://api.search.nicovideo.jp/api/v2/live/contents/search"
    url += "?q={}&targets={}".format(query, targets) # 検索対象
    url += "&filters[liveStatus][0]=onair" # 放送中のみ
    url += "&fields=contentId,title" # 欲しいデータ
    url += "&_sort=-startTime" # 開始時間でソート
    url += "&_limit={}".format(limit)
    url += "&_context=apiguide"

    # urlopen
    try:
        res = urlopen(url)
    except HTTPError as e:
        print("nico.streams failure: {} {}".format(e.code, e.reason), file=sys.stderr)
        return

    # parse
    j = res.read().decode('utf8')
    root = json.loads(j)
    for d in root['data']:
        title = d['title']
        url = 'http://live.nicovideo.jp/watch/' + d['contentId']
        yield (title, url)

if __name__ == '__main__':
    for (name, url) in streams(query='Splatoon'):
        print("{}:{}".format(name, url))
