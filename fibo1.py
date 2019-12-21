# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 19:04:51 2019

@author: CEC
"""

def fib(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
print()
fib(50)   