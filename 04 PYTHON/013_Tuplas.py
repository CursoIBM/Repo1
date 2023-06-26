


#   TUPLAS

"""Una tupla es una colección ordenada e inmutable. 
En Python, las tuplas se escriben entre paréntesis.
"""

#       Declaración de una tupla

miTupla = ("manzana", "banana", "cereza")
print(miTupla[1])

#   Otra forma de declararla

miTupla = tuple(("manzana", "banana", "cereza"))
print(miTupla)


#   Indexación Negativa

miTupla = ("manzana", "banana", "cereza")
print(miTupla[-1])

#   Rango de índices
#   Devuelve el tercer, cuarto y quinto elemento:

miTupla = ("manzana", "banana", "cereza", "naranja", "kiwi", "melon", "mango")
print(miTupla[2:5])

#   Convierta la tupla en una lista para poder cambiarla:

miTupla = ("manzana", "banana", "cereza")
miLista = list(miTupla)
miLista[1] = "kiwi"
miTupla = tuple(miLista)

print(miTupla)

#   Recorrer una tupla

miTupla = ("manzana", "banana", "cereza")
for x in miTupla:
  print(x)

#   Comprobar si existe un elemento
#   Compruebe si "manzana" está presente en la tupla:

miTupla = ("manzana", "banana", "cereza")
if "manzana" in miTupla:
  print("Sí, 'manzana' está en la tupla.")

#   Otra forma, simplemente con un boolean

print("manzana" in miTupla) 

#   Longitud de la tupla

miTupla = ("manzana", "banana", "cereza")
print(len(miTupla))


# Unir dos tuplas

tupla1 = ("a", "b" , "c")
tupla2 = (1, 2, 3)

tupla3 = tupla1 + tupla2
print(tupla3)

#   Cuantas veces se encuentra el elemento 4 en miTupla?

miTupla = ("manzana", "banana", "cereza" , "manzana")
print(miTupla.count("manzana"))	

#   Desempaquetdo de tupla

miTupla=("Angel", 4, 5.345, True, 4)
nombre, num1, num2, valor1, num3=miTupla

print(nombre)
print(num1)
print(num2)
print(valor1)
print(num3)







