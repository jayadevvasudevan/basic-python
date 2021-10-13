# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 16:07:58 2021

@author: SHRIDHAR KAPSE
"""



s="no man's land"
n =len(s)
firstPartOfStr =""
secondPartOfStr =""
if(n%2==0):
    firstPartOfStr=s[0:int((n/2))]
    secondPartOfStr=s[int((n/2)):(n)]
else:
    firstPartOfStr=s[0:int((n+1/2))]
    secondPartOfStr=s[int((n+1/2)):(n)]
print(firstPartOfStr+secondPartOfStr[::-1])