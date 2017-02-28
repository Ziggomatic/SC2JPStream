# SC2JPStream
Inspired by [Dota2 Watcher](https://github.com/Lillie251/Dota2watcher) by Lillie251  
Some Code Written by Miaha  

## 何これ
twitch/ニコ生でStarCraft IIの日本語配信を行っているリンクを一時間おきにツイートするbot  
[SJC](http://starcraft2.jpcommunity.com/sc2/)にいちいちアクセスして確認するのが面倒なので書いた

## 使ったもの

* Python 3.5.2
* tweepy
* pytz
* cssselect, lxml (OPENREC用)
* twitter,twitchのアカウント

## 使い方
1. 環境変数に以下のKeyを設定する
    * TWITTER_CONSUMER_KEY
    * TWITTER_CONSUMER_SECRET
    * TWITTER_ACCESS_TOKEN
    * TWITTER_ACCESS_TOKEN_SECRET
    * TWITCH_CLIENT_ID
2. ```$python twitch.py```で実行

##その他

1. twitch.pyの`game='StarCraft+II'`の部分を好きなゲームタイトルにすれば流用出来る (nico.py, openrec.pyも同様)
2. ~~Herokuで動かしているのでAM4~AM10は動かない~~ **現在VPSで24時間稼働中**
3. バグ報告,改善案など大募集中(他力本願)
4. ~~デプロイする度にツイートするのでたまに連投する~~ **FIXED**
5. ~~他サービス(ニコ生,OPENREC)への対応~~ **2016/12/02 ニコ生対応**, **2016/12/06 OPENREC対応**, **2017/2/28 アフリカTV対応**
