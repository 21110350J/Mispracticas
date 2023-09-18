# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 00:07:32 2023

@author: Jose Cruz TP
"""

#Aqui vamos a ver un ejemplo poo
class Usuario:
	nombre = ''
	apellidos = ''

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = Usuario()

usuario001.nombre = 'José Cruz'
usuario001.apellidos = 'Torres Palomares'

usuario001.imprime_datos()