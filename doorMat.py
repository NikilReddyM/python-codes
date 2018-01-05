# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 12:24:32 2017

@author: HP
"""
n,m = map(int,input().split())

""" upper part """
for i in range((n-1)//2):
    print(('.|.'*i).rjust((m-3)//2,'-')+
          '.|.'+
          ('.|.'*i).ljust((m-3)//2,'-')
          )

""" middle part """
print('WELCOME'.center(m,'-'))

""" lower part """
for i in range((n-1)//2):
    print(('.|.'*((n-1)//2-i-1)).rjust((m-3)//2,'-')+
          '.|.'+
          ('.|.'*((n-1)//2-i-1)).ljust((m-3)//2,'-')
    )
    
    