# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 22:30:25 2017

@author: juang
Simulador prototipo Subtuiter Ambiental
"""

from __future__ import division
import pdb #para hacer debug parcial
try:
    import json
except ImportError:
    import simplejson as json
# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import time
import math
import pickle
from datetime import date,timedelta
import unicodedata
import nltk
import re, string
#import CuentaTema
from difflib import SequenceMatcher
from CuentaTemaa import *
"""
La funcion CuentaTemaa define el tema mediante las palabras que más aparecen en
el archivo Ambiente.txt
"""
A=CuentaTemaa()
"""
Se Cargan las credenciales de acceso al api de twitter
"""
ACCESS_TOKEN = u'817383621397008384-TXP2pfAr0aLmr3E9Le3tDBlMSsUTQF9'
ACCESS_SECRET = u'oBXXy2cmyZ80PUm6EhUHGAs7SRb13HxYO5TWj2fq9AYVN'
CONSUMER_KEY = u'kpKOxDTCtWI8ueapP6JSySgfM'
CONSUMER_SECRET = u'ep7Di6fA1izMlQdQXBmcKiGT0q7PoXX2nDgaxFHjihA2ofgaAu'
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
"""
Ciclo de Simulacion: Busqueda de tuits ambientales en Morrocoyo TimeLine + Streaming
"""
Influenciadores = pickle.load( open( 'Influenciadores', "rb" ) )
LA=A.keys()
twitter = Twitter(auth=oauth)
MorroTL=twitter.statuses.home_timeline(count=200)
k=1;
i=0;
w, h = len(MorroTL), 3
"""
Crea un lista de 3 listas de tamaño Longitud de MorroTL con la calificacion de criterio para cada tweet 
"""
Criterios = [[0 for x in range(w)] for y in range(h)]
c=0;
L=dict();
for tweet in MorroTL:
    try:        #si es un retweet
        try:        #si cita una pagina en el tweet
            L[i]=[tweet['retweeted_status']['user']['name'],tweet['retweeted_status']['user']['screen_name'],
              tweet['retweeted_status']['text'],tweet['retweeted_status']['created_at'],
              tweet['retweeted_status']['retweet_count'],tweet['retweeted_status']['favorite_count'],
              tweet['retweeted_status']['user']['description'],tweet['retweeted_status']['entities']['urls'][0]['url'],
              tweet['created_at'],tweet['user']['time_zone'], tweet['user']['lang'], tweet['place'],
              tweet['user']['verified'],tweet['user']['screen_name'],tweet['user']['description'],
              tweet['user']['followers_count'],tweet['user']['friends_count'],tweet['user']['statuses_count']];
        except:
            L[i]=[tweet['retweeted_status']['user']['name'],tweet['retweeted_status']['user']['screen_name'],
              tweet['retweeted_status']['text'],tweet['retweeted_status']['created_at'],
              tweet['retweeted_status']['retweet_count'],tweet['retweeted_status']['favorite_count'],
              tweet['retweeted_status']['user']['description'],'',
              tweet['created_at'],tweet['user']['time_zone'], tweet['user']['lang'], tweet['place'],
              tweet['user']['verified'],tweet['user']['screen_name'],tweet['user']['description'],
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
    for r in LA:
        try:
            if r.lower() in L[i][2].encode('utf-8').lower().split():
                c+=1
        except:
            pass
    Criterios[0][i]=max(c,1)
    c=0
    try:
        Criterios[1][i]=Influenciadores[L[i][1]]
    except:
        pass
    try:
        u=twitter.users.lookup(screen_name=L[i][1])  
        if u[0]['followers_count']>60:
            Criterios[2][i]=u[0]['followers_count']/u[0]['statuses_count']
    except:
        pass
    print L[i][0]
    print i
    i+=1
    
    
    
    
    
    
    
    
    