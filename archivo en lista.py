# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:32:46 2019

@author: CEC
"""

devices = []
file = open("devices.txt", "r")
for item in file:
    item = item.strip()
    devices.append(item)
file.close()
print(devices)