# produto.py

class Produto:
    def __init__(self, ID, Nome, Quantidade, Valor):
        self.ID = ID
        self.Nome = Nome
        self.Quantidade = Quantidade
        self.Valor = Valor

    def to_dict(self):
        return {
            "ID": self.ID,
            "Nome": self.Nome,
            "Quantidade": self.Quantidade,
            "Valor": self.Valor
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(
            ID=dados["ID"],
            Nome=dados["Nome"],
            Quantidade=dados.get("Quantidade", 0),
            Valor=dados["Valor"]
        )

    @staticmethod
    def Calcular_Imposto(valor):
        return valor * 1.1  # já calcula valor + 10%

    @classmethod
    def Cadastrar_Produto(cls, lista_produtos):
        while True:
            try:
                ID = int(input("ID do produto: "))
                if ID < 0:
                    print("ID deve ser >= 0")
                    continue
                if any(p.ID == ID for p in lista_produtos):
                    print("ID já cadastrado")
                    continue
                break
            except ValueError:
                print("Digite um número válido para ID")

        Nome = input("Nome do produto: ").strip()
        Quantidade = 0

        while True:
            try:
                Valor = float(input("Preço do produto: R$"))
                if Valor < 0:
                    print("\nO preço deve ser maior ou igual a 0!")
                    continue
                break
            except ValueError:
                print("\nErro! Digite apenas números!")

        novo_produto = cls(ID, Nome, Quantidade, Valor)
        lista_produtos.append(novo_produto)
        print("\nProduto cadastrado!")

    @staticmethod
    def Listar_Produtos(lista_produtos):
        if lista_produtos:
            print("\n--- Listando Produtos Cadastrados ---")
            for i, p in enumerate(lista_produtos, start=1):
                print(f'''
--- {i}º Produto ---
ID: {p.ID}
Nome: {p.Nome}
Quantidade em estoque: {p.Quantidade}
Preço (sem imposto): R${p.Valor:.2f}
Preço (com imposto): R${Produto.Calcular_Imposto(p.Valor):.2f}''')
        else:
            print("\nNenhum produto cadastrado!")

    @staticmethod
    def Excluir_Cadastro_Produto(lista_produtos):
        if lista_produtos:
            while True:
                try:
                    ID = int(input("Digite o ID do produto para excluir ou -1 para sair: "))
                    if ID == -1:
                        break
                    for p in lista_produtos:
                        if p.ID == ID:
                            lista_produtos.remove(p)
                            print("Produto excluído!")
                            return
                    print("Produto não encontrado.")
                except ValueError:
                    print("Digite um número válido.")
        else:
            print("Nenhum produto cadastrado para excluir!")
    
    @staticmethod
    def Atualizar_Produto_info(lista_produtos):
        if not lista_produtos:
            print("Nenhum produto cadastrado para realizar atualização")
            return
        id_Produto = input("Digite o ID do produto que será atualizado: ").strip()
        if not id_Produto:
            print("Nada foi inserido. Voltando ao menu")
            return
        try:
            id_Produto = int(id_Produto)
            if id_Produto < 0: 
                print("ID deve ser um numero maior ou igual a 0")
                return
        except ValueError:
            print("ID deve ser um número inteiro!")
            return

        for p in lista_produtos:
            if p.ID == id_Produto:
                Produto_Nome_Att = input("Digite o nome do produto: ")
                if not Produto_Nome_Att:
                    print("Nada foi inserido. Voltando ao menu")
                    return
                for prod in lista_produtos:
                    if prod.Nome == Produto_Nome_Att and prod.ID != id_Produto:
                        print(f"\nEste nome já está cadastrado.")
                        return
                p.Nome = Produto_Nome_Att
                print("\nProduto atualizado")
                Valor_Att_str = input("Digite o novo preço do produto: R$ ")
                if not Valor_Att_str:
                    print("Nada foi inserido. Voltando ao menu")
                    return
                try:
                    Valor_Att = float(Valor_Att_str)
                    if Valor_Att < 0:
                        print("\nO preço deve ser maior ou igual a 0!")
                        return
                    p.Valor = Valor_Att
                    print("\nProduto atualizado")
                except ValueError:
                    print("\nDigite apenas números!")
                    return
                return  
        print(f'\nO ID "{id_Produto}" não está cadastrado.')


