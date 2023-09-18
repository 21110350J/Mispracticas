# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 00:12:25 2023

@author: Jose Cruz TP
"""

class Usuario:
	def __init__(self, nombre, apellidos):
		self.nombre = nombre
	self.apellidos = apellidos

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = Usuario('Enrique', 'Barros Fernández')

usuario002 = Usuario('Javier', 'Gomila Reyes')