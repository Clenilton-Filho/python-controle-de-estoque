from datetime import datetime

def cadastrar_produto(estoque, nome, preco):
    produto = {
        "nome": nome,
        "preço": preco,
        "data_cadastro": datetime.now().strftime("%d / %m / %Y | %H:%M:%S")
    }
    estoque.append(produto)
    print("Produto cadastrado com sucesso.")

def listar_produtos(estoque):
    if not estoque:
        print("Nenhum produto cadastrado.")
    else:
        for i, produto in enumerate(estoque, 1):
            print(f"{i}. Nome: {produto['nome']}, Preço: R${produto['preço']:.2f} Cadastrado em: {produto.get('data_cadastro', 'Data desconhecida')}")
        print(f"\nTotal de produtos cadastrados: {len(estoque)}")
        
def buscar_produto(estoque, nome):
    encontrados = [produto for produto in estoque if produto["nome"].lower() == nome.lower()]
    if encontrados:
        for produto in encontrados:
            print(f"Nome: {produto['nome']}, Preço: R${produto['preço']:.2f}")
    else:
        print("Produto não encontrado.")

def alterar_produto(estoque, nome, novo_nome=None, novo_preco=None):
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            if novo_nome:
                produto["nome"] = novo_nome
            if novo_preco is not None:
                produto["preço"] = novo_preco
            print("Produto alterado com sucesso.")
            return
    print("Produto não encontrado.")

def excluir_produto(estoque, nome):
    for i, produto in enumerate(estoque):
        if produto["nome"].lower() == nome.lower():
            del estoque[i]
            print("Produto excluído com sucesso.")
            return
    print("Produto não encontrado.")