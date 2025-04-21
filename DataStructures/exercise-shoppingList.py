# Imagine uma situação na qual você deve realizar o cadastro
# de uma lista de compra em um sistema. Cada produto comprado
# deverá ser registrado com seu nome, quantidade e valor unitário

mercado = []

for i in range(3):
   nome = input('Digite o nome do item:')
   qtd = int(input('Digite a quantidade:'))
   valor = float (input('Digite o valor:'))
   mercado.append([nome, qtd, valor])
   
print (mercado)

