


class Persona():
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
    
    def resumen(self):
        print("Nombre:", self.nombre, "\nEdad:", self.edad,"\nCiudad:",self.ciudad, "\n")
        
persona1 = Persona("Manolo", 45, "Madrid")

persona1.resumen()

'''class Empleado(Persona):
    def __init__(self, salario, antiguedad):
        super().__init__("Andrés", 32, "Barcelona")
        self.salario = salario
        self.antiguedad = antiguedad


operario01 = Empleado(23000, 2)

operario01.resumen()
'''

#El problema es que todos los empleados se llamarían igual 
# y que no nos saca salario y antiguedad

class Empleado(Persona):
    def __init__(self, nombre_empleado, edad_empleado, ciudad_empleado, salario, antiguedad):
        super().__init__(nombre_empleado, edad_empleado, ciudad_empleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def resumen(self):
        print("Nombre:", self.nombre, "\nEdad:", self.edad,"\nCiudad:",self.ciudad,
              "\nSalario", self.salario, "\nAntiguedad:", self.antiguedad, "años.")

operario01 = Empleado("Andrés", 34, "Barcelona", 23000, 2)

operario01.resumen()

#Principio de sustitución
isinstance(operario01, Empleado)
isinstance(operario01, Persona)