from .Contato import Contato

class Agenda:
    def __init__(self):
        self.contatos = []

    def cadastrar_contato(self, nome, sobrenome, telefone):
        contato = Contato(nome, sobrenome, telefone)
        self.contatos.append(contato)

    def listar_contatos(self):
        for contato in self.contatos:
            print(contato)

    def exibir_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                print(contato)
                break

