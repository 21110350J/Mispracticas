# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:28:13 2023

@author: Jose Cruz TP
"""

#Aqui lo que vemos es que vemos es que nosotros a ponerle a if nos dara la resouesta
#Y en este ejercicio buscamos agregar dos condiciones mas
edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 18:
	print('Eres menor de edad.')
elif edad > 18 and edad <= 45:
	print('Eres mayor de edad.')
elif edad > 45 and edad <= 100:
	print('Eres mayor de edad, pero eres un chavoruco.')
elif edad > 100 and edad <= 120:
	print('¿Comó sigues vivo?.')
else:
	print('Edad no válida.')