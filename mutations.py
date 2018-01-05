# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 21:36:58 2017

@author: HP
"""

def mutations(string, position, character):
    print(string[:position]+character+string[position+1:])
    
string = input()
temp = input().split()
mutations(string,int(temp[0]),temp[1])
