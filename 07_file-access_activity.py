# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:43:04 2019

@author: CEC
"""

file = open("devices.txt", "a")
while True:
    newItem= input("Ingrese nuevo Item:")
    
    if newItem == "exit":
        print("All done!")
        break
    
    file.write(newItem+"\n")
    
file.close()

#otra forma

file=open("devices.txt","a")
while True:
    newItem = input("Ingrese un nuevo item: ")
    file.write(newItem + "\n") 
    if newItem == 'exit':
        print("todo Listo!!")
        break

file.close()

#corrección otra forma

file=open("devices.txt","a")
while True:
    newItem = input("Ingrese un nuevo item: ")
    if newItem == 'exit':
        print("todo Listo!!")
        break
    else:
        file.write(newItem + "\n") 

file.close()
