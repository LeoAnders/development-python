#Variável global para armazenar as peças cadastradas
registeredPieces = []

#Registrando peça.
def registerPiece(code):
   piece = {}
   piece["code"] = code
   piece["name"] = input("Digite o nome da peça: ")
   piece["manufacturer"] = input("Digite o fabricante da peça: ")
   piece["value"] = float(input("Digite o valor da peça: "))

   registeredPieces.append(piece)
   print("Peça cadastrada com sucesso!\n")

#Consultar pecas
def consultPiece():
   while True:
      print("1 - Consultar peças")
      print("2 - Consultar peças por código")
      print("3 - Consultar peças por fabricante")
      print("4 - Retornar\n")
      option = input("Selecione a opção: ")

      if option == "1":
         print("---- Todas as Peças ----")
         for piece in registeredPieces:
            print("Código:", piece["code"])
            print("Nome:", piece["name"])
            print("Fabricante:", piece["manufacturer"])
            print("Valor: R$",piece["value"])
            print("_"*30 )

      elif option == "2":
         code = int(input("\nDigite o código da peça: "))
         print("---- Peça por Código ----")
         for piece in registeredPieces:
            if piece["code"] == code:
                    print("Código:", piece["code"])
                    print("Nome:", piece["name"])
                    print("Fabricante:", piece["manufacturer"])
                    print("Valor: R$",piece["value"])
                    break
            else:
                print("Nenhuma peça encontrada com o código informado.")

      elif option == "3":
         manufacturer = input("\nDigite o fabricante da peça: ")
         print("---- Peça por Fabricante ----")
         foundPieces = False
         for piece in registeredPieces:
            if piece["manufacturer"] == manufacturer:
               print("Código:", piece["code"])
               print("Nome:", piece["name"])
               print("Fabricante:", piece["manufacturer"])
               print("Valor: R$",piece["value"])
               foundPieces = True
            if not foundPieces:
               print("Nenhuma peça encontrada com o fabricante informado.")

      elif option == "4":
            break

      else:
         print("Opção inválida. Por favor, selecione uma opção válida.")


#Remover peça cadastrada
def removePiece():
    code = int(input("\nDigite o código da peça que deseja remover: "))
    for piece in registeredPieces:
         if piece["code"] == code:
            registeredPieces.remove(piece)
            print("Peça removida com sucesso!")
            break
         else:
            print("Nenhuma peça encontrada com o código informado.")
        
#Loop inicial
code = 1
while True:
   print("--------Opções-------")
   print("1 - Cadastrar peças")
   print("2 - Consultar peças")
   print("3 - Remover peças")
   print("4 - Sair\n")

   option = input("Selecione sua opção: ")

   if option == "1":
      print("Voce selecionou a opção de cadastrar peça.")
      print(f"Código da peça {code}")
      piece = registerPiece(code)
      code += 1

      
   elif option == "2":
      print("Voce selecionou a opção consultar peças.")
      consultPiece()
      
   elif option == "3":
      print("Voce selecionou a opção remover peça.")
      removePiece()
      
   elif option == "4":
      print("Encerrando programa...")
      break
      
   else:
      print("Opção inválida. Por favor, selecione uma opção válida.")

   
