import tkinter as tk
from tkinter import messagebox, scrolledtext

# Declarando as listas para produtos cadastrados, estoque de produtos e clientes
Produtos_Cadastrados = []
Estoque_Produtos = []
Clientes = []

# --- Classes de Lógica de Negócios (Mantidas o mais próximo possível do original) ---

class Cliente:
    def __init__(self, _Nome, _Email):
        self._Nome = _Nome
        self._Email = _Email

    # Decoradores
    @property
    def Nome(self):
        return self._Nome

    @property
    def Email(self):
        return self._Email

    @Nome.setter
    def Nome(self, novoNome):
        self._Nome = novoNome

    @Email.setter
    def Email(self, novoEmail):
        self._Email = novoEmail

    # Método para cadastrar os clientes (adaptado para GUI)
    @classmethod
    def Cadastrar_Cliente_GUI(cls, nome_entry, email_entry, status_label):
        nome = nome_entry.get().strip()
        email = email_entry.get().strip()

        if not nome:
            status_label.config(text="\nNome não pode ser vazio!", fg="red")
            return

        for Item_Cliente in Clientes:
            if Item_Cliente.Nome.lower() == nome.lower(): # Case-insensitive check
                status_label.config(text="\nO nome já está cadastrado!", fg="red")
                return

        if '@' not in email or '.' not in email:
            status_label.config(text="\nE-mail inválido!", fg="red")
            return
        
        for Item_Cliente in Clientes:
            if Item_Cliente.Email.lower() == email.lower(): # Case-insensitive check
                status_label.config(text="\nO e-mail já está cadastrado!", fg="red")
                return

        Clientes.append(cls(nome, email))
        nome_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        status_label.config(text="\nCliente cadastrado com sucesso!", fg="green")
        app.update_client_listbox() # Atualiza a lista na GUI


    # Lista os dados dos clientes cadastrados (adaptado para GUI)
    @staticmethod
    def Listar_Clientes_GUI(listbox):
        listbox.delete(0, tk.END) # Limpa a listbox
        if Clientes:
            for i, Item_Cliente in enumerate(Clientes):
                listbox.insert(tk.END, f"--- {i+1}º cliente ---")
                listbox.insert(tk.END, f"Nome do cliente: {Item_Cliente.Nome}")
                listbox.insert(tk.END, f"E-mail do cliente: {Item_Cliente.Email}")
                listbox.insert(tk.END, "-"*30) # Separador
        else:
            listbox.insert(tk.END, "Nenhum cliente cadastrado!")

    @staticmethod
    def Excluir_Cliente_GUI(nome_entry, status_label):
        nome_excluir = nome_entry.get().strip()
        if not nome_excluir:
            status_label.config(text="Digite o nome do cliente para excluir.", fg="red")
            return

        found = False
        for Item_Cliente in Clientes:
            if Item_Cliente.Nome.lower() == nome_excluir.lower(): # Case-insensitive check
                Clientes.remove(Item_Cliente)
                status_label.config(text="Cliente excluído com sucesso!", fg="green")
                found = True
                nome_entry.delete(0, tk.END)
                app.update_client_listbox() # Atualiza a lista na GUI
                break
        if not found:
            status_label.config(text=f'O nome "{nome_excluir}" não foi encontrado!', fg="red")

class Produto:
    def __init__(self, _Nome, _ID, _Preco, _Quantidade):
        self._Nome = _Nome
        self._ID = _ID
        self._Preco = _Preco
        self._Quantidade = _Quantidade

    # Decoradores
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
    def Nome(self, NovoNome):
        self._Nome = NovoNome
    @ID.setter
    def ID(self, NovoID):
        self._ID = NovoID
    @Preco.setter
    def Preco(self, NovoPreco):
        self._Preco = NovoPreco
    @Quantidade.setter
    def Quantidade(self, NovaQuantidade):
        self._Quantidade = NovaQuantidade
    
    # Método principal, cadastrar os produtos (adaptado para GUI)
    @classmethod
    def Cadastrar_Produto_GUI(cls, nome_entry, id_entry, preco_entry, quantidade_entry, status_label):
        nome = nome_entry.get().strip()
        id_prod = id_entry.get().strip()
        
        if not nome:
            status_label.config(text="Nome do produto não pode ser vazio!", fg="red")
            return

        if not id_prod:
            status_label.config(text="ID do produto não pode ser vazio!", fg="red")
            return
        
        for p in Produtos_Cadastrados:
            if p.ID == id_prod:
                status_label.config(text=f"O ID {id_prod} já foi cadastrado!", fg="red")
                return

        try:
            preco = float(preco_entry.get())
            if preco < 0:
                status_label.config(text="O preço deve ser maior ou igual a 0!", fg="red")
                return
        except ValueError:
            status_label.config(text="Preço inválido! Digite apenas números.", fg="red")
            return

        try:
            quantidade = int(quantidade_entry.get())
            if quantidade < 0:
                status_label.config(text="Quantidade inválida! Digite um valor maior ou igual a 0.", fg="red")
                return
        except ValueError:
            status_label.config(text="Quantidade inválida! Digite apenas números inteiros.", fg="red")
            return

        Produtos_Cadastrados.append(cls(nome, id_prod, preco, quantidade))
        if quantidade > 0:
            Estoque_Produtos.append(Estoque(id_prod, preco))
        
        nome_entry.delete(0, tk.END)
        id_entry.delete(0, tk.END)
        preco_entry.delete(0, tk.END)
        quantidade_entry.delete(0, tk.END)
        status_label.config(text="Produto cadastrado com sucesso!", fg="green")
        app.update_product_listbox() # Atualiza a lista na GUI
        app.update_stock_listbox()


    # Exclui o cadastro de um produto (adaptado para GUI)
    @staticmethod
    def Excluir_Cadastro_Produto_GUI(id_entry, status_label):
        id_excluir = id_entry.get().strip()
        if not id_excluir:
            status_label.config(text="Digite o ID do produto para excluir.", fg="red")
            return

        found_product = False
        for Item_Produto in Produtos_Cadastrados:
            if Item_Produto.ID == id_excluir:
                Produtos_Cadastrados.remove(Item_Produto)
                found_product = True
                
                # Remove do estoque também
                for Item_Estoque in Estoque_Produtos:
                    if Item_Estoque.CodigoProduto == id_excluir:
                        Estoque_Produtos.remove(Item_Estoque)
                        break
                
                status_label.config(text="Cadastro de produto removido com sucesso!", fg="green")
                id_entry.delete(0, tk.END)
                app.update_product_listbox()
                app.update_stock_listbox()
                break
        
        if not found_product:
            status_label.config(text=f'ID "{id_excluir}" não encontrado!', fg="red")

    # Função para calcular o preço final com imposto de um produto
    @staticmethod
    def Calcular_Imposto(Preco, Quantidade=0):
        Imposto = Preco * 0.15
        if Quantidade == 0:
            Total = Preco + Imposto
        else:
            Total = (Preco + Imposto) * Quantidade
        return Total

    # Método listar_produtos (adaptado para GUI)
    @classmethod
    def Listar_Produtos_GUI(cls, listbox):
        listbox.delete(0, tk.END)
        if Produtos_Cadastrados:
            for i, produto in enumerate(Produtos_Cadastrados):
                listbox.insert(tk.END, f"--- {i+1}º Produto ---")
                listbox.insert(tk.END, f"Nome do produto: {produto.Nome}")
                listbox.insert(tk.END, f"ID do produto: {produto.ID}")
                listbox.insert(tk.END, f"Preço original do produto: R${produto.Preco:.2f}")
                listbox.insert(tk.END, f"Preço final do produto com imposto: R${cls.Calcular_Imposto(produto.Preco):.2f}")
                listbox.insert(tk.END, f"Quantidade do produto em estoque: {produto.Quantidade}")
                listbox.insert(tk.END, "-"*30)
        else:
            listbox.insert(tk.END, "Nenhum produto cadastrado!")

class Estoque:
    def __init__(self, _CodigoProduto, _ValorProduto):
        self._CodigoProduto = _CodigoProduto
        self._ValorProduto = _ValorProduto
    
    # Decoradores
    @property
    def CodigoProduto(self):
        return self._CodigoProduto
    @property
    def ValorProduto(self):
        return self._ValorProduto
    
    @CodigoProduto.setter
    def CodigoProduto(self, NovoCodigo):
        self._CodigoProduto = NovoCodigo
    @ValorProduto.setter
    def ValorProduto(self, NovoValor):
        self._ValorProduto = NovoValor

    @staticmethod
    # Lista todos os produtos em estoque e seus dados (adaptado para GUI)
    def Visualizar_Estoque_GUI(listbox):
        listbox.delete(0, tk.END)
        if Estoque_Produtos:
            for i, Item_Estoque in enumerate(Estoque_Produtos):
                # Encontrar o produto correspondente em Produtos_Cadastrados para obter nome e quantidade
                nome = ""
                quantidade = 0
                for Cadastro in Produtos_Cadastrados:
                    if Cadastro.ID == Item_Estoque.CodigoProduto:
                        nome = Cadastro.Nome
                        quantidade = Cadastro.Quantidade
                        break
                
                listbox.insert(tk.END, f"--- {i+1}º Produto ---")
                listbox.insert(tk.END, f"Código do produto: {Item_Estoque.CodigoProduto}")
                if nome:
                    listbox.insert(tk.END, f"Nome do produto: {nome}")
                listbox.insert(tk.END, f"Valor do produto sem imposto: R${Item_Estoque.ValorProduto:.2f}")
                listbox.insert(tk.END, f"Valor do produto com imposto: R${Produto.Calcular_Imposto(Item_Estoque.ValorProduto):.2f}")
                listbox.insert(tk.END, f"Quantidade em estoque: {quantidade}")
                listbox.insert(tk.END, "-"*30)
        else:
            listbox.insert(tk.END, "Nenhum produto em estoque!")
    
    @staticmethod
    # Função para aumentar a quantidade de um produto no estoque (adaptado para GUI)
    def Reabastecer_Estoque_GUI(id_entry, quantidade_entry, status_label):
        id_prod = id_entry.get().strip()
        
        if not id_prod:
            status_label.config(text="O ID não pode ser vazio!", fg="red")
            return

        try:
            quantidade_add = int(quantidade_entry.get())
            if quantidade_add <= 0:
                status_label.config(text="A quantidade a abastecer precisa ser maior que 0!", fg="red")
                return
        except ValueError:
            status_label.config(text="Quantidade inválida! Digite apenas números inteiros.", fg="red")
            return
        
        found = False
        for Item_Produto in Produtos_Cadastrados:
            if Item_Produto.ID == id_prod:
                if Item_Produto.Quantidade == 0:
                    Estoque_Produtos.append(Estoque(Item_Produto.ID, Item_Produto.Preco))
                Item_Produto.Quantidade += quantidade_add
                status_label.config(text="Produto reabastecido com sucesso!", fg="green")
                found = True
                id_entry.delete(0, tk.END)
                quantidade_entry.delete(0, tk.END)
                app.update_stock_listbox()
                app.update_product_listbox()
                break
        
        if not found:
            status_label.config(text=f'O ID "{id_prod}" não está cadastrado!', fg="red")
    
    @staticmethod     
    # Função para retirar uma quantidade de um produto no estoque (adaptado para GUI)
    def Retirar_Produto_GUI(id_entry, quantidade_entry, status_label):
        id_prod = id_entry.get().strip()
        
        if not id_prod:
            status_label.config(text="O ID não pode ser vazio!", fg="red")
            return
        
        found_product = False
        for Item_Produto in Produtos_Cadastrados:
            if Item_Produto.ID == id_prod:
                found_product = True
                try:
                    quantidade_retirar = int(quantidade_entry.get())
                    if quantidade_retirar <= 0:
                        status_label.config(text="A quantidade retirada precisa ser maior que 0!", fg="red")
                        return
                    if Item_Produto.Quantidade - quantidade_retirar < 0:
                        status_label.config(text="Quantidade inválida, o estoque do produto ficaria negativo!", fg="red")
                        return
                except ValueError:
                    status_label.config(text="Quantidade inválida! Digite apenas números inteiros.", fg="red")
                    return
                
                Item_Produto.Quantidade -= quantidade_retirar
                
                if Item_Produto.Quantidade == 0:
                    for Item in Estoque_Produtos:
                        if Item.CodigoProduto == id_prod:
                            Estoque_Produtos.remove(Item)
                            break
                
                status_label.config(text="Quantidade retirada com sucesso!", fg="green")
                id_entry.delete(0, tk.END)
                quantidade_entry.delete(0, tk.END)
                app.update_stock_listbox()
                app.update_product_listbox()
                break
        
        if not found_product:
            status_label.config(text=f'O ID "{id_prod}" não está cadastrado!', fg="red")

# --- Interface Gráfica Tkinter ---

class AplicacaoEstoque(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gerenciamento de Estoque")
        self.geometry("800x600")

        self.frames = {}
        self.create_frames()
        self.show_frame("MenuPrincipal")

    def create_frames(self):
        # Menu Principal
        self.frames["MenuPrincipal"] = MenuPrincipalFrame(self, self)
        self.frames["MenuPrincipal"].grid(row=0, column=0, sticky="nsew")

        # Menu Clientes
        self.frames["MenuClientes"] = MenuClientesFrame(self, self)
        self.frames["MenuClientes"].grid(row=0, column=0, sticky="nsew")

        # Menu Produtos
        self.frames["MenuProduto"] = MenuProdutoFrame(self, self)
        self.frames["MenuProduto"].grid(row=0, column=0, sticky="nsew")

        # Menu Estoque
        self.frames["MenuEstoque"] = MenuEstoqueFrame(self, self)
        self.frames["MenuEstoque"].grid(row=0, column=0, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()
        # Atualiza as listboxes quando a tela é exibida
        if frame_name == "MenuClientes":
            self.frames["MenuClientes"].update_listbox()
        elif frame_name == "MenuProduto":
            self.frames["MenuProduto"].update_listbox()
        elif frame_name == "MenuEstoque":
            self.frames["MenuEstoque"].update_listbox()

    def update_client_listbox(self):
        self.frames["MenuClientes"].update_listbox()

    def update_product_listbox(self):
        self.frames["MenuProduto"].update_listbox()

    def update_stock_listbox(self):
        self.frames["MenuEstoque"].update_listbox()

class MenuPrincipalFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f0f0f0") # Cor de fundo

        tk.Label(self, text="--- Menu Principal ---", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=20)

        tk.Button(self, text="Opções de Produto", command=lambda: controller.show_frame("MenuProduto"),
                  font=("Arial", 14), bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=10)
        tk.Button(self, text="Opções de Estoque", command=lambda: controller.show_frame("MenuEstoque"),
                  font=("Arial", 14), bg="#2196F3", fg="white", padx=10, pady=5).pack(pady=10)
        tk.Button(self, text="Opções de Clientes", command=lambda: controller.show_frame("MenuClientes"),
                  font=("Arial", 14), bg="#FFC107", fg="black", padx=10, pady=5).pack(pady=10)
        tk.Button(self, text="Sair do programa", command=self.controller.quit,
                  font=("Arial", 14), bg="#F44336", fg="white", padx=10, pady=5).pack(pady=10)

class MenuClientesFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f0f0f0")

        tk.Label(self, text="--- Opções de Clientes ---", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)

        # Cadastro de Cliente
        cadastro_frame = tk.LabelFrame(self, text="Cadastrar Cliente", bg="#f0f0f0", padx=10, pady=10)
        cadastro_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(cadastro_frame, text="Nome:", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.nome_entry = tk.Entry(cadastro_frame, width=40)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=2, sticky="ew")

        tk.Label(cadastro_frame, text="E-mail:", bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.email_entry = tk.Entry(cadastro_frame, width=40)
        self.email_entry.grid(row=1, column=1, padx=5, pady=2, sticky="ew")

        self.status_label_cliente = tk.Label(cadastro_frame, text="", bg="#f0f0f0", font=("Arial", 10))
        self.status_label_cliente.grid(row=2, column=0, columnspan=2, pady=5, sticky="ew")

        tk.Button(cadastro_frame, text="Cadastrar", 
                  command=lambda: Cliente.Cadastrar_Cliente_GUI(self.nome_entry, self.email_entry, self.status_label_cliente),
                  bg="#64B5F6", fg="white").grid(row=3, column=0, columnspan=2, pady=5, sticky="ew")
        
        # Excluir Cliente
        excluir_frame = tk.LabelFrame(self, text="Excluir Cliente", bg="#f0f0f0", padx=10, pady=10)
        excluir_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(excluir_frame, text="Nome do Cliente:", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.excluir_nome_entry = tk.Entry(excluir_frame, width=40)
        self.excluir_nome_entry.grid(row=0, column=1, padx=5, pady=2, sticky="ew")

        self.status_label_excluir_cliente = tk.Label(excluir_frame, text="", bg="#f0f0f0", font=("Arial", 10))
        self.status_label_excluir_cliente.grid(row=1, column=0, columnspan=2, pady=5, sticky="ew")

        tk.Button(excluir_frame, text="Excluir", 
                  command=lambda: Cliente.Excluir_Cliente_GUI(self.excluir_nome_entry, self.status_label_excluir_cliente),
                  bg="#EF5350", fg="white").grid(row=2, column=0, columnspan=2, pady=5, sticky="ew")


        # Listagem de Clientes
        listagem_frame = tk.LabelFrame(self, text="Clientes Cadastrados", bg="#f0f0f0", padx=10, pady=10)
        listagem_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.listbox_clientes = scrolledtext.ScrolledText(listagem_frame, height=10, width=60)
        self.listbox_clientes.pack(fill="both", expand=True)

        tk.Button(listagem_frame, text="Atualizar Lista", command=self.update_listbox,
                  bg="#9CCC65", fg="white").pack(pady=5)

        tk.Button(self, text="Voltar ao Menu Principal", command=lambda: controller.show_frame("MenuPrincipal"),
                  bg="#757575", fg="white").pack(pady=10)
        
        self.update_listbox() # Carrega a lista ao iniciar o frame

    def update_listbox(self):
        self.listbox_clientes.delete(1.0, tk.END) # Limpa o Text widget
        if Clientes:
            for i, Item_Cliente in enumerate(Clientes):
                self.listbox_clientes.insert(tk.END, f"--- {i+1}º cliente ---\n")
                self.listbox_clientes.insert(tk.END, f"Nome do cliente: {Item_Cliente.Nome}\n")
                self.listbox_clientes.insert(tk.END, f"E-mail do cliente: {Item_Cliente.Email}\n")
                self.listbox_clientes.insert(tk.END, "-"*30 + "\n\n")
        else:
            self.listbox_clientes.insert(tk.END, "Nenhum cliente cadastrado!")


class MenuProdutoFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f0f0f0")

        tk.Label(self, text="--- Opções de Produto ---", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)

        # Cadastro de Produto
        cadastro_frame = tk.LabelFrame(self, text="Cadastrar Produto", bg="#f0f0f0", padx=10, pady=10)
        cadastro_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(cadastro_frame, text="Nome:", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.nome_entry = tk.Entry(cadastro_frame, width=40)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=2, sticky="ew")

        tk.Label(cadastro_frame, text="ID:", bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.id_entry = tk.Entry(cadastro_frame, width=40)
        self.id_entry.grid(row=1, column=1, padx=5, pady=2, sticky="ew")

        tk.Label(cadastro_frame, text="Preço (R$):", bg="#f0f0f0").grid(row=2, column=0, padx=5, pady=2, sticky="w")
        self.preco_entry = tk.Entry(cadastro_frame, width=40)
        self.preco_entry.grid(row=2, column=1, padx=5, pady=2, sticky="ew")

        tk.Label(cadastro_frame, text="Quantidade:", bg="#f0f0f0").grid(row=3, column=0, padx=5, pady=2, sticky="w")
        self.quantidade_entry = tk.Entry(cadastro_frame, width=40)
        self.quantidade_entry.grid(row=3, column=1, padx=5, pady=2, sticky="ew")

        self.status_label_produto = tk.Label(cadastro_frame, text="", bg="#f0f0f0", font=("Arial", 10))
        self.status_label_produto.grid(row=4, column=0, columnspan=2, pady=5, sticky="ew")

        tk.Button(cadastro_frame, text="Cadastrar Produto", 
                  command=lambda: Produto.Cadastrar_Produto_GUI(self.nome_entry, self.id_entry, self.preco_entry, self.quantidade_entry, self.status_label_produto),
                  bg="#64B5F6", fg="white").grid(row=5, column=0, columnspan=2, pady=5, sticky="ew")
        
        # Excluir Produto
        excluir_frame = tk.LabelFrame(self, text="Excluir Cadastro de Produto", bg="#f0f0f0", padx=10, pady=10)
        excluir_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(excluir_frame, text="ID do Produto:", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.excluir_id_entry = tk.Entry(excluir_frame, width=40)
        self.excluir_id_entry.grid(row=0, column=1, padx=5, pady=2, sticky="ew")

        self.status_label_excluir_produto = tk.Label(excluir_frame, text="", bg="#f0f0f0", font=("Arial", 10))
        self.status_label_excluir_produto.grid(row=1, column=0, columnspan=2, pady=5, sticky="ew")

        tk.Button(excluir_frame, text="Excluir", 
                  command=lambda: Produto.Excluir_Cadastro_Produto_GUI(self.excluir_id_entry, self.status_label_excluir_produto),
                  bg="#EF5350", fg="white").grid(row=2, column=0, columnspan=2, pady=5, sticky="ew")

        # Listagem de Produtos
        listagem_frame = tk.LabelFrame(self, text="Produtos Cadastrados", bg="#f0f0f0", padx=10, pady=10)
        listagem_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.listbox_produtos = scrolledtext.ScrolledText(listagem_frame, height=10, width=60)
        self.listbox_produtos.pack(fill="both", expand=True)
        tk.Button(listagem_frame, text="Atualizar Lista", command=self.update_listbox,
                  bg="#9CCC65", fg="white").pack(pady=5)


        tk.Button(self, text="Voltar ao Menu Principal", command=lambda: controller.show_frame("MenuPrincipal"),
                  bg="#757575", fg="white").pack(pady=10)
        
        self.update_listbox()

    def update_listbox(self):
        self.listbox_produtos.delete(1.0, tk.END)
        if Produtos_Cadastrados:
            for i, produto in enumerate(Produtos_Cadastrados):
                self.listbox_produtos.insert(tk.END, f"--- {i+1}º Produto ---\n")
                self.listbox_produtos.insert(tk.END, f"Nome do produto: {produto.Nome}\n")
                self.listbox_produtos.insert(tk.END, f"ID do produto: {produto.ID}\n")
                self.listbox_produtos.insert(tk.END, f"Preço original do produto: R${produto.Preco:.2f}\n")
                self.listbox_produtos.insert(tk.END, f"Preço final do produto com imposto: R${Produto.Calcular_Imposto(produto.Preco):.2f}\n")
                self.listbox_produtos.insert(tk.END, f"Quantidade do produto em estoque: {produto.Quantidade}\n")
                self.listbox_produtos.insert(tk.END, "-"*30 + "\n\n")
        else:
            self.listbox_produtos.insert(tk.END, "Nenhum produto cadastrado!")


class MenuEstoqueFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f0f0f0")

        tk.Label(self, text="--- Opções de Estoque ---", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)

        # Reabastecer Estoque
        reabastecer_frame = tk.LabelFrame(self, text="Reabastecer Estoque", bg="#f0f0f0", padx=10, pady=10)
        reabastecer_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(reabastecer_frame, text="ID do Produto:", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.reabastecer_id_entry = tk.Entry(reabastecer_frame, width=40)
        self.reabastecer_id_entry.grid(row=0, column=1, padx=5, pady=2, sticky="ew")

        tk.Label(reabastecer_frame, text="Quantidade para adicionar:", bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.reabastecer_quantidade_entry = tk.Entry(reabastecer_frame, width=40)
        self.reabastecer_quantidade_entry.grid(row=1, column=1, padx=5, pady=2, sticky="ew")

        self.status_label_reabastecer = tk.Label(reabastecer_frame, text="", bg="#f0f0f0", font=("Arial", 10))
        self.status_label_reabastecer.grid(row=2, column=0, columnspan=2, pady=5, sticky="ew")

        tk.Button(reabastecer_frame, text="Reabastecer", 
                  command=lambda: Estoque.Reabastecer_Estoque_GUI(self.reabastecer_id_entry, self.reabastecer_quantidade_entry, self.status_label_reabastecer),
                  bg="#64B5F6", fg="white").grid(row=3, column=0, columnspan=2, pady=5, sticky="ew")
        
        # Retirar Produto
        retirar_frame = tk.LabelFrame(self, text="Retirar Quantidade do Estoque", bg="#f0f0f0", padx=10, pady=10)
        retirar_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(retirar_frame, text="ID do Produto:", bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=2, sticky="w")
        self.retirar_id_entry = tk.Entry(retirar_frame, width=40)
        self.retirar_id_entry.grid(row=0, column=1, padx=5, pady=2, sticky="ew")

        tk.Label(retirar_frame, text="Quantidade para retirar:", bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=2, sticky="w")
        self.retirar_quantidade_entry = tk.Entry(retirar_frame, width=40)
        self.retirar_quantidade_entry.grid(row=1, column=1, padx=5, pady=2, sticky="ew")

        self.status_label_retirar = tk.Label(retirar_frame, text="", bg="#f0f0f0", font=("Arial", 10))
        self.status_label_retirar.grid(row=2, column=0, columnspan=2, pady=5, sticky="ew")

        tk.Button(retirar_frame, text="Retirar", 
                  command=lambda: Estoque.Retirar_Produto_GUI(self.retirar_id_entry, self.retirar_quantidade_entry, self.status_label_retirar),
                  bg="#EF5350", fg="white").grid(row=3, column=0, columnspan=2, pady=5, sticky="ew")

        # Listagem de Estoque
        listagem_frame = tk.LabelFrame(self, text="Produtos em Estoque", bg="#f0f0f0", padx=10, pady=10)
        listagem_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.listbox_estoque = scrolledtext.ScrolledText(listagem_frame, height=10, width=60)
        self.listbox_estoque.pack(fill="both", expand=True)
        tk.Button(listagem_frame, text="Atualizar Lista", command=self.update_listbox,
                  bg="#9CCC65", fg="white").pack(pady=5)


        tk.Button(self, text="Voltar ao Menu Principal", command=lambda: controller.show_frame("MenuPrincipal"),
                  bg="#757575", fg="white").pack(pady=10)
        
        self.update_listbox()

    def update_listbox(self):
        self.listbox_estoque.delete(1.0, tk.END)
        if Estoque_Produtos:
            for i, Item_Estoque in enumerate(Estoque_Produtos):
                nome = ""
                quantidade = 0
                for Cadastro in Produtos_Cadastrados:
                    if Cadastro.ID == Item_Estoque.CodigoProduto:
                        nome = Cadastro.Nome
                        quantidade = Cadastro.Quantidade
                        break
                
                self.listbox_estoque.insert(tk.END, f"--- {i+1}º Produto ---\n")
                self.listbox_estoque.insert(tk.END, f"Código do produto: {Item_Estoque.CodigoProduto}\n")
                if nome:
                    self.listbox_estoque.insert(tk.END, f"Nome do produto: {nome}\n")
                self.listbox_estoque.insert(tk.END, f"Valor do produto sem imposto: R${Item_Estoque.ValorProduto:.2f}\n")
                self.listbox_estoque.insert(tk.END, f"Valor do produto com imposto: R${Produto.Calcular_Imposto(Item_Estoque.ValorProduto):.2f}\n")
                self.listbox_estoque.insert(tk.END, f"Quantidade em estoque: {quantidade}\n")
                self.listbox_estoque.insert(tk.END, "-"*30 + "\n\n")
        else:
            self.listbox_estoque.insert(tk.END, "Nenhum produto em estoque!")


if __name__ == "__main__":
    app = AplicacaoEstoque()
    app.mainloop()