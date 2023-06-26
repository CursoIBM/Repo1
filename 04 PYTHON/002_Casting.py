
# Forzado de tipo Enteros:
x = int(1)  	 # x Valdrá 1
y = int(2.8) 	 # y Valdrá 2
z = int("3") 	 # z Valdrá 3

# Forzado de tipo Float:
x = float(1)     # x Valdrá 1.0
y = float(2.8)   # y Valdrá 2.8
z = float("3")   # z Valdrá 3.0
w = float("4.2") # w Valdrá 4.2

# Forzado de tipo string:
x = str("s1")    # x Valdrá 's1'
y = str(2)       # y Valdrá '2'
z = str(3.0)     # z Valdrá '3.0'

# CASTING. Reconversión de tipos:
# Casting de int a float:
n_numero = 13  
n_numero_2 = float(n_numero)

# Casting de float a int:
n_numero_3 = 24.876
n_numero_4 = int(n_numero_3)

# Casting de string a int
s_texto = "13"
n_numero_5 = int(s_texto)

# Casting de int a string
n_numero_6 = 27
s_texto_2 = str(n_numero_6)


print(n_numero_2)
print(type(n_numero_2))
print(n_numero_4)
print(type(n_numero_4))
print(n_numero_5)
print(type(n_numero_5))
print(s_texto_2)
print(type(s_texto_2))
