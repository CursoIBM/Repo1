class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')

if __name__ == '__main__':
    persona1 = Persona('Juan', 'Perez', 28)
    persona1.nombre = 'Juan Carlos'
    persona1.apellido = 'Lara'
    persona1.edad = 30
    persona1.mostrar_detalle()

    print(__name__)
