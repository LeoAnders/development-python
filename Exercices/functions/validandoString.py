
def validadeString (question, min, max):
    name = input(question)
    tam = len(name)
    while((tam < min) or (tam > max)):
        name = input(question)
        tam = len(question)
    return name

x = validadeString("Escreva seu primeiro nome", 2, 15)
print ("Nome cadastrado com sucesso")
        