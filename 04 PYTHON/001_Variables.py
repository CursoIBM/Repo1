# VARIABLES

# Lo ideal es declara e inicializar siempre las variables.
# -----------------------------------------------------------

# Declaración de variable numérica entera:
n_edad = 47

# Declaración de variable numérica de coma flotante:
n_numero = -23.5245

# Declaración de variable de tipo string:
s_nombre = 'Manolo es "amigo" mío'

# Declaración de variable de tipo string en varias líneas:
s_textoLargo = """Esto es un mensaje
...con tres saltos
...de linea"""

# Sobreescribimos el valor de la variable s_edad y ahora la ponemos como string:
s_edad = "47"

# Declaración de constante:
NUMEROPI = 3.14159

# Declaración de un boolean
is_verdadero = True
is_casado = False

# True = 1 y False = 0
True == 1
False == 0

print(True + 2)

# Cuando se valida una condición , Python devuelve True o False:
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Declaración múltiple
# En una sola instrucción, estamos declarando tres variables: a, b y c, y asignándoles un valor concreto a cada una.

a, b, c = 'string', 15, True

# Sería como poner:
a = 'string'
b = 15
c = True

# Para verificar el tipo de cualquier objeto en Python, usamos la función type() :

print(type(n_edad))
print(type(n_numero))
print(type(s_nombre))
print(type(NUMEROPI))
print(type(is_verdadero))
print(type(is_casado))
