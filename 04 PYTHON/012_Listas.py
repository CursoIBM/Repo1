

#   LISTAS

"""
La lista es un tipo de colección ordenada y modificable. 
Es decir, una secuencia de valores de cualquier tipo, ordenados y de tamaño variable.
Se escriben entre corchetes. []
"""

miLista=["Angel", 43, 677777777] 
miLista2 = [22, True, "una lista", [1, 2]]

# Usando el constructor list() para hacer una Lista:
miLista = list(("Angel", 43, 677777777)) 
print(miLista)


#   MÉTODOS DE LAS LISTAS


#   Acceder a los elementos de una lista
miLista = [22, True, "una cadena", [1, 2]]
print(miLista[0])

#   Si pongo índices negativos lo que hace Python es contar desde el final 
#   hasta el principio empezando por -1
  
print(miLista[- 4])
 
#   Para imprimir toda la lista podemos poner:
print(miLista[:])

#   Listas enlazadas
miLista = [[1,2] , [3,4] , [5,6]]
miVar = miLista[1],[1]
print(miVar)



#   Hacer una lista de una cadena
miLista = list("PYTHON")
print(miLista)

#   Rango. Devuelve el tercer, cuarto y quinto elemento:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#   Cambiar el valor de un elemento:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#   Recorrer una lista 
#   Imprima todos los elementos de la lista, uno por uno:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#   Recorrer una lista buscando un elemento
#   Compruebe si "manzana" está presente en la lista:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#   Longitud de una lista 
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#   Copiar una lista 
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#   Unir dos listas:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Añade el elemento al final de la lista.
miLista = ["Manzana", "banana", "cereza"]
miLista.append("Antonio")	
print(miLista)

# Añade el elemento en la posición [2].
miLista.insert(2,"Sandra")	

# Concatena la nueva lista a la anterior.
miLista.extend(["Sara", "Diego"])	

# Elimina un elemento de la lista.
miLista.remove("Angel")	

# Elimina el último elemento de una lista.
miLista.pop()	

# Nota: pop() devuelve el elemento eliminado mientras que remove() no lo hace.








#   Función con una lista como parámetro

def miFunccion(listaFrutas):
      for x in listaFrutas:
        print(x)

frutas = ["Manzana", "banana", "cereza"]

miFunccion(frutas)


