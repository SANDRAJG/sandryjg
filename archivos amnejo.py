# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:29:26 2019

@author: CEC
"""

# Manejo de ARCHIVOS
file = open("devices.txt", "r")
for item in file:
    item = item.strip()
    print(item)
file.close()