#declarando a lista de produtos em estoque
Lista_Produtos[]

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
    
    #método principal, cadastrar os produtos
    def Cadastrar_Produto(self):
        
        #Atribuindo Nome
        Nome = input("Nome do produto: ").strip()

        #Validando e atribuindo ID
        while True:git 
            ID = input("ID do produto: ").strip()
            #verifica se o ID está vazio e se já está cadastrado
            if ID:
                contador = 0
                for Produto in Lista_Produtos:
                    if Produto.ID == ID:
                        contador+=1
                if contador > 0:
                    print(f"O ID {ID} já foi cadastrado! ")
                    continue
                else:
                    self.ID = ID
                    break
            else:
                print("O ID do produto não pode estar vazio!")

            #validando e atribuindo o Preco
            while True:
                try:
                    self.Preco = float(input("Preço do produto em R$: "))
                    if self.Preco < 0:
                        print("O preço deve ser maior ou igual a 0!")
                        continue
                    break
                except ValueError as e:
                    print(f"Erro: {e} Digite apenas números!")

            #validando e atribuindo a Quantidade
            while True:
                try:
                    self.Quantidade = int(input("Quantidade do produto em estoque: "))
                    if self.Quantidade < 0:
                        print("Digite um valor maior que 0!")
                        continue
                    break
                except ValueError as e:
                    print(f"Erro: {e} Digite apenas números!")
            
            if self.Quantidade > 0:
                Lista_Produtos.append(Estoque(self.ID,self.Preco))
            

    #função para calcular o preço final com imposto de uma determinada quantidade de um produto
    def Calcular_Imposto(self,Preco,Quantidade):
        Imposto = Preco * 0.15
        Total = (Preco + Imposto) * Quantidade
        return Total

    #função listar_produtos


class Estoque:
    def __init__(self,_CodigoProduto,_ValorProduto):
        self._CodigoProduto = _CodigoProduto
        self._ValorProduto = _ValorProduto
    