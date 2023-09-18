# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 20:25:27 2023

@author: Jose Cruz TP
"""
#Aqui vamos a eliminar algunos elementos con la funcion pop y mostrarlos en una nueva
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
#La funcion pop 
color1 = colores.pop(1)
color2 = colores.pop(-2)
#y mostramos en una nueva lista 

colores_eliminados = [color1, color2]
print(colores_eliminados)