# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 20:55:46 2017

@author: HP
"""

#!/bin/python3

def maximizeProfit(a, b, m, k):
    max = m*k
    for i in range(len(a)):
        if a[i]*b[i]*m>max:
            max = a[i]*b[i]*m
    return max

if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    result = maximizeProfit(a, b, m, k)
    print(result)
    