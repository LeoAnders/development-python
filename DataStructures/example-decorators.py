def meu_decorador(func):
    def wrapper():
        print("Antes de executar a função")
        func()
        print("Depois de executar a função")
    return wrapper

@meu_decorador
def diz_ola():
    print("Olá!")

diz_ola()