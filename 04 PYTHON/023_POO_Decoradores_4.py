
#Función decoradora con parámetros variables y/o de tipo diccionario

def funcion_decoradora(funcion_a_decorar):
    
    def funcion_interior(*args, **kwargs):
        print("El resultado es ")
        
        funcion_a_decorar(*args, **kwargs)
        
        print(". Calculo terminado.")
        
    return funcion_interior


@funcion_decoradora
def suma(num1, num2):
    print(num1+num2)
 
#  @funcion_decoradora    
def resta(num1, num2):
    print(num1-num2)
    
@funcion_decoradora
def multiplica(num1, num2, num3):
    print(num1*num2*num3)    
    
@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))  
    
suma(3,5)
resta(10,5)
multiplica(2, 3, 4)
potencia(base=3, exponente=4)




