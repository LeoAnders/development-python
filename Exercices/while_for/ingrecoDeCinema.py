# Um cinema cobra preços diferentes para os ingressos de acordo com a idade
# de uma pessoa. Se a pessoa tiver menos de 3 anos de idade, o ingresso será
# gratuito, se tiver entre 3 e 12 anos, o ingresso custará R$ 15,
# se tiver mais de 12 anos, custará R$ 30
# - Escreva um laço em que você pergunte a idade aos usuários e, então,
# informe-lhes o preço do ingresso do cinema
# - Encerre o laço usando um break quando o usuário digitar sair
# - Após encerrar o laço, apresente na tela o total de pessoas que compraram
# ingressos, o total de dinheiro arrecadado e a média de idade das pessoas


total = 0
money = 0
#escrever um laco que pergunte a idade e que informe os preços
while True:
   age = input("Qual sua idade?")
#encerar o programa com "sair"
   if age == "sair":
      break
   age = int(age)
#calcular total de pessoas que compraram o ingresso    
   total += 1 
   if age < 3:
      ticket = 0
   elif(age > 12):
      ticket = 30
   else:
      ticket = 15
#calcular o total de dinheiro arrecadado      
   money += ticket

#Media de idade das pessoas
average = money / total

print(f"Total de pessoas: {total}")
print(f"Dinheiro arrecadado: {money}")
print(f"Media de idade das pessoas: {average}")
      
      
   

    






























# total = 0
# money = 0

# while True:
#    age = input("Qual sua idade? ")
#    if age == "sair":
#       break
#    age = int(age)
#    total += 1

#    if (age <3):
#       ticket = 0
#    else:
#       if (age > 12):
#           ticket = 30
#       else:
#           ticket = 15

#    money += ticket

# average  = money / total
# print(f"Total de pessoas: {total}")
# print(f"Dinheiro arrecado: R${money} {total}")
# print(f"Media de idade: {average}")

 