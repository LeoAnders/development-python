
# Escreva um programa que calcule o preço a pagar pelo fornecimento
# de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo
# de instalação: R para residências, I para indústrias e C para comércios

print("Calculo de custo de kWh")
print("R- Residencia ")
print("I- Industria")
print("C- Comercio")

typeInstallation = input("Selecione o tipo de instalação")
kWhConsumption = float(input(f"Informe o consumo de kWh"))

if (typeInstallation == "R"):
    if (kWhConsumption <= 500):
        price = 0.4
    else:
        price = 0.65

elif (typeInstallation == "I"):
    if (kWhConsumption <= 100):
        price = 0.55
    else:
        price = 0.6
elif (typeInstallation == "C"):
    if (kWhConsumption <=5000):
        price = 0.55
    else:
        price = 0.6 

else:
   print("Instalação invalida")

sum = kWhConsumption * price

print(f"Valor total a pagar: R${sum}") 