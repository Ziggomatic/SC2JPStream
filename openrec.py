# -*- coding: utf-8 -*-

import lxml.html
import sys
import traceback
from itertools import islice
from urllib.error import HTTPError
from urllib.request import urlopen

SC2 = 'ShcGI8HV4nW'

# OPENREC配信を検索
# (name, url)のタプルイテレータを返す
def streams(game=SC2, limit=5):
    # urlopen
    url = 'https://www.openrec.tv/game/' + game
    try:
        res = urlopen(url)
    except HTTPError as e:
        print("openrec.streams failure: {} {}".format(e.code, e.reason), file=sys.stderr)
        return []

    # parse
    html = res.read().decode('utf-8')
    root = lxml.html.fromstring(html)
    it = __parse_dom(root)
    return islice(it, limit)

# NOTE: DOM構造が変わると死ぬ
def __parse_dom(root):
    try:
        # is live?
        live = None
        ul = root.cssselect('ul.c-contents')[0]
        for li in ul.cssselect('li.c-content'):
            title = li.cssselect('div.c-content__title')[0]
            if title.text_content() == "Live":
                live = li
                break
        # streams
        if live is not None:
            ul = live.cssselect('ul.c-content__list')[0]
            for li in ul.cssselect('li.c-thumbnailVideo'):
                name = li.cssselect('a.c-thumbnailVideo__header__text__ellipsis__link')[0].text_content()
                url = li.cssselect('a.c-thumbnailVideo__box')[0].attrib['href']
                yield (name, url)
    except Exception:
        print("openrec.__parse_dom failure", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)

if __name__ == '__main__':
    SPLATOON = 'r0mbp8NZl34'
    for (name, url) in streams(game=SPLATOON):
        print("{}:{}".format(name, url))
