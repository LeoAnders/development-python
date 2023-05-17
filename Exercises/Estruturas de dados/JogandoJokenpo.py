# Crie um jogo de pedra, papel ou tesoura (Jokenpo). Você deverá jogar contra o computador.
# Você irá sempre escolher uma das opções: 1- pedra, 2- papel, 3- tesoura
# - O computador irá sempre sortear um número de 1 até 3 para jogar
# - Armazene todos os resultados em uma lista e no final apresente o vencedor
# - Encerre o programa ao digitar zero

import random

def validateInt(question, min, max):
   x = int(input(question))
   while ((x < min) or (x > max)):
        x = int(input(question))
   return x


def vencedor(jogador1, jogador2):
   global v1, v2, empate
   if jogador1 == 1:  # Pedra
      if jogador2 == 1:  # Pedra
         empate += 1
      elif jogador2 == 2:  # Papel
         v1 += 1
      elif jogador2 == 3:  # Tesoura
         v2 += 2
   elif jogador1 == 2:  # Papel

      if jogador2 == 1:  # Pedra
         v1 +=1 
      elif jogador2 == 2: # Papel
         empate += 1
      elif jogador2 == 3: # Tesoura
         v2 += 1
   elif jogador1 == 3: # Tesoura
      if jogador2 == 1: # Pedra
         v2 += 1
      elif jogador2 == 2: # Papel
         v1 += 1
      elif jogador2 == 3: # Tesoura
         empate += 1
   resultados = [v1, v2, empate]
   return resultados          


print("JOKENPO")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

resultados = []
jogadas = []
v1 = 0
v2 = 0
empate = 0

while True:
    j1 = validateInt("Escolha sua jogada: ", 0, 3)
    if j1 == 0:
        print("Encerrando programa...\n")
        break
    j2 = random.randint(1,3)
    jogadas.append([j1,j2])
    resultados = vencedor(j1,j2)
   
    for jogada in jogadas:
         for dado in jogada:
            print(dado, end=" ")
         print()

print("-"*40)
print("Numero de vitorias do jogador 1: {}".format(resultados[0]))
print("Numero de vitorias do jogador 2: {}".format(resultados[1])) 
print("Numero de empates: {}".format(resultados[2]))
print("_"*40)             
   

    