# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 11:10:52 2017

@author: HP
"""
def minion_game(x):
    l = len(x)
    vowels = "A E I O U".split()
    kevin = 0
    stuart = 0
    for i in range(l):
        if x[i] in vowels:
            kevin += l-i
        else:
            stuart += l-i
    if kevin > stuart:
        print("kevin",kevin)
    elif kevin < stuart:
        print("stuart",stuart)
    else:
        print("Draw")
        
    
s=input()
minion_game(s)