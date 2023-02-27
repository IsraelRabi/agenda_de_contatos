from .Contato import Contato

class Agenda:
    def __init__(self):
        self.contatos = []

    def contato_existe(self, telefone='', nome=''):
        if telefone != '':
            for contato in self.contatos:
                if contato.telefone == telefone:
                    return True
        elif nome != '':
             for contato in self.contatos:
                if contato.nome == nome:
                    return True
        return False

    def cadastrar_contato(self, nome, sobrenome, telefone):
        if not self.contato_existe(telefone=telefone):
            contato = Contato(nome, sobrenome, telefone)
            self.contatos.append(contato)
            return 'Cadastrado com sucesso.'
        return 'Contato já existente.'

    def listar_contatos(self):
        for contato in self.contatos:
            print(contato)

    def exibir_contato(self, nome):
        if self.contato_existe(nome=nome):
            for contato in self.contatos:
                if contato.nome == nome:
                    return contato
        return 'Contato não existente.'

