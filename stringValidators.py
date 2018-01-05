# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 22:14:22 2017

@author: HP
"""

s = input()
print(any(i.isalnum() for i in s))
print(any(i.isalpha() for i in s))
print(any(i.isdigit() for i in s))
print(any(i.isupper() for i in s))
print(any(i.islower() for i in s))
