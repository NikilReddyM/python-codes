# -*- coding: utf-8 -*-

from itertools import combinations
a = input().split()
for j in range(1,int(a[1])+1):
    for i in combinations(sorted(a[0]),j):
        print(''.join(i))
