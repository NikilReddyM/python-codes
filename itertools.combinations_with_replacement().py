# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 13:58:39 2017

@author: HP
"""
from itertools import combinations_with_replacement
a = input().split()
for i in combinations_with_replacement(sorted(a[0]),int(a[1])):
    print(''.join(i))
