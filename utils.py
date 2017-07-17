#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:52:33 2017

@author: juan
"""
from difflib import SequenceMatcher
import pandas as pd
import operator
import math
import re
import numpy as np

# Sigmoid Function
def sigmoid(x):
  return 1 / (1 + math.exp(-x))


# Relevance by length of financial info
def relevance(x):
  long = len([e for e in x if re.search('[-+]?[0-9]+$', e)])
  return long

# Normalization ~ N(0, 1)
def normalize(x):
    return (x - np.mean(x))/np.std(x)
    
# Compounded Anual Growth Rate last two valid numbers in a series
def CAGRLast(x):
    FV = x.apply(lambda y: y[y.isnull() == False][-1], axis = 1)
    FVIndex = x.apply(lambda y: y[y.isnull() == False].index[-1], axis = 1).apply(pd.to_numeric, args=('coerce',))
    IV = x.apply(lambda y: y[y.isnull() == False][-2], axis = 1)
    IVIndex = x.apply(lambda y: y[y.isnull() == False].index[-2], axis = 1).apply(pd.to_numeric, args=('coerce',))
    n = (FVIndex - IVIndex).astype(float)
    return (FV/IV)**(1/n)-1 

# Ratio of String Similarity
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
    