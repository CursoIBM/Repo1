

#	WHILE

#   Imprime edad cuando el contador llegue a 18

edad = 0
while edad < 18: 
    edad=edad+1
print("Tienes "+str(edad))

#   Pregunta la edad mientras sea negativa

edad=int(input("Introduce edad: "))

while edad<0:
    print("Edad incorrecta")
    edad=int(input("Introduce edad: "))

print("tu edad es: "+str(edad))

#   Calcula la raiz cuadrada de un número. Tenemos tres intentos y el número no puede ser negativo.

import math;
intentos=0
num = int(input("Introduce numero: "))

while num<0:
    intentos=intentos+1
    print("Incorrecto")
    num=int(input("Introduce numero: "))

    if intentos==2:
        print("Demasiados intentos")
        break

if intentos<2:
    intentos=intentos+1
    solucion=math.sqrt(num)
    print("la raiz cuadrada de "+str(num)+ " es: "+str(solucion))

#   Bucle while con un if anidado y un break
#   Salga del bucle cuando num sea 3:

num = 1
while num < 6:
  print(num)
  if num == 3:
    break
  num += 1
  


#   en Python no existe un bucle "do-while" como tal, pero se puede lograr un 
#   comportamiento similar utilizando un bucle "while" junto con una condición de salida

# Ejemplo de bucle "do-while" en Python

# Variable de control
contador = 0

# Bucle "do-while"
while True:
    # Código que se ejecuta al menos una vez
    print("El contador es:", contador)

    # Incrementar el contador
    contador += 1

    # Verificar la condición de salida
    if contador >= 5:
        break

    # Código adicional dentro del bucle
    print("Realizando más operaciones...")

print("Fin del bucle")




