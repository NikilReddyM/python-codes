# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 20:38:29 2017

@author: HP
"""
from itertools import permutations
a = input().split()
for i in permutations(sorted(a[0]),int(a[1])):
    print(''.join(i))
