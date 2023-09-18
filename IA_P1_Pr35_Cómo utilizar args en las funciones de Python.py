# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 23:56:06 2023

@author: Jose Cruz TP
"""

#*args es como un comodín con un número ilimitado de usos (al menos, no he llegado a encontrarle un límite), por ejemplo, si le pasas cuatro argumentos en la llamada como en el ejemplo, *args equivale a cuatro argumentos.
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores('rojo', 'azul')

def suma(*args):
	resultado = args[0] + args[1] + args[2] + args[3] + args[4]
	print('El resultado de sumar estos cinco números es:', resultado)

suma(16, 20, 13, 9083, 1, 2)