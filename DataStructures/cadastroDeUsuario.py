# Crie um programa para ler o nome, ano de nascimento e sexo de diferentes pessoas
# Armazene os dados em um dicionário com listas
# Ao encerrar o cadastro, apresente:
# - O total de cadastros efetuados
# - A média das idades das pessoas
# - Uma lista de mulheres com menos de 30 anos 
# - Uma lista de homens com idade acima da média

register = {"name":[], "year":[], "gender":[]}

totalRegistrations = 0
totalAge = 0
womenUnder30 = []
aboveAverageMen = []

while True:
   negacao = input("você gostaria de realizar o cadastro? [S/N]")
   if negacao.upper() == "N":
        print("Encerando programa...")
        break
   if negacao.upper() not in "S":
       print('Digite [S] para sim e [N] para nao')
   else:
       #total de registros
       totalRegistrations += 1

   name = input("Escreva seu nome: ")
   year = int(input("Escreva seu ano de nascimento: "))
   gender = input("Escreva seu sexo [F/M]")
   register["name"].append(name)
   register["year"].append(year)
   register["gender"].append(gender.upper())

#calculando Media de idades
for year in register["year"]:
    age = 2023 -year 
    totalAge += age

averageAge = totalAge / totalRegistrations    


#mulheres com menos de 30 anos 
for i in range(len(register["name"])):
    if register["gender"][i] == "F" and (2023 - register["year"][i]) < 30:
        womenUnder30.append(register["name"][i])
    

#Homens com idades acima da media
for i in range(len(register["name"])):
    if register["gender"][i] == "M" and (2023 - register["year"][i]) > averageAge:
        aboveAverageMen.append(register["name"][i])
    
   
print("Total de cadastros: ",totalRegistrations)
print("Media das idades do cadastro: ", {round(averageAge,2)})
print("Mulheres com menos de 30 anos: ", womenUnder30)
print("Homens com idade acima da media: ",aboveAverageMen)
   
       




