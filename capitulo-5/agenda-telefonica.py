# -*- coding: utf-8 -*-

def mostrar_menu():
    print()
    ops = ["Sair", "Adicionar contato", "Remover contato", "Procurar contato pelo nome", "Listar todos contatos"]
    for i, op in enumerate(ops):
        print(f"[{i}] - {op}")

def obter_op():
    while True:
        try:
            op = int(input("\nDigite a opção desejada: "))
            if op not in[0,1,2,3,4,] or op == "":
                raise ValueError("\nOpção inválida. Tente novamente\n")
            return op
        except ValueError as e:
            print(f"\nErro: {e}")

def adicionar_contato():
    while True:
        nome = input("\nDigite o nome do contato: ").strip()
        if nome == "":
            print("\nInput inválido. Tente novamente")
        else:
            break
    telefone = int(input("Digite o número: "))
    agenda[nome] = telefone

def remover_contato():
    nome = input("\nDigite o nome do contato: ")
    removido = agenda.pop(nome, None)
    if removido is not None:
        print(f"Contato {nome} removido com sucesso!")
    else:
        print(f"Contato {nome} não encontrado")

def procurar_pelo_nome():
    while True:
        nome = input("\nDigite o nome do contato: ").strip()
        if nome == "":
            print("\nInput inválido. Tente novamente")
        else:
            if agenda.get(nome):
                print(f"\nContato: {nome} - Telefone: {agenda.get(nome)}")
            else:
                print("\nContato inexistente. Tente novamente.")

def listar_todos_os_contatos():
    chaves = agenda.keys()
    if not chaves:
        print("\nAgenda vazia. Adicione algum contato.")
    else:
        print("\n")
        for chave in chaves:
            print(f"{chave} - {agenda.get(chave)}")

def executar_op(op):
    if op == 1:
        adicionar_contato()
    elif op == 2:
        remover_contato()
    elif op == 3:
        procurar_pelo_nome()
    elif op == 4:
        listar_todos_os_contatos()

op = -1
agenda = {}

while (op != 0):
    mostrar_menu()
    op = obter_op()
    executar_op(op)
print("\nPrograma encerrado. Volte sempre.")