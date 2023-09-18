# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 23:34:30 2023

@author: Jose Cruz TP
"""
#En este codigo lo que vamos a realizar es eliminar info de los tcaldos para solo quedarnos con un dato
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclado1
del teclado2['Categoría']
del teclado2['Precio']
print(teclado2['Modelo'])