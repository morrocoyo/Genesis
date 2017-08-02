# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 12:51:47 2017

@author: juang
"""

from difflib import SequenceMatcher
from utils import normalize, similar
from dateutil import parser

def Repetidos(Lista, Influ):
    co=0 
    IndRep=list();
    for m in range(1,len(Lista)):
        for n in range(0,m):
            if m not in IndRep:
                if similar(Lista[m][2],Lista[n][2])>0.72:
                    try:
                        if Lista[m][1]==Lista[n][1] and Influ[Lista[m][1]][3]>=0:
                            IndRep.append(m)
                    except:
                        pass
    Lista = [r for q, r in enumerate(Lista) if q not in IndRep]    #elimina los indices de IndRep
    return Lista   