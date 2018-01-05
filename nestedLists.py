# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 21:27:56 2017

@author: HP
"""
from operator import itemgetter
l=[]
n = int(input())
for i in range(n):
    l.append([input(),float(input())])
    
l=sorted(l,key = itemgetter(1,0))
sl = sorted(list(set([i[1] for i in l ])))
output = [i[0] for i in l if(i[1] == sl[2])]
for i in output:
    print(i)
    