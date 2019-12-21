# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 18:50:32 2019

@author: CEC
"""

def fib(n):    # escribe la serie Fibonacci hasta n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
print()
fib(100)

#
#def fib2(n):   # devuelve la serie Fibonacci hasta n
    #resultado = []
    #a, b = 0, 1
    #while b < n:
       # resultado.append(b)
        #a, b = b, a+b
    #return resultado
#