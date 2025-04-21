
class MinhaClasse:
  valor = 10 # Atributo de classe
  
  def __init__(self, valor):
    self.valor = valor # Atributo de instância
    
  # requer uma instância para ser chamado
  def metodo_instancia(self):
    print("Método de instância")
    
  @classmethod
  def metodo_de_classe(cls):
    print("Método de classe")
    
  @staticmethod
  def metodo_estatico():
    print("Método estático")
    
obj = MinhaClasse(20)
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_de_classe())

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    @classmethod
    def criar_carro(cls, configuracao):
      marca, modelo, ano = configuracao.split(',')
      return cls(marca, modelo, int(ano))

configuracao1 = "Ford,Mustang,2022"
carro = Carro.criar_carro(configuracao1)

class Matematica:
  
    @staticmethod
    def somar(a,b):
      return a + b
    
print(Matematica.somar(2,3))