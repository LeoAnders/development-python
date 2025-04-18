# Escreva um algoritmo que leia dois valores numéricos e que
# pergunte ao usuário qual operação ele deseja realizar:
# adição (+), subtração (-), multiplicação (*), divisão (/)
# e sair. Exiba na tela o resultado da operação desejada
# Repita até que a opção saída seja escolhida - 
# (Exercício construído na aula prática 3)


print("Selecione sua operação para soma dos valores")
print(" + Adição")
print(" - subtração")
print(" * multiplicação")
print(" / divisão")
print("Escreva exit para finalizar o programa apos seleção do operador") 


while True:

   operation = (input("Selecione sua operação"))
   if (operation == "+" or operation == "-" or operation == "*" or operation == "/"):
      x = float(input("Digite o primeiro valor: "))
      y = float(input("Digite o segundo valor: "))

      
   if (operation == "+"):
    result = x + y
    print(f"{x} + {y} = {result}")
    continue
    
   elif (operation == "-"):
    result = x - y
    print(f"{x} - {y} = {result}")
    continue

   elif (operation == "*"):
    result = x * y
    print(f"{x} * {y} = {result}")
    continue

   elif (operation == "/"):
    result = x / y
    print(f"{x} / {y} = {result}")
    continue

   elif (operation == "exit"):
      break

   else:
         print("operação invalida")

print("Encerrando o programa...")
