# SC2JPStream
Inspired by [Dota2 Watcher](https://github.com/Lillie251/Dota2watcher) by Lillie251  
Some Code Written by Miaha  

## 何これ
twitchでStarCraft IIの日本語配信を行っているリンクを一時間おきにツイートするbot  
[SJC](http://starcraft2.jpcommunity.com/sc2/)にいちいちアクセスして確認するのが面倒なので書いた
## 使ったもの
Python 3.5.2  
tweepy  
pytz  

```python
import json
import urllib.request
import tweepy
import time
from datetime import datetime
from pytz import timezone
from os import environ
```   
twitter,twitchのアカウント

## 使い方
1. 環境変数に以下のKeyを設定する  
2. ```$python twitch.py```で実行

```python
client_id = environ['TWITCH_CLIENT_ID']  
consumer_key = environ['TWITTER_CONSUMER_KEY']
consumer_secret = environ['TWITTER_CONSUMER_SECRET']
access_token = environ['TWITTER_ACCESS_TOKEN']
access_token_secret = environ['TWITTER_ACCESS_TOKEN_SECRET']
```

##その他
```onlySC2 = '?game=StarCraft+II'```  
  
1. ここを好きなゲームタイトルにすれば流用出来る  
2. Herokuで動かしているのでAM4~AM10は動かない
3. バグ報告,改善案など大募集中(他力本願)
4. デプロイする度にツイートするのでたまに連投する
