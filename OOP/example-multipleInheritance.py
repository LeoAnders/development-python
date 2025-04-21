class Autenticavel:
    def __init__(self, username, senha):
        self.username = username
        self._senha = senha
    
    def autenticar(self, senha_digitada):
        return self._senha == senha_digitada


class Autorizavel:
    def __init__(self, permissoes):
        self.permissoes = permissoes

    def tem_permissao(self, permissao):
        return permissao in self.permissoes


class UsuarioAdmin(Autenticavel, Autorizavel):
    def __init__(self, username, senha, permissoes):
        Autenticavel.__init__(self, username, senha)
        Autorizavel.__init__(self, permissoes)
    
    def __str__(self):
        return f"Administrador: {self.username}"
