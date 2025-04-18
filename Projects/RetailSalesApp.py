
price = float(input("Digite o valor do produto em R$: "))
amount = int(input("Digite a quantidade do produto: "))


if amount <= 9:
   #Sem desconto
   discount = 0
elif amount >= 10 and amount <= 99:
   #Desconto de 5% na unidade
   discount = 0.05
elif amount >= 100 and amount <= 999:  
   #Desconto de 10% na unidade
   discount = 0.1
else:
     #Desconto de 15% na unidade
    discount = 0.15

withoutDiscount = amount * price
withDiscount = amount * price * (1 - discount)

#Resultado final

print(f"Valor sem acréscimo de desconto fica em R${withoutDiscount:.2f}.")
if amount <=9:
   print("Em compras abaixo de 9 itens nao disponibilizamos descontos.")

if amount >=10:
   print(f"Com desconto de {discount}% em sua compra, o valor total fica em: R${withDiscount:.2f}.")  