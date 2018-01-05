# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 23:28:38 2017

@author: HP
"""

x= set(input().split())
y = int(input())
count = 0
for i in range(y):
    if x>set(input().split()):
        count += 1
print(count == y)
        