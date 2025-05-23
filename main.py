#declarando as listas para produtos cadastrados, estoque de produtos e clientes
Produtos_Cadastrados = []
Estoque_Produtos = []
Clientes = []

class Cliente:
    def __init__(self,_Nome,_Email):
        self._Nome = _Nome
        self._Email = _Email

    #decoradores
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

    #Método para cadastrar os clientes (acessível sem objetos)
    @classmethod
    def Cadastrar_Cliente(cls):
        while True:
            contador = 0
            Nome = input("Nome completo do cliente: ").strip()

            #Verifica se o nome já está cadastrado
            for Item_Cliente in Clientes:
                if Item_Cliente.Nome == Nome:
                    contador+=1
            if contador > 0:
                print("O nome já está cadastrado!")
                continue
            break

        #validação básica de e-mail
        while True:
            Email = input("E-mail do cliente: ").strip()
            if '@' not in Email or '.' not in Email:
                print("E-mail inválido!")
                continue
            break
        
        Clientes.append(cls(Nome,Email))
        return
        
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
    
    #método principal, cadastrar os produtos (acessível sem objetos)
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
            except ValueError:
                print(f"Erro! Digite apenas números!")

        #Validando a Quantidade
        while True:
            try:
                Quantidade = int(input("Quantidade do produto em estoque: "))
                if Quantidade < 0:
                    print("Digite um valor maior que 0!")
                    continue
                break
            except ValueError:
                print(f"Erro! Digite apenas números!")

        #Cadastra o produto e, se a quantidade for maior que 0, coloca também na lista com o estoque
        Produtos_Cadastrados.append(cls(Nome,ID,Preco,Quantidade))
        if Quantidade > 0:
            Estoque_Produtos.append(Estoque(ID,Preco))
        
        return
            

    #Função para calcular o preço final com imposto de um produto
    @staticmethod
    def Calcular_Imposto(Preco,Quantidade = 0):
        Imposto = Preco * 0.15
        if Quantidade == 0:
            Total = Preco + Imposto
        else:
            Total = (Preco + Imposto) * Quantidade
        return Total

    #Método listar_produtos (acessível sem objetos)
    @classmethod
    def Listar_Produtos(cls):
        #Verifica se existem produtos cadastrados e usa um contador para enumerar os produtos
        if Produtos_Cadastrados:
            contador = 1
            print(f"\n --- Listando Produtos Cadastrados ---")
            for Produto in Produtos_Cadastrados:
                print(f'''\n--- {contador}º Produto ---
Nome do produto: {Produto.Nome}
ID do produto: {Produto.ID}
Preço original do produto: R${Produto.Preco:.2f}
Preço final do produto com imposto: R${cls.Calcular_Imposto(Produto.Preco):.2f}
Quantidade do produto em estoque: {Produto.Quantidade}''')
                contador += 1
        else:
            print("Nenhum produto cadastrado!")

class Estoque:
    def __init__(self,_CodigoProduto,_ValorProduto):
        self._CodigoProduto = _CodigoProduto
        self._ValorProduto = _ValorProduto
    
    #Decoradores
    @property
    def CodigoProduto(self):
        return self._CodigoProduto
    @property
    def ValorProduto(self):
        return self._ValorProduto
    
#Lista todos os produtos em estoque e seus dados, como nome, código (ID) valor com e sem imposto e a quantidade
def Visualizar_Estoque():
    #Verifica se existem produtos em estoque
    if Estoque_Produtos:
            print(f"\n --- Listando Estoque ---\n")
            for Item_Produto in Estoque_Produtos:
                for Cadastro in Produtos_Cadastrados:
                    if Cadastro.ID == Item_Produto.CodigoProduto:
                        Nome = Cadastro.Nome
                        Quantidade = Cadastro.Quantidade
                        print(f"Código do produto: {Item_Produto.CodigoProduto}")
                        if Nome != '':
                            print(f"Nome do produto: {Nome}")
                        print(f"Valor do produto sem imposto: R${Item_Produto.ValorProduto}")
                        print(f"Valor do produto com imposto: R${Produto.Calcular_Imposto(Item_Produto.ValorProduto)}")
                        print(f"Quantidade em estoque: {Quantidade}")
    else:
        print("Nenhum produto em estoque!")

#Função para aumentar a quantidade de um produto no estoque
def Reabastecer_Estoque():
    while True:
        #Validação do ID e quantidade a adicionar
        ID = input("ID do produto: ").strip()
        if ID == '':
            print("O ID não pode ser vazio!")
            continue
        while True:
            try:
                Quantidade = int(input("Quantidade para reabastecer: "))
                if Quantidade <= 0:
                    print("A quantidade precisa ser maior que 0!")
                    continue
                break
            except ValueError :
                print(f"Erro! Digite apenas números!")
                continue
        
        for Item_Produto in Produtos_Cadastrados:
            #Para a função se conseguir alterar a quantidade
            if Item_Produto.ID == ID:
                #Se a quantidade inicial for 0, coloca o item no estoque
                if Item_Produto.Quantidade == 0:
                    Estoque_Produtos.append(Estoque(Item_Produto.ID,Item_Produto.Preco))
                Item_Produto.Quantidade += Quantidade
                return
        print(f'''O ID "{ID}" não está cadastrado!''')
        
#Função para retirar uma quantidade de um produto no estoque
def Retirar_Produto():
    while True:
        #validação do ID e quantidade a retirar
        ID = input("ID do produto: ").strip()
        if ID == '':
            print("O ID não pode ser vazio!")
            continue
        for Item_Produto in Produtos_Cadastrados:
            #Somente pede a quantidade se o produto for encontrado
            if Item_Produto.ID == ID:
                while True:
                        try:
                            Quantidade = int(input("Quantidade para retirar: "))
                            if Quantidade <= 0:
                                print("A quantidade precisa ser maior que 0!")
                                continue
                            if Item_Produto.Quantidade - Quantidade < 0:
                                print(f"Quantidade inválida, o estoque do produto ficaria negativo!")
                                continue

                            break
                        except ValueError :
                            print(f"Erro! Digite apenas números!")
                            continue
                #Para a função se conseguir alterar a quantidade
                Item_Produto.Quantidade -= Quantidade

                #Se o produto ficar com quantidade 0, tira do estoque
                if Item_Produto.Quantidade == 0:
                    for Item in Estoque_Produtos:
                        if Item.CodigoProduto == ID:
                            Estoque_Produtos.remove(Item)
                            break
                return
        print(f'''O ID "{ID}" não está cadastrado!''')
