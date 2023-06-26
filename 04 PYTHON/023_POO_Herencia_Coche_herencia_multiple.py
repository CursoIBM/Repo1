
# SOBREESCRITURA DE MÉTODOS

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
        print("El modelo es un coche", "\n",
            "Marca:", self.marca, "\n",
              "Modelo:", self.modelo, "\n",
              "Color:", self.color, "\n",
              "Está arrancado:", self.arrancado,"\n",
              "Está parado:", self.parado
              )

        
miCoche = Vehiculo("Renault", "Megane")

miCoche.arrancar()

miCoche.resumen()

class Moto(Vehiculo):
    is_carenado = False
    
    def poner_carenado(self):
        self.is_carenado = True

    def resumen(self):
        print("El modelo es una moto", "\n",
            "Marca:", self.marca, "\n",
            "Modelo:", self.modelo, "\n",
            "Color:", self.color, "\n",
            "Está arrancado:", self.arrancado,"\n",
            "Está parado:", self.parado, "\n",
            "Tiene carenado:", self.is_carenado
            )
        
miMoto = Moto("Kawasaki", "Ninja")

miMoto.resumen()

class kwad(Moto):
    pass

miKwad = kwad("Kawasaki", "Stream casper")

miKwad.resumen()

class Vehiculo_electrico():
    voltaje = 78
    carga_rapida = True
    
    def muestra_Voltaje(self):
        print("El voltaje del vehículo es de:", self.voltaje, "Kws")
        
class Coche_electrico(Vehiculo, Vehiculo_electrico):
    pass

miCocheElectrico = Coche_electrico("Hyunday", "Ionic")

miCocheElectrico.resumen()
miCocheElectrico.muestra_Voltaje()
    