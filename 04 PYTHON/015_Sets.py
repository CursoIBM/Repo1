


#   SETs, conjuntos

"""
Un conjunto es una colección de elementos únicos que no está ordenada ni indexada, 
por lo que no puede estar seguro de en qué orden aparecerán los elementos. 
En Python, los conjuntos se escriben entre llaves.
Una vez que se crea un conjunto, no puede cambiar sus elementos, pero puede agregar nuevos elementos.
"""

#   Declaración:

mi_conjunto  = {"Angel", "Sara", "Pilar"}
mi_conjunto2 = {"Angel", "Manolo", "Juan"}

#   Otra forma de declararlo

mi_conjunto3 = set(("Angel", "Sara", "Pilar")) 
print(mi_conjunto3)


#   Para añadir un nuevo elemento:

mi_conjunto.add("Antonio")

#   Para añadir varios elementos:
    
mi_conjunto.update({"Fran", "María"})

#   Unión de colecciones. Si hay algún valor repetido sólo aparecerá una vez.

union= mi_conjunto | mi_conjunto2

#   Intersección de conjuntos:

interseccion= mi_conjunto & mi_conjunto2

#   Nos crea otro conjunto con los valores que estaban duplicados en ambos conjuntos. 
#   En nuestro caso sólo Angel.

#   Diferencia de conjuntos. Nos crea otro conjunto con los elementos que no están duplicados.

diferencia= mi_conjunto - mi_conjunto2

#   Para comprobar si un elemento está en un conjunto:

"Angel" in mi_conjunto		#   Devuelve true o false

#   Recorra el conjunto e imprima los valores:

miSet = {"manzana", "banana", "cereza"}

for x in miSet:
  print(x)

"""
No puede acceder a los elementos de un conjunto haciendo referencia a un índice, 
ya que los conjuntos no están ordenados, los elementos no tienen índice.
"""

#   Obtenga la cantidad de elementos en un conjunto:

miSet = {"manzana", "banana", "cereza"}

print(len(miSet))

#   Elimine "banana" utilizando el método remove() :

miSet = {"manzana", "banana", "cereza"}

miSet.remove("banana")

print(miSet)

#   Elimine "banana" utilizando el método discard() :

miSet = {"manzana", "banana", "cereza"}

miSet.discard("banana")

print(miSet)

"""
Si el elemento a eliminar no existe, remove() generará un error.
Si el elemento a eliminar no existe, discard() NO generará un error.
"""

#   Elimine el último elemento utilizando el método pop() :
"""También puede usar el método pop() para eliminar un elemento, 
pero este método eliminará el último elemento. 
Recuerde que los conjuntos no están ordenados, 
por lo que no sabrá qué elemento se elimina.
"""

miSet = {"manzana", "banana", "cereza"}

x = miSet.pop()

print(x)

print(miSet)

#   El método clear() vacía el conjunto:

miSet = {"manzana", "banana", "cereza"}

miSet.clear()

print(miSet)

#   La palabra clave del borrará completamente el conjunto:

miSet = {"manzana", "banana", "cereza"}

del miSet

print(miSet)

#   Unión de conjuntos
#   El método union() devuelve un nuevo conjunto con todos los elementos de ambos conjuntos:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#   El método update() inserta los elementos en set2 en set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#   Tanto union() como update() excluirán cualquier elemento duplicado.

















