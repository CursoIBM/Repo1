


# POO

# CREACIÓN DE UNA CLASE PADRE
# Todas las clases heredan de la superclase OBJECT
# Es como si pusiésemos: class Empleado(object):

class Empleado():
# Método constructor
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
        self.sueldo = 0

    def modificaSueldo(self, sueldo):
        self.sueldo = sueldo

    def muestraSueldo(self):
        print("El sueldo del", self.cargo, "es de", self.sueldo)


conserje = Empleado("Manolo", "conserje")

conserje.modificaSueldo(15000)

conserje.muestraSueldo()

class Jefe(Empleado):
    
    def plusSueldo(self, plus):
        self.sueldo = self.sueldo + plus

    def muestraSueldo(self):
        print("El sueldo del", self.cargo, "es de", self.sueldo), 

D_Andres = Jefe("D. Andrés", "jefe de ventas")


D_Andres.modificaSueldo(25000)
D_Andres.plusSueldo(5000)

D_Andres.muestraSueldo()

print(D_Andres.nombre)