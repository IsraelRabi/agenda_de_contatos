from agenda_de_contatos.Agenda import Agenda

agenda = Agenda()

while True:
    opcao = input('''\
(C)adastrar Contato
(L)istar Contatos
(E)xibir Contato
(S)air 
opcao -> ''').lower()
    if opcao ==  's':
        break
    elif opcao == 'c':
        nome = input('Nome: ')
        sobrenome = input('Sobrenome: ')
        telefone = input('Telefone: ')
        agenda.cadastrar_contato(nome, sobrenome, telefone)
        print()
    elif opcao == 'l':
        print()
        agenda.listar_contatos()
        print()
    elif opcao == 'e':
        nome = input('Digite o nome do contato: ')
        print()
        agenda.exibir_contato(nome)
        print()

