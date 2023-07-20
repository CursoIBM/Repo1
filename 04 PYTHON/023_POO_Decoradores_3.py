
#Función decoradora con parámetros variables

def funcion_decoradora(funcion_a_decorar):
    
    def funcion_interior(*args):
        print("El resultado es ")
        
        funcion_a_decorar(*args)
        
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
    
suma(3,5)
resta(10,5)
multiplica(2, 3, 4)




