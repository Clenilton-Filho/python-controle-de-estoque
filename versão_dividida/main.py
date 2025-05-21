from dados import carregar_dados, salvar_dados
from estoque import cadastrar_produto, listar_produtos, buscar_produto, alterar_produto, excluir_produto

estoque = carregar_dados()

while True:
    print("\n===== MENU =====")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Buscar produto")
    print("4. Alterar produto")
    print("5. Excluir produto")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        cadastrar_produto(estoque, nome, preco)
        salvar_dados(estoque)

    elif opcao == "2":
        listar_produtos(estoque)

    elif opcao == "3":
        nome = input("Digite o nome do produto que deseja buscar: ")
        buscar_produto(estoque, nome)

    elif opcao == "4":

        nome = input("Digite o nome do produto que deseja alterar: ")
        novo_nome = input("Novo nome (aperte enter para manter o mesmo): ")
        novo_preco = input("Novo preço (aperte enter para manter o mesmo): ")

        if novo_preco:
            novo_preco = float(novo_preco)

        else:
            novo_preco = None

        alterar_produto(estoque, nome, novo_nome or None, novo_preco)
        salvar_dados(estoque)

    elif opcao == "5":
        nome = input("Digite o nome do produto que deseja excluir: ")
        confirmacao = input(f"Tem certeza que deseja excluir '{nome}' ? (s/n): ").lower()

        if confirmacao == "s":
            excluir_produto(estoque,nome)
            salvar_dados(estoque)
        
        else:
            print("Exclusão cancelada.")

    elif opcao == "6":
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
