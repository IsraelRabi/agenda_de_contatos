class Contato:
    def __init__(self, nome, sobrenome, telefone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone

    def __repr__(self):
        return f'Nome: {self.nome} {self.sobrenome}\nTelefone: {self.telefone}'
