# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 22:13:04 2017

@author: HP
"""

def capitalize_line(x):
    for i in range(len(x)):
        x[i] = x[i].capitalize()
    x = ' '.join(x)
    return(x)
    
print(capitalize_line(input().split(' ')))
