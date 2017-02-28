# -*- coding: utf-8 -*-

import json
import sys
from itertools import islice
from urllib.error import HTTPError
from urllib.request import urlopen

# アフリカTV配信を検索
# (name, url)のタプルイテレータを返す
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
    root = json.loads(j)
    return islice(__parse_json(root), limit)

def __parse_json(root):
    for x in root['channel']['glist']:
        if x["pwd"] == "1": # ignore private stream
            continue
        name = x['bnick']
        url = "http://live.afreecatv.jp/" + x['bid']
        yield (name, url)

if __name__ == '__main__':
    for (name, url) in streams(query=''):
        print("{}:{}".format(name, url))
