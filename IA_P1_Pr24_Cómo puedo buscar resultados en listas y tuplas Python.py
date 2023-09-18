# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:35:08 2023

@author: Jose Cruz TP
"""
#En este codigo vamos a usa las tuplas para confirmar en orden si el color
#Que escribamos es el correcto o si no que no esta admitido 
colores = input("Introduce un color:\n")
tupla_colores = ("morado", "violeta", "naranja", "negro")
#condicionales de que se cumplan nuestos colores
if colores in tupla_colores[0]:
    print("El color morado esta en la lista")
elif colores in tupla_colores[1]:
    print("El color violeta esta en la lista")
elif colores in tupla_colores[2]:
    print("El color naranja esta en la lista")
elif colores in tupla_colores[3]:
    print("El color negro esta en la lista")
else:
    print("color no admitido")