



class Persona():
    def __init__(self, nombre, edad, lugar):
        self.nombre=nombre
        self.edad=edad
        self.lugar=lugar
    

    def descripcion(self):
        print("El nombre es ", self.nombre, ", tiene ", self.edad, " anyos", " y es de ", self.lugar)
    

    # Para personalizar el constructor del padre de acuerdo a las necesidades del hijo se usa super():
    
class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_emp, edad_emp, lugar_epm):
        super().__init__(nombre_emp, edad_emp, lugar_epm)
        self.salario=salario
        self.antiguedad=antiguedad
        
    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.salario, ", antiguedad: ", self.antiguedad)
        
Angel=Persona("Angel", 43, "Malaga")
Angel.descripcion()

Empleado1=Empleado(2000, 2017, "Manolo", 33, "Madrid")
Empleado1.descripcion()

