#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 14:05:49 2017

@author: tata
"""

from __future__ import division
import pdb #para hacer debug parcial
try:
    import json
except ImportError:
    import simplejson as json
# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
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
import numpy as np
#import CuentaTema
from difflib import SequenceMatcher

Influ = pickle.load(open('./Data/InfluenciadoresC', "rb" ) )

#Defino cauntil
q=0.95
Influencers=Influ
for I in Influencers.keys():
    Influencers[I].append((Influencers[I][4]*4/3+Influencers[I][5])/2.3)
Influenciadores={I:Influencers[I] for I in Influencers if Influencers[I][6]>q}
#Se halla percentil q 


ACCESS_TOKEN = u'817383621397008384-TXP2pfAr0aLmr3E9Le3tDBlMSsUTQF9'
ACCESS_SECRET = u'oBXXy2cmyZ80PUm6EhUHGAs7SRb13HxYO5TWj2fq9AYVN'
CONSUMER_KEY = u'kpKOxDTCtWI8ueapP6JSySgfM'
CONSUMER_SECRET = u'ep7Di6fA1izMlQdQXBmcKiGT0q7PoXX2nDgaxFHjihA2ofgaAu'
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter = Twitter(auth=oauth)

seguidores=list()
R_id_followers=dict()
R_id_followers['next_cursor']=-1
while R_id_followers['next_cursor'] != 0:
    R_id_followers = twitter.followers.ids(screen_name = Inf_q.keys()[0],cursor=R_id_followers['next_cursor'])
    seguidores=seguidores+R_id_followers['ids']  
    
pt=Influenciadores.keys()  
pt_2 = []

j=1
for i in range(2,5):
    seguidores=list()
    R_id_followers = dict()
    R_id_followers['next_cursor']=-1
    while R_id_followers['next_cursor'] != 0:
        R_id_followers = twitter.followers.ids(screen_name = pt[i],
        cursor=R_id_followers['next_cursor'])
        j+=1
        seguidores=seguidores+R_id_followers['ids']       
    pt_2.append(seguidores)
    if j==15:
        time.sleep(905)
        j=1
            


