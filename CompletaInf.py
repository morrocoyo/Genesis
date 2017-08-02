# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 11:06:02 2017

@author: juang
"""

from __future__ import division
from scipy.stats import lognorm
#from sklearn import datasets, linear_model
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from utils import sigmoid, normalize, normalizeLogN, similar
from datetime import date,timedelta,datetime
from difflib import SequenceMatcher
from dateutil import parser
import numpy as np
#import CuentaTema
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
#para hacer debug parcial
import time
import math
import operator
import nltk
import pdb
import os


os.path.dirname(os.path.abspath(__file__))

"""Se carga el diccionario de influenciadores del tema"""
#Influ={I:Influenciadores[I] for I in Influenciadores.keys() if isinstance(Influenciadores[I], int)==False}
Influ = pickle.load( open( './Data/InfluenciadoresC', "rb" ) )

"""Se Cargan las credenciales de acceso al api de twitter"""
ACCESS_TOKEN = u'817383621397008384-TXP2pfAr0aLmr3E9Le3tDBlMSsUTQF9'
ACCESS_SECRET = u'oBXXy2cmyZ80PUm6EhUHGAs7SRb13HxYO5TWj2fq9AYVN'
CONSUMER_KEY = u'kpKOxDTCtWI8ueapP6JSySgfM'
CONSUMER_SECRET = u'ep7Di6fA1izMlQdQXBmcKiGT0q7PoXX2nDgaxFHjihA2ofgaAu'
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter = Twitter(auth=oauth)

"""Actualiza el el numero de seguidores y el ratio #seguidores/#tweets de cada usuario"""
j=0
Mult=[899*r for r in range(11)[1:11]]
start = time.time()
for I in Influ.keys():
    if j in Mult:
       time.sleep(905)
    try:
       In=twitter.users.lookup(screen_name=I)
       #Diccionario de Influenciadores comprende id,seguidores,seguidores/tweets,score_inicial,score
       Influ[I][1]=In[0]['followers_count']
       Influ[I][1]=In[0]['followers_count']/In[0]['statuses_count']
    except:
       pass
    j+=1
end = time.time() 

"""Rankea el score de cantidad de veces que ha tuiteado el usuario"""
Scores=[s[3] for s in Influ.values() if s[3]>0 and s[3]<200]                    #habrá que recalibrar el 200
ZScores=normalizeLogN(Scores)
Score={Scores[j]:lognorm.cdf(ZScores[j],1,loc=0,scale=1) for j in range(len(Scores))}
for I in Influ.keys():
    if Influ[I][3]<0:
        Influ[I][4]=-1
    elif Influ[I][3]==0:
        Influ[I][4]=0
    elif Influ[I][3]>=200:
        Influ[I][4]=1
    else:
        Influ[I][4]=Score[Influ[I][3]]


"""Rankea el score de cantidad de veces que ha tuiteado el usuario"""
Scores2=[s[2] for s in Influ.values() if s[2]>0 and s[2]<10 and s[3]>0]
ZScores2=normalizeLogN(Scores2)
Score2={Scores2[j]:lognorm.cdf(ZScores2[j],1,loc=0,scale=1) for j in range(len(Scores2))}
for I in Influ.keys():
    if Influ[I][3]<0:
        Influ[I].append(-1)
    elif Influ[I][2]==0 or Influ[I][3]==0:
        Influ[I].append(0)
    elif Influ[I][2]>=10 and Influ[I][3]>0:
        Influ[I].append(1)
    else:
        Influ[I].append(Score2[Influ[I][2]])




#F=Influenciadores.items()
#Indices=list()
#for i in range(len(F)):
#    if isinstance(F[i][1], int):
#        Indices.append(i)
#F1 = [F[i] for i in enumerate(F) if i not in Indices]
#F11=[f for f in F1 if f[1][3]>0]
#F2 = sorted(F11, key=lambda k: k[1][2], reverse=True)
#Scores2=[v[1][2] for v in F2]
#ZScore2=normalize(Scores2)
#Score2={Scores2[j]:sigmoid(ZScore2[j]) for j in range(len(Scores2))}


#fig = plt.figure()
#plt.scatter(Puntajes1,Puntajes2)
#plt.plot(L,m*L+b, color = 'g',linewidth=3.0 )
#plt.xlabel('Puntajes 1', fontsize=18)
#plt.ylabel('Puntajes 2', fontsize=18)







