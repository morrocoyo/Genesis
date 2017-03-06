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
from dateutil import parser
from datetime import date,timedelta,datetime
import datetime
import time
import math
import pickle
import operator
import unicodedata
import nltk
import re, string
#import CuentaTema
from difflib import SequenceMatcher
from CuentaTemaa import *

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
"""
La funcion CuentaTemaa define el tema mediante las palabras que más aparecen en
el archivo Ambiente.txt
"""
A=CuentaTemaa()
#A = pickle.load( open( 'A', "rb" ) )
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
#Lista de palabras mas usadas en el tema
LA=A.keys()
#pdb.set_trace()   
#crea un texto con las palabras separandolas por coma
tx=",".join(LA)
twitter = Twitter(auth=oauth)
MorroTL=twitter.statuses.home_timeline(count=200)
try:
   LastId=MorroTL[len(MorroTL)-1]['id']
except:
    LastId=0;       
#One_hour_ago = datetime.datetime.utcnow().replace(microsecond=0)-datetime.timedelta(hours = 1)
One_hour_ago = datetime.datetime.utcnow()-datetime.timedelta(hours = 1)
k=10   #veces que corre el ciclo completo
kk=5    #veces que corre el ciclo de streaming
count1=0;
tweet_count = 50    #de tweets que lee en el streaming
i=0;
L=dict();
while (count1<k):
    if count1>0:
        MorroTL=twitter.statuses.home_timeline(count=200)
    for tweet in MorroTL:
        try:
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
        
            tweeted_datetime = parser.parse(L[i][3]).replace(tzinfo=None)       
            if tweeted_datetime > One_hour_ago:
                print i            
                i+=1 
        except:
            pass
    count2=0;        
    while (count2<kk):
        twitter_stream = TwitterStream(auth=oauth)
        iterator = twitter_stream.statuses.filter(track=tx, language="es")
        print count2
        if count2>0:
            time.sleep(180)
        for tweet in iterator:
            tweet_count -= 1
            try:
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
                    
                tweeted_datetime = parser.parse(L[i][3]).replace(tzinfo=None)
                if tweeted_datetime > One_hour_ago:
                    print i
                    i+=1           
            except:
                pass
            if tweet_count <= 0:
                break 
                    
        count2+=1
   
    count1+=1
    """
    Crea una lista de 3 listas de tamaño Longitud de MorroTL+tweet_count con la calificacion de criterio para cada tweet 
    """
    w, h = len(L), 3
    Criterios = [[0 for x in range(w)] for y in range(h)]
    c=0;
    '''
    Primer Criterio: Numero de palabras del tema
    Segundo Criterio:Score del usuario en Influenciadores
    Tercer Criterio: Razon seguidores/tweets
    '''
    for q in range(len(L)):  
        for r in LA:
            try:
                if r.lower() in L[q][2].encode('utf-8').lower().split():
                    c+=1
            except:
                pass
        Criterios[0][q]=max(c,0)
        c=0
        try:
            Criterios[1][q]=Influenciadores[L[q][1]]
        except:
            pass
        try:
            u=twitter.users.lookup(screen_name=L[q][1])  
            if u[0]['followers_count']>60:
                Criterios[2][q]=u[0]['followers_count']/u[0]['statuses_count']
        except:
            pass
    LBIG=L;
      
    Criterios0=[Criterios[0][q] for q in range(len(L)) if Criterios[0][q]>0]
    Criterios1=[Criterios[1][q] for q in range(len(L)) if Criterios[0][q]>0]
    Criterios2=[Criterios[2][q] for q in range(len(L)) if Criterios[0][q]>0]
    L=[L[q] for q in range(len(L)) if Criterios[0][q]>0]
    Indices=range(len(L))
    Indices=sorted(zip(Criterios0,Indices),reverse=True)
    Indices = [j[1] for j in Indices]
    C2 = [Criterios2[j] for j in Indices]
    C1 = [Criterios1[j] for j in Indices]
    L = [L[j] for j in Indices]
    Indices=range(len(L))
    Indices=sorted(zip(C2,Indices),reverse=True)
    Indices = [j[1] for j in Indices]
    C2 = [C2[j] for j in Indices]
    C1 = [C1[j] for j in Indices]
    L = [L[j] for j in Indices]
    Indices=range(len(L))
    Indices=sorted(zip(C2,Indices),reverse=True)
    Indices=range(len(L))
    Indices=sorted(zip(C1,Indices),reverse=True)
    Indices = [j[1] for j in Indices]
    C1 = [C1[j] for j in Indices]
    L = [L[j] for j in Indices]  
   
    #elimina tweets "iguales"    
    for m in range(1,len(L)):
        if m<len(L):
            for n in range(0,m):
                if n<m:
                    if similar(L[m][2],L[n][2])>0.75:
                        try:
                            if L[m][1]==L[n][1] and Influenciadores[L[m][1]]>0:
                                Influenciadores[L[m][1]]=max(0,Influenciadores[L[m][1]]-1)
                            del L[m];
                            m=m-1;  
                        except:
                            pass
    
    TheList=L[:int(math.modf(len(L)*0.85)[1])]
    TheList = sorted(TheList, key=lambda x:x[3], reverse=True)
    o, p = len(L), k
    Lists=[[0 for x in range(o)] for y in range(p)]
    Lists[count1-1]=TheList
    pickle.dump(Lists, open('Lists', "wb" ))
    L={index:l for index,l in enumerate(L)}
    i=len(L)

        
InfluenciadoresTest=[q[1] for q in TheList]
for I in InfluenciadoresTest:
    try:
        if Influenciadores[I]<0:
            Influenciadores[I]-=1
        else:
            Influenciadores[I]+=1
    except:
        Influenciadores[I]=0
        print 'nuevo ',I
pickle.dump(Influenciadores, open('Influenciadores', "wb" ))

for t in TheList:
    print ''.join([t[0],'\n',t[1],'\n',t[2],'\n\n'])
        
File='Ambiente.txt';
for t in TheList: 
    with open(File, 'a') as dest:
                T=''.join(['\n', t[2].encode('utf-8')])
                dest.write(T) 
                
#F=dict((I,q) for I,q in Influenciadores.items() if q>3)



    
    
    
    
    
    
    
    
    