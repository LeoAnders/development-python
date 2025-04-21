from math import pi

# Classe base
class FormaGeometrica:
    def calcular_area(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

# Classe derivada: Círculo
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return pi * (self.raio ** 2)

# Classe derivada: Retângulo
class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

# Classe derivada: Triângulo
class Triangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

# Usando polimorfismo
formas = [
    Circulo(5),
    Retangulo(4, 6),
    Triangulo(3, 7)
]

# O método calcular_area será chamado para cada forma, mas o comportamento varia
for forma in formas:
    print(f'Área: {forma.calcular_area():.2f}')
