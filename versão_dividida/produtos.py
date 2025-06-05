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
