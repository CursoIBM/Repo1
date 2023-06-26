class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def cacular_area(self):
        return self.base * self.altura


base = int(input('Proporciona la base: '))
altura = int(input('Proporciona la altura: '))

rectangulo1 = Rectangulo(base, altura)
print(f'Área rectángulo: {rectangulo1.cacular_area()}')

base = int(input('Proporciona la base: '))
altura = int(input('Proporciona la altura: '))

rectangulo2 = Rectangulo(base, altura)
print(f'Área rectángulo: {rectangulo2.cacular_area()}')
