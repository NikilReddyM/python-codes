# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 20:04:51 2017

@author: HP
"""

n = input()
eng = set(input().split())
m = input()
fre = set(input().split())
print(len(eng|fre))
