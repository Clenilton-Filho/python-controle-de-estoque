#importando a biblioteca tkinter


from tkinter import * 


#declarando a lista de produtos em estoque
Produtos_Cadastrados = []
Estoque_Produtos = []

class Cliente:
    def __init__(self,_Nome,_Email):
        self._Nome = _Nome
        self._Email = _Email
    
    @property
    def Nome(self):
        return self._Nome
    @property
    def Email(self):
        return self._Email
    
    @Nome.setter
    def Nome(self,novoNome):
        self._Nome = novoNome
    @Email.setter
    def Email(self,novoEmail):
        self._Email = novoEmail

class Produto:
    def __init__(self,_Nome,_ID,_Preco,_Quantidade):
        self._Nome = _Nome
        self._ID = _ID
        self._Preco = _Preco
        self._Quantidade = _Quantidade

    #decoradores
    @property
    def Nome(self):
        return self._Nome
    @property
    def ID(self):
        return self._ID
    @property
    def Preco(self):
        return self._Preco
    @property
    def Quantidade(self):
        return self._Quantidade

    @Nome.setter
    def Nome(self,NovoNome):
        self._Nome = NovoNome
    @ID.setter
    def ID(self,NovoID):
        self._ID = NovoID
    @Preco.setter
    def Preco(self,NovoPreco):
        self._Preco = NovoPreco
    @Quantidade.setter
    def Quantidade(self,NovaQuantidade):
        self._Quantidade = NovaQuantidade
    
    #método principal, cadastrar os produtos (pode ser acessada sem objeto)
    @classmethod
    def Cadastrar_Produto(cls):
        print(f"\n--- Cadastrando o {len(Produtos_Cadastrados)+1}º Produto ---")
        #Atribuindo Nome
        Nome = input("Nome do produto: ").strip()

        #Validando o ID
        while True:
            ID = input("ID do produto: ").strip()
            #verifica se o ID está vazio e se já está cadastrado
            if ID:
                contador = 0
                if Produtos_Cadastrados:
                    for Produto in Produtos_Cadastrados:
                        if Produto.ID == ID:
                            contador+=1
                if contador > 0:
                    print(f"O ID {ID} já foi cadastrado! ")
                    continue
                else:
                    break
            else:
                print("O ID do produto não pode estar vazio!")

        #Validando o Preco
        while True:
            try:
                Preco = float(input("Preço do produto: R$"))
                if Preco < 0:
                    print("O preço deve ser maior ou igual a 0!")
                    continue
                break
            except ValueError as e:
                print(f"Erro: {e} Digite apenas números!")

        #validando a Quantidade
        while True:
            try:
                Quantidade = int(input("Quantidade do produto em estoque: "))
                if Quantidade < 0:
                    print("Digite um valor maior que 0!")
                    continue
                break
            except ValueError as e:
                print(f"Erro: {e} Digite apenas números!")
        
        Novo_Produto = cls(Nome,ID,Preco,Quantidade)

        Produtos_Cadastrados.append(Novo_Produto)
        if Quantidade > 0:
            Estoque_Produtos.append(Estoque(ID,Preco))
        
        print("Produto Cadastrado!")

        return Novo_Produto
            

    #função para calcular o preço final com imposto de uma determinada quantidade de um produto
    
    #transformar em staticmethod
    def Calcular_Imposto(self,Preco,Quantidade):
        Imposto = Preco * 0.15
        if Quantidade == None:
            Total = Preco + Imposto
        else:
            Total = (Preco + Imposto) * Quantidade
        return Total

    #método listar_produtos
    #mudar para classmethod
    def Listar_Produtos(self):
        if Produtos_Cadastrados:
            contador = 1
            print(f"\n --- Listando Produtos Cadastrados ---")
            for Produto in Produtos_Cadastrados:
                print(f'''\n--- {contador}º Produto ---
Nome do produto: {Produto.Nome}
ID do produto: {Produto.ID}
Preço original do produto: R${Produto.Preco:.2f}
Preço final do produto com imposto: R${self.Calcular_Imposto(Produto.Preco,None):.2f}
Quantidade do produto em estoque: {Produto.Quantidade}''')
                contador += 1
        else:
            print("Nenhum produto cadastrado!")

class Estoque:
    def __init__(self,_CodigoProduto,_ValorProduto):
        self._CodigoProduto = _CodigoProduto
        self._ValorProduto = _ValorProduto

#def Cadastrar_Cliente():

#def Visualizar_Estoque():



Produto1 = Produto.Cadastrar_Produto()

Produto2 = Produto.Cadastrar_Produto()

Produto1.Listar_Produtos()