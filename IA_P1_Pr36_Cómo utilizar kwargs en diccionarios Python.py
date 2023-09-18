# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 00:04:02 2023

@author: Jose Cruz TP
"""

#Aqui vamoa a ver un ejemplo de kwargs
def colores (**kwargs):
	print("Este es el color " + kwargs['color1'] + '.')

colores(color1='rojo', color2='azul')