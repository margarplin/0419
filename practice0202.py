# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:51:44 2023

@author: Margaret Lin
"""

#pratice 0201 take 5 input integers and print the sum up result
#use for loop 
a=0
for i in range(1,6):
    print(i)
    x = input("enter a number:")
    print(f"{i}")
    a = a+int(x)
print (f"the result={a}")
