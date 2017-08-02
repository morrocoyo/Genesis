# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 09:41:04 2017

@author: juang
"""

from dateutil import parser

def CargaTweet(L, tweet, i):
    try:        #si es un retweet
        try:        #si cita una pagina en el tweet
            L[i]=[tweet['retweeted_status']['user']['name'],tweet['retweeted_status']['user']['screen_name'],
              tweet['retweeted_status']['text'],tweet['retweeted_status']['created_at'],
              tweet['retweeted_status']['retweet_count'],tweet['retweeted_status']['favorite_count'],
              tweet['retweeted_status']['user']['description'],tweet['retweeted_status']['entities']['urls'][0]['url'],
              tweet['created_at'],tweet['user']['time_zone'], tweet['user']['lang'], tweet['place'],
              tweet['user']['verified'],tweet['user']['name'],tweet['user']['description'],
              tweet['user']['followers_count'],tweet['user']['friends_count'],tweet['user']['statuses_count']];
        except:
            L[i]=[tweet['retweeted_status']['user']['name'],tweet['retweeted_status']['user']['screen_name'],
              tweet['retweeted_status']['text'],tweet['retweeted_status']['created_at'],
              tweet['retweeted_status']['retweet_count'],tweet['retweeted_status']['favorite_count'],
              tweet['retweeted_status']['user']['description'],'',
              tweet['created_at'],tweet['user']['time_zone'], tweet['user']['lang'], tweet['place'],
              tweet['user']['verified'],tweet['user']['name'],tweet['user']['description'],
              tweet['user']['followers_count'],tweet['user']['friends_count'],tweet['user']['statuses_count']];      
    except:
        try:        #si cita una pagina en el tweet
            L[i]=[tweet['user']['name'],tweet['user']['screen_name'],
              tweet['text'],tweet['created_at'],
              tweet['retweet_count'],tweet['favorite_count'],
              tweet['user']['description'],tweet['entities']['urls'][0]['url'],
              tweet['created_at'],tweet['user']['time_zone'], tweet['user']['lang'], tweet['place'],
              tweet['user']['verified'],'','',tweet['user']['followers_count'],
              tweet['user']['friends_count'],tweet['user']['statuses_count']];
        except:
            L[i]=[tweet['user']['name'],tweet['user']['screen_name'],
              tweet['text'],tweet['created_at'],
              tweet['retweet_count'],tweet['favorite_count'],
              tweet['user']['description'],'',
              tweet['created_at'],tweet['user']['time_zone'], tweet['user']['lang'], tweet['place'],
              tweet['user']['verified'],'','',tweet['user']['followers_count'],
              tweet['user']['friends_count'],tweet['user']['statuses_count']]; 
    try:
        L[i].extend([tweet['entities']['media'][0]['media_url']]) 
    except:
        L[i].extend([''])    
    
    return L