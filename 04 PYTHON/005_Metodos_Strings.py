
#   TRABAJAR CON STRINGS
"""Los strings son secuencias de caracteres de texto. 
Todos los objetos en Python se engloban en dos categorías: mutables o inmutables. 
Los tipos básicos mutables son las listas, los diccionarios y los sets. 
Los tipos básicos inmutables son los números, los strings y las tuplas. 
Los objetos mutables pueden ser cambiados en el mismo objeto, mientras que los inmutables no.
"""
#   Para concatenar textos se hace con “+” o simplemente con una coma.
#   Si ponemos coma nos pone entre los textos un espacio, con + no lo hace.

print("Esta frase" , "termina aquí.")
print("Esta frase " + "termina aquí.")

#   Contatenación y multiplicación de strings
a = "uno"
b = "dos"
c = a + b		 # c es "unodos"
c = a * 3 		 # c es "unounouno"


#----------------------------------------------

#   MÉTODOS DE LOS STRINGS:

#   lower(): Convierte en minúsculas un string.
s_texto1 = "ESTE TEXTO ESTÁ INICIALMENTE EN MAYÚSCULAS"
print(s_texto1.lower())

#   capitalize(): Pone la primera letra en mayúscula.
s_texto2 = "este texto no tenía la primera letra en mayúsculas"
print(s_texto2.capitalize())


#   count(): Cuenta cuantas veces aparece una letra o una cadena de caracteres.
s_texto3 = "Vamos a ver cuántas veces aparece la letra c"
print(s_texto3.count('c'))

#   find(): Representa el índice o la posición en el cual aparece un carácter o un grupo de caracteres. Si aparece varias veces me dice sólo el primero.
s_texto4 = "Vamos a ver en qué posición aparece primero la letra e"
print(s_texto4.find('e'))

#   rfind(): Igual que find() pero contando desde atrás.
s_texto5 = "Vamos a ver en qué posición aparece la palabra desde, contando desde atrás"
print(s_texto5.rfind('desde'))

#   isdigit(): Devuelve un boolean, nos dice si el valor introducido es un string. Tiene que ser un valor introducido entre comillas o dará error.
s_texto6 = "6"
print(s_texto6.isdigit())

#   isalum(): Devuelve un boolean, Devuelve verdadero si todos los caracteres de la cadena son numéricos y hay al menos un carácter. En caso contrario, devuelve falso.
s_texto7 = "9857654gf7"
print(s_texto7.isalnum())

#   isalpha(): Devuelve un boolean, comprueba si hay sólo letras. Los espacios no cuentan.
s_texto8 = "Holamundo"
print(s_texto8.isalpha())

#   split(): Separa por palabras utilizando espacios. Crea una lista.
s_texto9 = "Vamos a separar esta frase por los espacios"
print(s_texto9.split())

#   Podemos usar otro carácter como separador, por ejemplo una coma:
s_texto10 = "Esta sería la primera parte,y esta la segunda"
print(s_texto10.split(","))
 
#   strip(): Borra los espacios sobrantes al principio y al final.
s_texto11 = "   En este texto había espacios al principio y al final    "
print(s_texto11.strip())

#   replace(): Cambia una palabra o una letra por otra.
s_texto12 = "Vamos reemplazar la palabra casa"
print(s_texto12.replace("casa", "hogar"))

#   Te invito a que inspecciones el resto de funciones predefinidas para los strings en:
#   https://www.freecodecamp.org/espanol/news/metodos-de-string-de-python-explicados-con-ejemplo/






