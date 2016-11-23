# SC2JPStream
Inspired by [Dota2 Watcher](https://github.com/Lillie251/Dota2watcher) by Lillie251  
Almost Code Written by Miaha  

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
```   
twitter,twitchのアカウント

## 使い方
1. 以下を各自用意したKeyで埋める  
2. ```$python twitch.py```で実行

```python
client_id = 'twitchAPIのClient_ID'
#以下四つはtwitterのAPIKey
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
```

##その他
```onlySC2 = '?game=StarCraft+II'```  
ここを好きなゲームタイトルにすれば流用出来る


