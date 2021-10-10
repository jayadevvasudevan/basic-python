# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 01:13:59 2021

@author: SHRIDHAR KAPSE
"""

import random
n=20
cn=int(n*random.random())+1
gn=0
 
while gn != cn:
    gn=int(input("New number:"))
    if gn>0:
        if gn>cn:
            print("number is too bigg")
        elif gn<cn:
            print("number is too small")
    else:
        print("you are not interested it seems")
        break
        
else:
  print("congratulation u have guessed it correctlly")
 
 