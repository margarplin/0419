# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 13:57:03 2023

@author: Margaret Lin
"""

def maxNumber(a,b):
    return a if a>b else b

def minNumber(a,b):
    return a if a<b else b

def max(x,y,z):
    if x>y:
        max=x
    else:
        max=y
    return z if max < z else max

big = max(333,555,777)
print(big)
large=maxNumber(9,4)
small=minNumber(1,7)

print(f"large:{large}")
print(f"smaLl:{small}")