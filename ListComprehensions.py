# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 11:05:04 2017

@author: HP
"""

x = int(input())
y = int(input())
z = int(input())
n = int(input())
p =[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if( i+j+k != n )]