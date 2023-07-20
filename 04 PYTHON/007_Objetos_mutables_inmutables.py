


  
#   Obtener la dirección de memoria de una variable

a = 65
print("La dirección de memoria es" , id(a))

#   Obtener la dirección de memoria de una variable que apunta a otra

miNumero = 65
miNumero2 = miNumero
print("La dirección de memoria es" , id(miNumero))
print("La dirección de memoria es" , id(miNumero2))

#   Si cambio la variable, realmente creo una copia en otra dirección de memoria:

a = 65
print("La dirección de memoria es" , id(a))
a+=2
print("La dirección de memoria es" , id(a))

#   Obtener la dirección de memoria de una tupla
a = (1, 2, 3, 4, 5)
print("La dirección de memoria es" , id(a))

#   Obtener la dirección de memoria de una lista

a = [1, 2, 3, 4, 5]
print("La dirección de memoria es" , id(a))  

#   Obtener la dirección de memoria de un diccionario
a = {'a': 1, 'b': 2}
print(a)
print("La dirección de memoria es" , id(a))

a["c"] = 3
print(a)
print("La dirección de memoria es" , id(a))