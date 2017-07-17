# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 11:06:02 2017

@author: juang
"""

from __future__ import division
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from utils import sigmoid, normalize, similar
from datetime import date,timedelta,datetime
from difflib import SequenceMatcher
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
import operator
import nltk
import pdb
import os

os.path.dirname(os.path.abspath(__file__))

"""Se el diccionario de palabras que identifican al tema ambiental A y el
diccionario de influenciadores del tema"""
A = pickle.load( open( './Data/A', "rb" ) )
Influenciadores = pickle.load( open( './Data/Influenciadores', "rb" ) )

"""Se Cargan las credenciales de acceso al api de twitter"""
ACCESS_TOKEN = u'817383621397008384-TXP2pfAr0aLmr3E9Le3tDBlMSsUTQF9'
ACCESS_SECRET = u'oBXXy2cmyZ80PUm6EhUHGAs7SRb13HxYO5TWj2fq9AYVN'
CONSUMER_KEY = u'kpKOxDTCtWI8ueapP6JSySgfM'
CONSUMER_SECRET = u'ep7Di6fA1izMlQdQXBmcKiGT0q7PoXX2nDgaxFHjihA2ofgaAu'
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

"""Se lee la cuenta de twitter hasta 200 tweets del Timeline"""
twitter = Twitter(auth=oauth)

Scores=Influenciadores.values()
Scores=[s for s in Scores if s>=0]
ZScore=normalize(Scores)
Score={Scores[j]:sigmoid(ZScore[j]) for j in range(len(Scores))}











