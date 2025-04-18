# Escreva um algoritmo que crie uma tupla com 10 palavras.
# Encontre dentro dessa tupla as vogais de cada palavra. Faça 
# um print na tela com o nome da palavra e suas respectivas vogais


def encontrarVogais(palavra):
   vogais = []
   for letra in palavra:
        if letra.lower() in ('a', 'e', 'i', 'o', 'u'):
            vogais.append(letra)
   return vogais


fabricantesCarros = ("Ferrari", "Volkswagen", "GM", "Ford", "Honda", "BMW", "Mercedes-Benz", "Fiat", "Hyundai", "Nissan")

for fabricantesCarros in fabricantesCarros:
    vogais = encontrarVogais(fabricantesCarros)
    print(f"Fabricante: {fabricantesCarros}. Vogais: {vogais}.")