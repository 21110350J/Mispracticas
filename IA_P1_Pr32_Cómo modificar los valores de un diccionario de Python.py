# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 23:25:30 2023

@author: Jose Cruz TP
"""
#En este codigo lo que vamos hacer es que usando la liberia que ya tenemos
#con u ciclo for podemos mostarlo de forma mas ordenada 
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

for x in teclado1:
	print(x, '=', teclado1[x] + '.')