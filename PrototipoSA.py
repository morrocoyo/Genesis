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
import CuentaTema
from difflib import SequenceMatcher
from CuentaTemaa import *
"""
La funcion CuentaTemaa define el tema mediante las palabras que más aparecen en
el archivo Ambiente.txt
"""
A=CuentaTemaa()
"""
Carga las credenciales de acceso al api de twitter
"""
ACCESS_TOKEN = u'817383621397008384-TXP2pfAr0aLmr3E9Le3tDBlMSsUTQFg'
ACCESS_SECRET = u'oBXXy2cmyZ80PUm6EhUHGAs7SRb13HxYO5TWj2fqgAYVN'
CONSUMER_KEY = u'kpKOxDTCtWI8ueapP6JSySgfM'
CONSUMER_SECRET = u'ep7Di6fA1izMlQdQXBmcKiGT0q7PoXX2nDgaxFHjihA2ofgaAu'
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
"""
Cico de Simulacion: Busqueda de tuits ambientales en Morrocoyo timeline + Streaming
"""
LA=A.keys()
twitter = Twitter(auth=oauth)
MorroTL=twitter.statuses.home_timeline(count=200)
k=1;
for i in range(k,len(MorroTL)):
     print i