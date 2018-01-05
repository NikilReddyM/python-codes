# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 18:38:16 2017

@author: HP
"""

def no_idea(arr,pos,neg):
    happiness = 0
    for i in arr:
        if i in pos:
            happiness += 1
        if i in neg:
            happiness -= 1
    return happiness  

n,m = map(int,input().split())
arr = map(int,input().split())
pos = map(int,input().split())
neg = map(int,input().split())
print(no_idea(arr,pos,neg))