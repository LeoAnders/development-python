

def objectsDimensions():
  # Função para obter as dimensões do objeto e calcular o preço com base no volume 
   while True:
      try:
         height = float(input("Digite a altura do objeto (em cm): "))
         length = float(input("Digite o comprimento do objeto (em cm): "))
         width = float(input("Digite a largura do objeto (em cm): "))
         volume = height * length * width

         if volume < 1000:
            return 10 
         elif volume < 10000:
            return 20 
         elif volume < 30000:
            return 30 
         elif volume < 100000:
            return 50 
         elif volume >= 100000:
            print(f"O volume do objeto em cm: {volume} ")
            print("Nao aceitamos objetos com dimensões tao grandes.")
            continue
               
         print(f"O volume do objeto em cm: {volume} ")

         return None   
      
      except ValueError:
         print("Voce digitou alguma dimensão do objeto com valor nao numérico.")



def objectWeight():
   # Função para obter o peso do objeto e calcular o preço com base no peso
   while True:
      try:
         weight = float(input("Digite o peso do objeto (em kg): "))
      
         if weight < 0.1:
            return 1
         elif weight < 1:
            return 1.5
         elif weight <10:
            return 2
         elif weight <= 30:
            return 3
         elif weight > 30:
            print(f"O peso do objeto em kg: {weight} ")
            print("Nao aceitamos objetos tao pesados.")
            continue

         return None
      
      except ValueError:
         print("Voce digitou o peso do objeto com valor nao numérico.")


def objectRoute():
   # Função para obter a rota desejada e calcular o preço com base na rota
   while True:
         print("----------Rotas disponíveis----------")
         print("FB - De Florianópolis até Balneário Camboriú")
         print("BF - De Balneário Camboriú até Florianópolis")
         print("JB - De Joinville até Balneário Camboriú")
         print("BJ - De Balneário Camboriú até Joinville ")
         print("JF - De Joinville até Florianópolis")
         print("FJ - De Florianópolis até Joinville \n")
         
         route = input("Digite a rota desejada(utilize as siglas): ") 
         route = route.upper()

         if route == "FB" or route == "BF":
            return 1.0
            
         elif route == "JB" or route == "BJ":
            return 1.2
         
         elif route == "JF" or route == "FJ":
            return 1.5 
         else:
            print("Rota nao encontrada.")
            print("Entre com a rota desejada novamente.\n") 
            continue     
     

dimensions = objectsDimensions()
weight = objectWeight()
route = objectRoute()

# Calcula o preço total
total = dimensions * weight * route

# Exibe o resultado final
print(f"Preço total a pagar: R${total}")
print(f"Dimensões: {dimensions} * Peso: {weight} * Rota: {route}.")
