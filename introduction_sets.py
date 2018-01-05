# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 17:40:23 2017

@author: HP
"""


def average(arr):
    return (sum(set(arr))/len(set(arr)))
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)