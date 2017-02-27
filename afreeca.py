# -*- coding: utf-8 -*-

import json
import sys
from itertools import islice
from urllib.error import HTTPError
from urllib.request import urlopen

# Afreeca配信を検索
# (title, url)のタプルイテレータを返す
def streams(query='starcraft', limit=5):
    # urlopen
    url = 'http://search.afreecatv.jp/app_search.php/?pt=sch_lives&q=' + query
    try:
        res = urlopen(url)
    except HTTPError as e:
        print("afreeca.streams failure: {} {}".format(e.code, e.reason), file=sys.stderr)
        return []

    # parse
    j = res.read().decode('utf8')
    return islice(__parse(j), limit)

def __parse(j):
    root = json.loads(j)
    for x in root['channel']['glist']:
        if x["pwd"] == "1": # ignore private stream
            continue
        title = x['title']
        url = "http://live.afreecatv.jp/" + x['bid']
        yield (title, url)

if __name__ == '__main__':
    for (title, url) in streams(query=''):
        print("{}:{}".format(title, url))
