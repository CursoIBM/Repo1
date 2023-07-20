
class Moto():
    def ruedas(self):
        print("Moto. Vehículo con dos ruedas")
        
class Coche():
    def ruedas(self):
        print("Coche. Vehículo con cuatro ruedas")
        
class Camion():
    def ruedas(self):
        print("Camión. Vehículo con 8 ruedas")
        
moto01 = Moto()
moto01.ruedas()

coche01 = Coche()
coche01.ruedas()

camion01 = Camion()
camion01.ruedas()

#Polimorfismo

class Moto():
    def ruedas(self):
        print("Moto. Vehículo con dos ruedas")
        
class Coche():
    def ruedas(self):
        print("Coche. Vehículo con cuatro ruedas")
        
class Camion():
    def ruedas(self):
        print("Camión. Vehículo con 8 ruedas")
        
def ruedas_vehiculos(vehiculo):
    vehiculo.ruedas()
    
vehiculo01 = Camion()
ruedas_vehiculos(vehiculo01)

vehiculo02 = Coche()
ruedas_vehiculos(vehiculo02)

vehiculo03 = Moto()
ruedas_vehiculos(vehiculo03)