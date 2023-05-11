# Escreva um algoritmo que leia um valor e que imprima a quantidade 
# de cédulas necessárias para pagar esse mesmo valor Para simplificar,
# vamos trabalhar apenas com valores inteiros e com cédulas de R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 1

amount = int(input("Total do valor da compra em R$: "))

while True:
   print(f"Para pagar o valor de R${amount} Precisamos de notas de:")   

   if amount >=100:
      currency100 = amount // 100
      amount -= currency100 * 100
      print(f"Nota de R$100: {currency100}")       
#Caso o resultado seja zero if not amount break vai parar o programa e o restante do código nao ira ser executado       
      if not amount:
         break

   if amount >=50:
      currency50 = amount // 50
      amount -= currency50 * 50
      print(f"Nota de R$50: {currency50}") 
      if not amount:
         break
    
   if amount >=20:
      currency20 = amount // 20
      amount -= currency20 * 20
      print(f"Nota de R$20: {currency20}")
      if not amount:
         break 

   if amount >=10:
      currency10 = amount // 10
      amount -= currency10 * 10
      print(f"Nota de R$10: {currency10}") 
      if not amount:
         break

   if amount >=5:
      currency5 = amount // 5
      amount -= currency5 * 5
      print(f"Nota de R$5: {currency5}") 
      if not amount:
         break

   if amount: 
      currency1 = amount
      print(f"Nota de R$1: {currency1}")
      break


