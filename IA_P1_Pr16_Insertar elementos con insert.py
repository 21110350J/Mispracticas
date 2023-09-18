# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 20:41:31 2023

@author: Jose Cruz TP
"""

#Aqui vamos a utilizar insert para agregar elementos con un posicion definida 
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
#Añade a la siguiente lista los colores 'magenta' y 'turquesa' utilizando insert().
colores.insert(-4, 'magenta')
colores.insert(-1, 'turquesa')

print(colores)