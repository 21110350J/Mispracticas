# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 22:41:09 2023

@author: Jose Cruz TP
"""
#en este ejercicio vamos a utilizar las condiciones del while
x = 0

while x <= 30:
    x += 1
    
    # if para saltar ejecuciones del bucle
    if x == 4 or x == 6 or x == 10:
     print('Se saltó el valor ', x, ' de x')
	 
     continue
 
    # if para romper la ejecución del bucle
    if x == 15 :
        print('El valor del bucle es: ', + x)
        break
    
    
    print(x)
