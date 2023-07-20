


# Módulos

"""
Para llamar a una función que tengamos en un módulo tenemos que importarla y luego 
usar la nomenclatura del punto:
Suponiendo que en un módulo funciones.py tenemos la siguiente función suma:
"""
def suma(num1, num2):
    print("suma= ", num1+num2)
    
#   Desde otro módulo la llamaríamos así:

import funciones
funciones.suma(3,4)	#Además de importar debemos usar la nomenclatura del punto.


#   Para simplificar también podemos poner:

from funciones import suma
suma(3,4)

#   De esta forma, además, ya no necesitamos usar la nomenclatura del punto.

# ---------------------------------------


#   Si queremos importar todo el contenido de un paquete:

from funciones import *

#   La función dir() enumera todos los elementos de un módulo. 

import funciones

x = dir(funciones)
print(x)
2400