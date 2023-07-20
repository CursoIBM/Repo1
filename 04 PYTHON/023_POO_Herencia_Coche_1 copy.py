

class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.color = "Rojo"
        self.arrancado = False
        self.parado = True
        
    def arrancar(self):
        self.arrancado = True
        self.parado = False

    def parar(self):
        self.parado = True
        self.arrancado = False
        
    def resumen(self):
        print("Marca:", self.marca, "\n",
              "Modelo:", self.modelo, "\n",
              "Color:", self.color, "\n",
              "Está arrancado:", self.arrancado,"\n",
              "Está parado:", self.parado
              )

        
miCoche = Vehiculo("Renault", "Megane")

miCoche.arrancar()

miCoche.resumen()

class Moto(Vehiculo):
    pass

miMoto = Moto("Kawasaki", "Ninja")

miMoto.resumen()