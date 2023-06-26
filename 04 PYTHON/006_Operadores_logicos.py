

a = True
b = False
resultado = a and b
# print(resultado)

resultado = a or b
# print(resultado)

resultado = not a
print(resultado)

#----------------------------------
# Sintaxis simplificada para varios operadores lógicos
edad = int(input('Introduce tu edad: '))

#veintes = edad >= 20 and edad < 30
#print(veintes)
#treintas = edad >= 30 and edad <40
#print(treintas)

if ( 20 <= edad < 30) or (30 <= edad <40):
    print('Dentro de rango (20\'s) o (30\'s)')
#    if veintes:
#        print('Dentro de los 20\'s')
#    elif treintas:
#        print('Dentro de los 30\'s')
#    else:
#        print('Fuera de rango')
else:
    print("No está dentro de los 20's ni 30's")


