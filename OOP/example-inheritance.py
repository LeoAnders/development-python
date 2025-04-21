# https://docs.python.org/pt-br/3.13/tutorial/classes.html#inheritance

# Classe base: Conta bancária genérica
class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    def exibir_saldo(self):
        print(f"{self.titular} tem R${self.saldo:.2f} na conta.")


# Subclasse: Conta Corrente
class ContaCorrente(Conta):
    def __init__(self, titular, saldo=0, limite=500):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor > (self.saldo + self.limite):
            print("Limite excedido.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com limite. Novo saldo: R${self.saldo:.2f}")


# Subclasse: Conta Poupança
class ContaPoupanca(Conta):
    def render_juros(self, taxa):
        juros = self.saldo * taxa
        self.saldo += juros
        print(f"Juros de R${juros:.2f} aplicados. Novo saldo: R${self.saldo:.2f}")


# Usando as classes
print("==== Conta Corrente ====")
cc = ContaCorrente("João", saldo=100)
cc.exibir_saldo()
cc.sacar(550)
cc.depositar(200)

print("\n==== Conta Poupança ====")
cp = ContaPoupanca("Maria", saldo=1000)
cp.exibir_saldo()
cp.render_juros(0.05)  # 5% de juros
