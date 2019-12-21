# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:55:14 2019

@author: CEC
"""

#full= np.full((2,2),8)
#print(full)

#espacio1 = np.arange(0,30,5)
#print(espacio1)

#espacio2 = np.linspace(0,2,5)
#print(espacio2)

#identidad1 = np.eye(4,4)
#print (identidad1)
#
#identidad2 = np.identity(4)
#print (identidad2)

#a= np.array([(1,2,3),(4,5,6)])
#print(a.ndim)

# funciones de typo
#a= np.array([(1,2,3)])
#print(a.dtype)

# funciones de tamaño y forma
#a = np.array([(1,2,3,4,5,6)])
#print(a.size)
#print(a.shape)

# cambiar dimensiones de matriz
#import numpy as np
#a= np.array([(8,9,10),(11,12,13)])
#print(a)
#print("\n"*2)
#a= a.reshape(3,2)
#print(a)

# orden especifico de una matriz
#import numpy as np
#a = np.array([(1,2,3,4),
#              (3,4,5,6)])
#print(a)
#print("\n"*1)
#print(a[1,3])

# otras opciones, recuerde la indexacioncomienza en cero
#import numpy as np
#a = np.array([(1,2,3,4),
#              (3,4,5,6)])
#print(a[0:,0])
#print(a[0:,1])
#print(a[0:,2])

#import numpy as np
#a=np.array([2,4,8])
#print(a.min())
#print(a.max())
#print(a.sum())

#import numpy as np
#a = np.array([(1,2,3),(3,4,5)])
#print ("\n"*2)
#print(np.sqrt(a))
#print("\n"*2)
#print(np.std(a))

# operaciones en una matriz
#import numpy as np
#x = np.array([(1,2,3),
#             (3,4,5)])
#y= np.array([(1,2,3),
#             (3,4,5)])
#print(x+y)
#print("\n")
#print(x-y)
#print("\n")
#print(x*y)
#print("\n")
#print(x/y)
#print("\n")

import numpy as np
a= np.array([[1,2],[3,4]])
b= np.array([[11,12],[13,14]])
print(np.dot(a,b))


# https://numpy.org/doc/
#ejemplos de uso numpy....revisar


