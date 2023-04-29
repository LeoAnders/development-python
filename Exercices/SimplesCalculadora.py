
print("Selecione sua operação para soma dos valores")
print(" + Adição")
print(" - subtração")
print(" * multiplicação")
print(" / divisão")

operation = (input("Selecione sua operação"))

if (operation == "+" or operation == "-" or operation == "*" or operation == "/"):
    x = float(input("Digite o primeiro valor: "))
    y = float(input("Digite o segundo valor: "))

if (operation == "+"):
    result = x + y
    print(result)

elif (operation == "-"):
    result = x - y
    print(result)

elif (operation == "*"):
    result = x * y
    print(result)

elif (operation == "/"):
    result = x / y
    print(result)

else:
   print("operação invalida")

print("Encerrando o programa...")