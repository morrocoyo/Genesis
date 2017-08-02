# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 10:37:49 2017

@author: juang
"""

from __future__ import division
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from utils import sigmoid, normalize, similar
from datetime import date,timedelta,datetime
from difflib import SequenceMatcher
from CargaTweet import CargaTweet
from Repetidos import Repetidos
from dateutil import parser
from CuentaTemaa import *
try:
    import json
except ImportError:
    import simplejson as json
import unicodedata
import re, string
import datetime
import operator
import pickle
import time
import math
import nltk
import pdb                                                                  #para hacer debug parcial pdb.set_trace()
import os

os.path.dirname(os.path.abspath(__file__))
#start = time.time()

"""Carga el diccionario de palabras que identifican al tema ambiental A y el
diccionario de influenciadores del tema"""
A = pickle.load(open('./Data/A', "rb" ) )
Influ = pickle.load(open('./Data/InfluenciadoresC', "rb" ) )
TweetsAmb = pickle.load(open('./Data/TweetsAmb', "rb" ) )
#Imprime ultimos tweets históricos
Ahora=datetime.datetime.utcnow()
for t in TweetsAmb[0:5]:
    if not not t[13]:
        print ''.join([t[13], u' retwiteó'])
    if (Ahora-parser.parse(t[8]).replace(tzinfo=None)).seconds/60 < 1:
        tiempo=('%f' % round((Ahora-parser.parse(t[8]).replace(tzinfo=None)).seconds))
        print ''.join([t[0],' @',t[1],' '+tiempo + ' seg','\n',t[2],'\n', t[7],'\n', t[18],'\n'])
    elif (Ahora-parser.parse(t[8]).replace(tzinfo=None)).seconds >= 60 and \
        (Ahora-parser.parse(t[8]).replace(tzinfo=None)).seconds < 3600:
        tiempo=('%f' % round((Ahora-parser.parse(t[8]).replace(tzinfo=None)).seconds/60)).rstrip('.0')
        print ''.join([t[0],' @',t[1],' '+tiempo + ' min','\n',t[2],'\n',t[7],'\n',t[18],'\n'])
    elif (Ahora-parser.parse(t[8]).replace(tzinfo=None)).seconds >= 86400:
        tiempo=('%f' % round((Ahora-parser.parse(t[8]).replace(tzinfo=None)).seconds/(3600*24))).rstrip('.0')
        print ''.join([t[0],' @',t[1],' '+tiempo + ' días','\n',t[2],'\n',t[7],'\n',t[18],'\n'])
    else:
#        tiempo=('%f' % round((Ahora-parser.parse(t[8]).replace(tzinfo=None)).seconds/3600)).rstrip('.0')
        tiempo=str(round((Ahora-parser.parse(t[8]).replace(tzinfo=None)).seconds/3600))
        print ''.join([t[0],' @',t[1],' '+tiempo + ' horas','\n',t[2],'\n',t[7],'\n',t[18],'\n'])
print u'prox. actualización en 2 minutos'
"""Lista palabras que identifican tema ambiental y texto con palabras 
separadas por coma"""
LA=A.keys()
LAm=[l.lower() for l in LA]
tx=",".join(LA)

"""CompletaInf actualiza los scores de Influencia"""
#CompletaInf

"""Especifica el conjunto actual de mayores influenciadores - cuantil 25 superior"""
q=0.75
Influencers=Influ
for I in Influencers.keys():
    Influencers[I].append((Influencers[I][4]*4/3+Influencers[I][5])/2.3)
Influenciadores={I:Influencers[I] for I in Influencers if Influencers[I][6]>q}

"""Se Cargan las credenciales de acceso al api de twitter y se accede"""
ACCESS_TOKEN = u'817383621397008384-TXP2pfAr0aLmr3E9Le3tDBlMSsUTQFg'
ACCESS_SECRET = u'oBXXy2cmyZ80PUm6EhUHGAs7SRb13HxYO5TWj2fqgAYVN'
CONSUMER_KEY = u'kpKOxDTCtWI8ueapP6JSySgfM'
CONSUMER_SECRET = u'ep7Di6fA1izMlQdQXBmcKiGT0q7PoXX2nDgaxFHjihA2ofgaAu'
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter = Twitter(auth=oauth)

"""Datetime de hace una hora al momento de comenzar a correr y inicializan contadores"""
One_hour_ago = datetime.datetime.utcnow()-datetime.timedelta(hours = 1)
k=1                                                                            #veces que corre el ciclo globa - 15 mins
kk=1                                                                           #veces que corre subciclos de streaming dentro del ciclo global
count1=1
tweet_count = 500                                                               #tweets que lee en el streaming
i=0
L=dict()
LInf=list()
LnoInf=list()
Nuevos=list()
"""Comienza el ciclo completo"""
while (count1<=k):
    MorroTL=twitter.statuses.home_timeline(count=200)                          #lee la cuenta de twitter hasta 200 tweets del Timeline
    for tweet in MorroTL:                                                      #primer subciclo - revisa el TimeLine de morrocoyo
        try:
            L=CargaTweet(L,tweet,i)                                            #Función que carga a la lista la información relevante del tweet
            tweeted_datetime = parser.parse(L[i][3]).replace(tzinfo=None)       
            if tweeted_datetime > One_hour_ago:                                #Si es de la última hora lo aprueba            
                i+=1 
        except:
            pass
    count2=1
    while (count2<=kk):                                                        #segundo subciclo - revisa los tweets del streaming   
        twitter_stream = TwitterStream(auth=oauth)                             #lee el streaming de twitter
        iterator = twitter_stream.statuses.filter(track=tx, language="es")     #Lee el streaming en español filtrando por las palabras en tx
        if count2>1:                                                           #Cada paso de este subciclo espera más de 3 minutos
            time.sleep(90)                                                     #para volver a desactivar el límite del primer ciclo
            print u'prox. actualización en 3 minutos'
        startite = time.time()
        for tweet in iterator:
            tweet_count -= 1
            try:
                L=CargaTweet(L,tweet,i)                                        #Función que carga a la lista la información relevante del tweet
                tweeted_datetime = parser.parse(L[i][3]).replace(tzinfo=None)       
                if tweeted_datetime > One_hour_ago:                            #Si es de la última hora lo aprueba           
                    i+=1
            except:
                pass
            if tweet_count <= 0:
                break
        endite = time.time()
        print ((endite - startite)/60, 'mins') 
        count2+=1                  
        """
        Actualiza la lista de noticias relevantes y no relevantes
        """            
        for T in L.values():
            c=0
            try:
                for r in T[2].encode('utf-8').lower().split():
                    if r.lower() in LAm:
                        c+=1
                if c>0:                                                        #Si alguna palabra del tweet está en LA
                    if T[1] in Influ.keys():
                        if T[1] in Influenciadores.keys():
                            LInf.insert(0,T)
                        else:
                            LnoInf.insert(0,T)
                    else:
                        LnoInf.append(T)
                        Influ[T[1]]=[In[0]['id']]+[In[0]['followers_count']]+[In[0]['followers_count']/In[0]['statuses_count']]+[0]+[0]+[0]
                        Nuevos.append(Influ[T[1]])                                        
            except:
                pass
        #elimina tweets "iguales" 
        LInf=Repetidos(LInf,Influ)
        LnoInf=Repetidos(LnoInf,Influ)
        #Los Organiza cronológicamente
        Ahora=datetime.datetime.utcnow()
        DiferenciaTiempos=list(enumerate([Ahora-parser.parse(t[3]).replace(tzinfo=None) for t in LInf]))
        DiferenciaTiempos = sorted(DiferenciaTiempos, key=lambda k: k[1])
        Orden=[h[0] for h in DiferenciaTiempos]
        LInf=[LInf[o] for o in Orden]
        DiferenciaTiempos2=list(enumerate([Ahora-parser.parse(t[3]).replace(tzinfo=None) for t in LnoInf]))
        DiferenciaTiempos2 = sorted(DiferenciaTiempos2, key=lambda k: k[1])
        Orden2=[h[0] for h in DiferenciaTiempos2]
        LnoInf=[LnoInf[o] for o in Orden2]
        #
        for T in LInf+LnoInf:
            try:                           
                In=twitter.users.lookup(screen_name=T[1])
                Influ[T[1]][1]=In[0]['followers_count']             #actualiza  el conteo de seguidores
                Influ[T[1]][2]=In[0]['followers_count']/In[0]['statuses_count']
                Influ[T[1]][3]+=1                                       #actualiza  el contador de tweets ambientales
            except:
                pass
        TweetsAmb=LInf+LnoInf+TweetsAmb[0:30]
        Ahora=datetime.datetime.utcnow()
        for t in TweetsAmb[0:5]:
            if not not t[13]:
                print ''.join([t[13], u' retwiteó'])
            if (Ahora-parser.parse(t[8]).replace(tzinfo=None)).seconds/60 <= 1:
                tiempo=('%f' % round((Ahora-parser.parse(t[8]).replace(tzinfo=None)).seconds))
                print ''.join([t[0],' @',t[1],' '+tiempo + ' seg','\n',t[2],'\n', t[7],'\n', t[18],'\n'])
            elif (Ahora-parser.parse(t[8]).replace(tzinfo=None)).seconds >= 60 and \
                (Ahora-parser.parse(t[8]).replace(tzinfo=None)).seconds < 3600:
                tiempo=('%f' % round((Ahora-parser.parse(t[8]).replace(tzinfo=None)).seconds/60)).rstrip('.0')
                print ''.join([t[0],' @',t[1],' '+tiempo + ' min','\n',t[2],'\n',t[7],'\n',t[18],'\n'])
            elif (Ahora-parser.parse(t[8]).replace(tzinfo=None)).seconds >= 86400:
                tiempo=('%f' % round((Ahora-parser.parse(t[8]).replace(tzinfo=None)).seconds/(3600*24))).rstrip('.0')
                print ''.join([t[0],' @',t[1],' '+tiempo + ' días','\n',t[2],'\n',t[7],'\n',t[18],'\n'])
            else:
                tiempo=str(round((Ahora-parser.parse(t[8]).replace(tzinfo=None)).seconds/3600))
                print ''.join([t[0],' @',t[1],' '+tiempo + ' horas','\n',t[2],'\n',t[7],'\n',t[18],'\n'])        
    count1+=1
    pdb.set_trace()
    print ('Completa- ciclo global:'+ str(count1) + ' subciclo streaming:'+str(count2) +'\n')

#end = time.time()
#print ((end - start)/3600, 'horas') 
#print ((end - start)/60, 'mins')            

pickle.dump(Influ, open('./Data/InfluenciadoresC', "wb" ))
pickle.dump(TweetsAmb, open('./Data/TweetsAmb', "wb" ))





