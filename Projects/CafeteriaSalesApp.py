print("Bem vindo a lanchonete FastBite do Leonardo M. Anders")
print("------------------Cardápio------------------")
print("| Código |        Descrição       |  Valor   |")
print("|  100   |  Cachorro-Quente       | R$ 9,00  |")
print("|  101   |  Cachorro-Quente Duplo | R$ 11,00 |")
print("|  102   |  X-Egg                 | R$ 12,00 |")
print("|  103   |  X-Salada              | R$ 13,00 |")
print("|  104   |  X-Bacon               | R$ 14,00 |")
print("|  105   |  X-Tudo                | R$ 17,00 |")
print("|  200   |  Refrigerante Lata     | R$ 5,00  |")
print("|  201   |  Chá Gelado            | R$ 4,00  |\n")

totalPrice = 0
# totalPrice armazena o valor total da compra.

while True:

   code = int(input("Digite o código desejado: "))
   #Solicita ao usuário que digite o código do item desejado.
   if code == 100:
      price = 9
      totalPrice += price
      #Adiciona o preço do Cachorro-Quente (R$ 9,00) ao valor total(totalPrice), equivalente a todos os produtos a baixo.
      print("Você pediu um cachorro-Quente no valor de R$ 9,00")
      question = input("Gostaria de mais alguma coisa?\n 1 - Sim \n 0 - Nao \n")
      #Pergunta ao usuário se deseja adicionar mais itens.
      if question == "1":
         continue
      elif question == "0":
         print(f"valor total a ser pago: R${totalPrice}")
         print("LeoAnders") 
         break
      else:
         print("Opção inválida. Por favor, digite '1' para 'Sim' ou '0' para 'Não'.")

   elif code == 101:
      price = 11
      totalPrice += price
      print("Você pediu um cachorro-Quente Duplo no valor de R$ 11,00")
      question = input("Gostaria de mais alguma coisa?\n 1 - Sim \n 0 - Nao \n")
      if question == "1":
         continue
      elif question == "0":
         print(f"valor total a ser pago: R${totalPrice}")
         print("LeoAnders")
         break
      else:
         print("Opção inválida. Por favor, digite '1' para 'Sim' ou '0' para 'Não'.")

   elif code == 102:
      price = 12
      totalPrice += price
      print("Você pediu um X-Egg no valor de R$ 12,00")
      question = input("Gostaria de mais alguma coisa?\n 1 - Sim \n 0 - Nao \n")
      if question == "1":
         continue
      elif question == "0": 
         print(f"valor total a ser pago: R${totalPrice}") 
         print("LeoAnders")
         break
      else:
         print("Opção inválida. Por favor, digite '1' para 'Sim' ou '0' para 'Não'.")

   elif code == 103:
      price = 13
      totalPrice += price
      print("Você pediu um X-Salada no valor de R$ 13,00")
      question = input("Gostaria de mais alguma coisa? \n 1 - Sim \n 0 - Nao \n")
      if question == "1":
         continue
      elif question == "0":
         print(f"valor total a ser pago: R${totalPrice}")
         print("LeoAnders")  
         break
      else:
         print("Opção inválida. Por favor, digite '1' para 'Sim' ou '0' para 'Não'.")

   elif code == 104:
      price = 14
      totalPrice += price
      print("Você pediu um X-Bacon no valor de R$ 14,00")
      question = input("Gostaria de mais alguma coisa? \n 1 - Sim \n 0 - Nao  \n")
      if question == "1":
         continue
      elif question == "0":
         print(f"valor total a ser pago: R${totalPrice}")  
         print("LeoAnders")
         break
      else:
         print("Opção inválida. Por favor, digite '1' para 'Sim' ou '0' para 'Não'.")

   elif code == 105:
      price = 17
      totalPrice += price
      print("Você pediu um X-Tudo no valor de R$ 17,00")
      question = input("Gostaria de mais alguma coisa? \n 1 - Sim \n 0 - Nao \n")
      if question == "1":
         continue
      elif question == "0": 
         print(f"Valor total a ser pago: R${totalPrice}") 
         print("LeoAnders")
         break
      else:
         print("Opção inválida. Por favor, digite '1' para 'Sim' ou '0' para 'Não'.")

   elif code == 200:
      price = 5
      totalPrice += price
      print("Você pediu um refrigerante Lata no valor de R$ 5,00 ")
      question = input("Gostaria de mais alguma coisa? \n 1 - Sim \n 0 - Nao  \n")
      if question == "1":
         continue
      elif question == "0":
         print(f"Valor total a ser pago: R${totalPrice}")
         print("LeoAnders")  
         break
      else:
         print("Opção inválida. Por favor, digite '1' para 'Sim' ou '0' para 'Não'.")

   elif code == 201:
      price = 4 
      totalPrice += price
      print("Você pediu um chá Gelado no valor de R$ 4,00 ")
      question = input("Gostaria de mais alguma coisa?  \n 1 - Sim \n 0 - Nao \n")
      if question == "1":
         continue
      elif question == "0":
         print(f"Valor total a ser pago: R${totalPrice}")
         print("LeoAnders")  
         break
      else:
         print("Opção inválida. Por favor, digite '1' para 'Sim' ou '0' para 'Não'.")

   else:
      print("Código invalido!")
      continue
    #Se o código digitado não corresponder a nenhum item do cardápio, exibe uma mensagem de código inválido e continua o loop.
            

