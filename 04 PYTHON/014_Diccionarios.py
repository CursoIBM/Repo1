


#   DICCIONARIOS

"""Los diccionarios, también llamados matrices asociativas, deben su nombre a que son 
colecciones que relacionan una clave y un valor.
Un diccionario es una colección desordenada, modificable e indexada. 
En Python, los diccionarios se escriben entre llaves y tienen claves y valores.
"""

#   Declaración de un diccionario

miDiccionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(miDiccionario)


#   A los valores almacenados en un diccionario se accede por su clave

peliculas = {"Love Actually": "Richard Curtis", 
"Kill Bill": "Tarantino",
"Amélie": "Jean-Pierre Jeunet"}

peliculas["Love Actually"] 

# Reasignar valores a un diccionario

peliculas["Kill Bill"] = "Quentin Tarantino"
print(peliculas)

#   Usar una tupla dentro de un diccionario:

miDiccionario3={"nombre":"Jordan", "Equipo":"Bulls", "Anillos":[1991, 1992, 1993, 1996, 1997, 1998]}
print(miDiccionario3["Anillos"])

#   Quitar valores de un diccionario

peliculas = {"Love Actually": "Richard Curtis", 
"Kill Bill": "Tarantino",
"Amélie": "Jean-Pierre Jeunet"}

peliculas.pop("Love Actually")	

print(peliculas)

#   Crear un diccionario a partir de dos listas:

lista_claves=["nombre", "edad"]
lista_valores=["Angel", 43]
diccionario = dict(zip(lista_claves , lista_valores))
print(diccionario)

#   Para comprobar si una clave está en el diccionario:

"nombre" in diccionario		#Devuelve true o false


#   Imprima las claves del diccionario:

peliculas = {"Love Actually": "Richard Curtis", 
"Kill Bill": "Tarantino",
"Amélie": "Jean-Pierre Jeunet"}
for x in peliculas:
      print(peliculas[x])

#   Longitud de un diccionario:

peliculas = {"Love Actually": "Richard Curtis", 
"Kill Bill": "Tarantino",
"Amélie": "Jean-Pierre Jeunet"}

print(len(peliculas))

#   Agregar elementos a un diccionario:

miDiccionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
miDiccionario["color"] = "red"
print(miDiccionario)

#   Eliminar el último elemento insertado:

miDiccionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
miDiccionario.popitem()
print(miDiccionario)


#   La palabra clave del elimina el elemento con el nombre de clave especificado:

miDiccionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del miDiccionario["model"]
print(miDiccionario)


#   La palabra clave del también puede eliminar completamente el diccionario:

miDiccionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del miDiccionario
print(miDiccionario)

#   La palabra clave clear() vacía el diccionario:

miDiccionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
miDiccionario.clear()
print(miDiccionario)


      
#   Copiar un diccionario

miDiccionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
midict = miDiccionario.copy()
print(midict)


#   Otra forma de copiar un diccionario

miDiccionario = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
midict = dict(miDiccionario)
print(midict)

#   Diccionarios anidados

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child1"])


