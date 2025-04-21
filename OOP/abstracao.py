from abc import ABC, abstractmethod

# Classe abstrata
class Veiculo(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def parar(self):
        pass

# Subclasse concreta
class Carro(Veiculo):
    def mover(self):
        print("O carro está se movendo")

    def parar(self):
        print("O carro parou")

# Outra subclasse concreta
class Moto(Veiculo):
    def mover(self):
        print("A moto está se movendo")

    def parar(self):
        print("A moto parou")

# Usando as classes concretas
veiculo1 = Carro()
veiculo2 = Moto()

veiculo1.mover()  # O carro está se movendo
veiculo1.parar()  # O carro parou

veiculo2.mover()  # A moto está se movendo
veiculo2.parar()  # A moto parou
