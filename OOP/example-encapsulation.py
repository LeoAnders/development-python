class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial  # atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('Valor de depósito inválido.')

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso.')
        else:
            print('Saldo insuficiente ou valor inválido.')

    def consultar_saldo(self):
        return f'Saldo atual: R${self.__saldo:.2f}'

# Uso da classe
conta = ContaBancaria("João", 1000)

print(conta.consultar_saldo())  # Saldo atual: R$1000.00
conta.depositar(500)
print(conta.consultar_saldo())  # Saldo atual: R$1500.00
conta.sacar(200)
print(conta.consultar_saldo())  # Saldo atual: R$1300.00

# Tentativa de acessar saldo diretamente (vai falhar)
print(conta.__saldo)  # AttributeError
