# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 14:13:40 2021

@author: SHRIDHAR KAPSE
"""

def add(x):
    sum=0
    for i in x:
        sum=sum+i
    return sum

# number of elements
n = int(input("Enter number of elements : "))
 
# Below line read inputs from user using map() function
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
 
print("Sum of The numbers entered is : ", add(a))