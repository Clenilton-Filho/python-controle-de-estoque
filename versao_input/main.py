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
            Nome = input("\nNome completo do cliente: ").strip()

            #Verifica se o nome já está cadastrado
            for Item_Cliente in Clientes:
                if Item_Cliente.Nome == Nome:
                    contador+=1
            if contador > 0:
                print("\nO nome já está cadastrado!")
                continue
            break

        #Validação básica de e-mail
        while True:
            Email = input("E-mail do cliente: ").strip()
            if '@' not in Email or '.' not in Email:
                print("\nE-mail inválido!")
                continue
            break
        
        Clientes.append(cls(Nome,Email))
        print("\nCliente cadastrado!")

    #Lista os dados dos clientes cadastrados (acessível sem objetos)
    @staticmethod
    def Listar_Clientes():
        if Clientes:
            contador = 1
            print("\n--- Listando Clientes ---")
            for Item_Cliente in Clientes:
                print(f'''
--- {contador}º cliente ---
Nome do cliente: {Item_Cliente.Nome}
E-mail do cliente: {Item_Cliente.Email}''')
                contador+=1
        else:
            print("\nNenhum cliente cadastrado!")
    
    @staticmethod
    def Excluir_Cliente():
        if Clientes:
            while True: 
                Nome = input("Digite o nome do cliente ou 'sair' para voltar: ").strip()
                if Nome == 'sair':
                    break
                for Item_Cliente in Clientes:
                    if Item_Cliente.Nome == Nome:
                        Clientes.remove(Item_Cliente)
                        print("\nCliente excluído!")
                        return
                print(f'''\nO nome "{Nome}" não foi encontrado!''')
        else:
            print("Nenhum cliente cadastrado para excluir!")
        
class Produto:
    def __init__(self,_Nome,_ID,_Preco,_Quantidade):
        self._Nome = _Nome
        self._ID = _ID
        self._Preco = _Preco
        self._Quantidade = _Quantidade

    #Decoradores
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
    
    #Método principal, cadastrar os produtos
    @classmethod
    def Cadastrar_Produto(cls):
        print(f"\n--- Cadastrando o {len(Produtos_Cadastrados)+1}º Produto ---")
        #Atribuindo Nome
        Nome = input("\nNome do produto: ").strip()

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
                    print(f"\nO ID {ID} já foi cadastrado! ")
                    continue
                else:
                    break
            else:
                print("\nO ID do produto não pode estar vazio!")

        #Validando o Preço
        while True:
            try:
                Preco = float(input("Preço do produto: R$"))
                if Preco < 0:
                    print("\nO preço deve ser maior ou igual a 0!")
                    continue
                break
            except ValueError:
                print(f"\nErro! Digite apenas números!")

        #Validando a Quantidade
        while True:
            try:
                Quantidade = int(input("Quantidade do produto em estoque: "))
                if Quantidade < 0:
                    print("\nDigite um valor maior que 0!")
                    continue
                break
            except ValueError:
                print(f"\nErro! Digite apenas números!")

        #Cadastra o produto e, se a quantidade for maior que 0, coloca também na lista de estoque
        Produtos_Cadastrados.append(cls(Nome,ID,Preco,Quantidade))
        if Quantidade > 0:
            Estoque_Produtos.append(Estoque(ID,Preco))
        
        print("\nProduto cadastrado!")
    
    #Exclui o cadastro de um produto caso o usuário digite um ID válido
    @staticmethod
    def Excluir_Cadastro_Produto():
        while True:
            ID = input("\nDigite o ID do produto ou 'sair' para voltar: ").strip()
            if ID == 'sair':
                break
            for Item_Produto in Produtos_Cadastrados:
                if Item_Produto.ID == ID:
                    Produtos_Cadastrados.remove(Item_Produto)
                    for Item_Estoque in Estoque_Produtos:
                        if Item_Estoque.CodigoProduto == ID:
                            Estoque_Produtos.remove(Item_Estoque)
                            break
                    print(f"\nCadastro removido!")
                    return
            print(f"\nID {ID} não encontrado!")



    #Função para calcular o preço final com imposto de um produto
    @staticmethod
    def Calcular_Imposto(Preco,Quantidade = 0):
        Imposto = Preco * 0.15
        if Quantidade == 0:
            Total = Preco + Imposto
        else:
            Total = (Preco + Imposto) * Quantidade
        return Total

    #Método listar_produtos
    @classmethod
    def Listar_Produtos(cls):
        #Verifica se existem produtos cadastrados e usa um contador para enumerar os produtos
        if Produtos_Cadastrados:
            contador = 1
            print(f"\n--- Listando Produtos Cadastrados ---")
            for Produto in Produtos_Cadastrados:
                print(f'''\n--- {contador}º Produto ---
Nome do produto: {Produto.Nome}
ID do produto: {Produto.ID}
Preço original do produto: R${Produto.Preco:.2f}
Preço final do produto com imposto: R${cls.Calcular_Imposto(Produto.Preco):.2f}
Quantidade do produto em estoque: {Produto.Quantidade}''')
                contador += 1
        else:
            print("\nNenhum produto cadastrado!")

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
    
    @CodigoProduto.setter
    def CodigoProduto(self,NovoCodigo):
        self._CodigoProduto = NovoCodigo
    @ValorProduto.setter
    def ValorProduto(self,NovoValor):
        self._ValorProduto = NovoValor

    @staticmethod
    #Lista todos os produtos em estoque e seus dados, como nome, código (ID) valor com e sem imposto e a quantidade
    def Visualizar_Estoque():
        #Verifica se existem produtos em estoque
        if Estoque_Produtos:
                contador = 1
                print(f"\n --- Listando Estoque ---")
                for Item_Produto in Estoque_Produtos:
                    for Cadastro in Produtos_Cadastrados:
                        if Cadastro.ID == Item_Produto.CodigoProduto:
                            Nome = Cadastro.Nome
                            Quantidade = Cadastro.Quantidade
                            print(f"\n--- {contador}º Produto ---")
                            print(f"Código do produto: {Item_Produto.CodigoProduto}")
                            if Nome != '':
                                print(f"Nome do produto: {Nome}")
                            print(f"Valor do produto sem imposto: R${Item_Produto.ValorProduto}")
                            print(f"Valor do produto com imposto: R${Produto.Calcular_Imposto(Item_Produto.ValorProduto)}")
                            print(f"Quantidade em estoque: {Quantidade}")
                            contador += 1
        else:
            print("\nNenhum produto em estoque!")
    @staticmethod
    #Função para aumentar a quantidade de um produto no estoque
    def Reabastecer_Estoque():
        if Estoque_Produtos:
            while True:
                #Validação do ID e quantidade a adicionar
                ID = input("\nID do produto: ").strip()
                if ID == '':
                    print("\nO ID não pode ser vazio!")
                    continue
                while True:
                    try:
                        Quantidade = int(input("Quantidade para reabastecer: "))
                        if Quantidade <= 0:
                            print("\nA quantidade abastecida precisa ser maior que 0!")
                            continue
                        break
                    except ValueError :
                        print(f"\nErro! Digite apenas números!")
                        continue
                
                for Item_Produto in Produtos_Cadastrados:
                    if Item_Produto.ID == ID:
                        #Se a quantidade inicial for 0, coloca o item no estoque
                        if Item_Produto.Quantidade == 0:
                            Estoque_Produtos.append(Estoque(Item_Produto.ID,Item_Produto.Preco))
                        Item_Produto.Quantidade += Quantidade
                        
                        #Para a função se conseguir alterar a quantidade
                        print("\nProduto reabastecido!")
                        return
                print(f'''\nO ID "{ID}" não está cadastrado!''')
        else:
            print("\nNenhum produto em estoque para reabastecer!")
    
    @staticmethod    
    #Função para retirar uma quantidade de um produto no estoque
    def Retirar_Produto():
        if Estoque_Produtos:
            while True:
                #validação do ID e quantidade a retirar
                ID = input("\nDigite o ID do produto ou 'sair' para voltar: ").strip()
                if ID == '':
                    print("\nO ID não pode ser vazio!")
                    continue
                elif ID == 'sair':
                    break
                for Item_Produto in Produtos_Cadastrados:
                    #Somente pede a quantidade se o produto for encontrado
                    if Item_Produto.ID == ID:
                        while True:
                                try:
                                    Quantidade = int(input("Quantidade para retirar: "))
                                    if Quantidade <= 0:
                                        print("\nA quantidade retirada precisa ser maior que 0!")
                                        continue
                                    if Item_Produto.Quantidade - Quantidade < 0:
                                        print(f"\nQuantidade inválida, o estoque do produto ficaria negativo!")
                                        continue

                                    break
                                except ValueError :
                                    print(f"\nErro! Digite apenas números!")
                                    continue
                        #Para a função se conseguir alterar a quantidade
                        Item_Produto.Quantidade -= Quantidade
                        
                        #Se o produto ficar com quantidade 0, tira do estoque
                        if Item_Produto.Quantidade == 0:
                            for Item in Estoque_Produtos:
                                if Item.CodigoProduto == ID:
                                    Estoque_Produtos.remove(Item)
                                    break
                        
                        print("\nQuantidade retirada!")
                        return
                    print(f'''\nO ID "{ID}" não está cadastrado!''')
        else:
            print("\nNenhum produto em estoque para retirar!")


#Menu com opções referentes aos clientes
def Menu_Clientes():
        print('''\n---Opções de Clientes---
[1] - Cadastrar Cliente
[2] - Listar Clientes Cadastrados
[3] - Excluir Cliente
[4] - Voltar ao Menu Principal''')
        while True:
            Opcao_Clientes = input("\nDigite a opção desejada: ").strip()
            if Opcao_Clientes not in ('1234') or len(Opcao_Clientes) != 1:
                print("\nResposta inválida!")
                continue
            match Opcao_Clientes:
                case '1':
                    Cliente.Cadastrar_Cliente()
                case '2':
                    Cliente.Listar_Clientes()
                case '3':
                    Cliente.Excluir_Cliente()
                case '4':
                    break
            break

        print("\nVoltando ao menu principal...")

#Menu com opções referentes aos produtos
def Menu_Produto():
        print('''\n---Opções de Produto---
[1] - Cadastrar Produto
[2] - Listar Produtos Cadastrados
[3] - Excluir Cadastro de um Produto
[4] - Voltar ao Menu Principal''')
        while True:
            Opcao_Produto = input("\nDigite a opção desejada: ").strip()
            if Opcao_Produto not in ('1234') or len(Opcao_Produto) != 1:
                print("\nResposta inválida!")
                continue
            break
        match Opcao_Produto:
            case '1':
                Produto.Cadastrar_Produto()
            case '2':
                Produto.Listar_Produtos()
            case '3':
                Produto.Excluir_Cadastro_Produto()
            case '4':
                print("\nAté mais!")
        print("\nVoltando ao menu principal...")
        
#Menu com opções referentes aos produtos em estoque
def Menu_Estoque():
        print('''\n---Opções de Estoque---
[1] - Listar Produtos em Estoque
[2] - Reabastecer Estoque de um Produto
[3] - Retirar uma Quantidade de um Produto no Estoque
[4] - Voltar ao Menu Principal''')
        while True:
            Opcao_Estoque = input("\nDigite a opção desejada: ").strip()
            if Opcao_Estoque not in ('1234') or len(Opcao_Estoque) != 1:
                print("\nResposta inválida!")
                continue
            match Opcao_Estoque:
                case '1':
                    Estoque.Visualizar_Estoque()
                case '2':
                    Estoque.Reabastecer_Estoque()
                case '3':
                    Estoque.Retirar_Produto()
                case '4':
                    print("\nAté mais!")
            break
        print("\nVoltando ao menu principal...")
#Menu de opções para chamar as outras funções de menus
def Menu_Principal():
    while True:
        print('''\n---Menu de opções---
[1] - Opções de Produto
[2] - Opções de Estoque
[3] - Opções de Clientes
[4] - Sair do programa''')
        while True:
            Opcao_Menu = input("\nDigite a opção desejada: ").strip()
            if Opcao_Menu not in ('1234') or len(Opcao_Menu) != 1:
                print("\nResposta inválida!")
                continue
            break
        match Opcao_Menu:
            case '1':
                Menu_Produto()
            case '2':
                Menu_Estoque()
            case '3':
                Menu_Clientes()
            case '4':
                return

########Adicionar funcionalidades de compra/venda
############### PDF para entregar
####email - verificar se já está cadastrado, adicionar + mensagens de validação (faltando @, faltando .)
####tkinter na visualizacao de cliente



Menu_Principal()