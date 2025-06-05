from produtos import Produto

def ler_numero_positivo(mensagem="Digite um número positivo: "):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("O valor deve ser positivo!")
                continue
            return valor
        except ValueError:
            print("Digite um número válido!")

def Visualizar_Estoque(Estoque_Produtos, Produtos_Cadastrados):
    if Estoque_Produtos:
        contador = 1
        print(f"\n --- Listando Estoque ---")
        for Item_Produto in Estoque_Produtos:
            for Cadastro in Produtos_Cadastrados:
                if Cadastro.ID == Item_Produto.ID:
                    Nome = Cadastro.Nome
                    Quantidade = Item_Produto.Quantidade
                    print(f"\n--- {contador}º Produto ---")
                    print(f"Código do produto: {Item_Produto.ID}")
                    if Nome != '':
                        print(f"Nome do produto: {Nome}")
                    imposto, valor_com_imposto = Produto.Calcular_Imposto(Item_Produto.ValorProduto)
                    print(f"Valor do produto sem imposto: R${Item_Produto.ValorProduto:.2f}")
                    print(f"Imposto (10%): R${imposto:.2f}")
                    print(f"Valor do produto com imposto: R${valor_com_imposto:.2f}")
                    print(f"Quantidade em estoque: {Quantidade}")
                    contador += 1
    else:
        print("\nNenhum produto em estoque!")

def Reabastecer_Estoque(Estoque_Produtos):
    if not Estoque_Produtos:
        print("Estoque vazio. Não há produtos para reabastecer.")
        return

    try:
        codigo = int(input("Digite o código do produto para reabastecer: "))
    except ValueError:
        print("Digite um número válido.")
        return

    for produto in Estoque_Produtos:
        if produto.ID == codigo:
            quantidade = ler_numero_positivo("Digite a quantidade para adicionar ao estoque: ")
            produto.Quantidade += quantidade
            print("Estoque reabastecido!")
            return

    print("Produto não encontrado no estoque.")

def Retirar_Produto(Estoque_Produtos):
    if not Estoque_Produtos:
        print("Estoque vazio. Não há produtos para retirar.")
        return

    try:
        codigo = int(input("Digite o código do produto para retirar: "))
    except ValueError:
        print("Digite um número válido.")
        return

    for produto in Estoque_Produtos:
        if produto.ID == codigo:
            quantidade = ler_numero_positivo("Digite a quantidade para retirar do estoque: ")
            if quantidade > produto.Quantidade:
                print("Quantidade insuficiente no estoque!")
                return
            produto.Quantidade -= quantidade
            print("Produto retirado do estoque!")
            return

    print("Produto não encontrado no estoque.")
