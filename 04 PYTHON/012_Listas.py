

#   LISTAS

"""
La lista es un tipo de colección ordenada y modificable. 
Es decir, una secuencia de valores de cualquier tipo, ordenados y de tamaño variable.
Se escriben entre corchetes. []
"""

miLista=["Angel", 43, 667767250] 
miLista2 = [22, True, "una lista", [1, 2]]

#   MÉTODOS DE LAS LISTAS

#   Hacer una lista de una cadena
miLista = list("PYTHON")
print(miLista)

#   Acceder a los elementos de una lista
miLista = [22, True, "una cadena", [1, 2]]
print(miLista[0])

miLista = [[1,2] , [3,4] , [5,6]]
miVar = miLista[1,1]
print(miVar)

#   Función con una lista como parámetro

def miFunccion(listaFrutas):
      for x in listaFrutas:
        print(x)

frutas = ["Manzana", "banana", "cereza"]

miFunccion(frutas)

