# Lista para armazenar os contatos
contatos = []

# Função para adicionar um contato
def adicionar_contato(nome, telefone):
    contato = {'nome': nome, 'telefone': telefone}
    contatos.append(contato)
    print(f"Contato {nome} adicionado com sucesso.")

# Função para remover um contato
def remover_contato(nome):
    for contato in contatos:
        if contato['nome'] == nome:
            contatos.remove(contato)
            print(f"Contato {nome} removido com sucesso.")
            return
    print(f"Contato {nome} não encontrado.")

# Função para listar os contatos
def listar_contatos():
    if not contatos:
        print("Nenhum contato na lista.")
    else:
        print("Lista de contatos:")
        for contato in contatos:
            print(f"Nome: {contato['nome']} - Telefone: {contato['telefone']}")

# Função principal com menu interativo
def menu():
    while True:
        print("\n--- Menu de Contatos ---")
        print("1. Adicionar contato")
        print("2. Remover contato")
        print("3. Listar contatos")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            adicionar_contato(nome, telefone)
        elif opcao == '2':
            nome = input("Digite o nome do contato a remover: ")
            remover_contato(nome)
        elif opcao == '3':
            listar_contatos()
        elif opcao == '4':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()