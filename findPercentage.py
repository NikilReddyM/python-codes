# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 10:32:23 2017

@author: HP
"""

n= int(input())
dict= {}
for i in range(n):
    temp = input().split()
    dict[temp[0]]=list(map(int,temp[1:]))
print('%.2f'%(sum(dict[input()])/3))
