# POO

# CREACIÓN DE UNA CLASE
class Usuario():
    # Declaración de atributos
    nombre = "Angel"
    __edad = 47
    login = "admin"
    password = "1234"
    email = "angel@loquesea.com"
    telefono = 666666666

    # Declaración de métodos
    def resumen(self):  # self hace referencia a la instancia de clase.
        print(f'Los datos del usuario son:\n'
              f'Nombre: {self.nombre}\n'
              f'Edad: {self.__edad}\n'
              f'Login: {self.login}\n'
              f'Password: {self.password}\n'
              f'Email: {self.email}\n'
              f'Teléfono: {self.telefono}')

    def cambiaEdad(self):
        edadIntroducida = int(input("Introduce edad entre 18-100:"))

        if 18 < edadIntroducida < 100:
            self.__edad = edadIntroducida
            print("Edad introducida correcta")
            return ""
        else:
            print("La edad introducida no es correcta.")
            self.cambiaEdad()
            return ""


    def muestraEdad(self):
        print('La edad del usuario es:', self.__edad, 'años.')
        return ""



administrador = Usuario()
administrador.resumen()

print(administrador.cambiaEdad())
print(administrador.muestraEdad())
