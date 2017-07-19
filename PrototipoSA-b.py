# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 10:37:49 2017

@author: juang
"""

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from utils import sigmoid, normalize, similar
from datetime import date,timedelta,datetime
from difflib import SequenceMatcher
from __future__ import division
from dateutil import parser
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
import nltk
import pdb
import os

os.path.dirname(os.path.abspath(__file__))

"""Se el diccionario de palabras que identifican al tema ambiental A y el
diccionario de influenciadores del tema"""
A = pickle.load( open( './Data/A', "rb" ) )
Influ = pickle.load( open( './Data/InfluenciadoresC', "rb" ) )

"""Se Cargan las credenciales de acceso al api de twitter"""
ACCESS_TOKEN = u'817383621397008384-TXP2pfAr0aLmr3E9Le3tDBlMSsUTQF9'
ACCESS_SECRET = u'oBXXy2cmyZ80PUm6EhUHGAs7SRb13HxYO5TWj2fq9AYVN'
CONSUMER_KEY = u'kpKOxDTCtWI8ueapP6JSySgfM'
CONSUMER_SECRET = u'ep7Di6fA1izMlQdQXBmcKiGT0q7PoXX2nDgaxFHjihA2ofgaAu'
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

"""Se lee la cuenta de twitter hasta 200 tweets del Timeline"""
twitter = Twitter(auth=oauth)
MorroTL=twitter.statuses.home_timeline(count=200)

"""Lista palabras que identifican tema ambiental y texto con palabras 
separadas por coma"""
LA=A.keys()
tx=",".join(LA)

"""Datetime de hace una hora al momento de comenzar a correr"""
One_hour_ago = datetime.datetime.utcnow()-datetime.timedelta(hours = 1)

"""Especifica el conjunto actual de mayores influenciadores - cuantil 25 superior"""
Influencers=Influ
for I in Influencers.keys():
    Influencers[I].append((Influencers[I][4]*4/3+Influencers[I][5])/2.3)
Influenciadores={I:Influencers[I] for I in Influencers if Influencers[I][6]>0.75}





#F=Influenciadores.items()
#Indices=list()
#for i in range(len(F)):
#    if isinstance(F[i][1], int):
#        Indices.append(i)
#F1 = [F[i] for i in enumerate(F) if i not in Indices]
#F11=[f for f in F1 if f[1][3]>0]
#F2 = sorted(F11, key=lambda k: k[1][2], reverse=True)





