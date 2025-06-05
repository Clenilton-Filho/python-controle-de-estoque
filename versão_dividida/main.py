import json
from produtos import Produto  
from estoque import Visualizar_Estoque, Reabastecer_Estoque, Retirar_Produto
from dados import salvar_lista_em_json, carregar_lista_de_json

ARQUIVO_PRODUTOS = "produtos_cadastrados.json"
ARQUIVO_ESTOQUE = "estoque_produtos.json"

Produtos_Cadastrados = []  # variável global para produtos cadastrados
Estoque_Produtos = []      # variável global para estoque
Clientes = []

def salvar_produtos(lista_produtos):
    lista_dicionarios = [p.to_dict() for p in lista_produtos]
    salvar_lista_em_json(lista_dicionarios, ARQUIVO_PRODUTOS)

def carregar_produtos():
    try:
        return [Produto.from_dict(d) for d in carregar_lista_de_json(ARQUIVO_PRODUTOS)]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_estoque(lista_estoque):
    lista_dicionarios = [e.to_dict() for e in lista_estoque]
    salvar_lista_em_json(lista_dicionarios, ARQUIVO_ESTOQUE)

def carregar_estoque():
    try:
        return [Produto.from_dict(d) for d in carregar_lista_de_json(ARQUIVO_ESTOQUE)]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def iniciar_programa():
    global Produtos_Cadastrados, Estoque_Produtos
    Produtos_Cadastrados = carregar_produtos()
    Estoque_Produtos = carregar_estoque()

def finalizar_programa():
    salvar_produtos(Produtos_Cadastrados)
    salvar_estoque(Estoque_Produtos)

# --- Classe Cliente ---

class Cliente:
    def __init__(self, _Nome, _Email):
        self._Nome = _Nome
        self._Email = _Email

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

    @classmethod
    def Cadastrar_Cliente(cls):
        while True:
            contador = 0
            Nome = input("\nNome completo do cliente: ").strip()
            for Item_Cliente in Clientes:
                if Item_Cliente.Nome == Nome:
                    contador += 1
            if contador > 0:
                print("\nO nome já está cadastrado!")
                continue
            break

        while True:
            Email = input("E-mail do cliente: ").strip()
            if '@' not in Email or '.' not in Email:
                print("\nE-mail inválido!")
                continue
            break
        
        Clientes.append(cls(Nome, Email))
        print("\nCliente cadastrado!")

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
                contador += 1
        else:
            print("\nNenhum cliente cadastrado!")
    
    @staticmethod
    def Excluir_Cliente():
        if Clientes:
            while True: 
                Nome = input("Digite o nome do cliente ou 'sair' para voltar: ").strip()
                if Nome.lower() == 'sair':
                    break
                for Item_Cliente in Clientes:
                    if Item_Cliente.Nome == Nome:
                        Clientes.remove(Item_Cliente)
                        print("\nCliente excluído!")
                        return
                print(f'''\nO nome "{Nome}" não foi encontrado!''')
        else:
            print("Nenhum cliente cadastrado para excluir!")

# --- Menus ---

def Menu_Clientes():
    while True:
        print('''\n---Opções de Clientes---
[1] - Cadastrar Cliente
[2] - Listar Clientes Cadastrados
[3] - Excluir Cliente
[4] - Voltar ao Menu Principal''')
        Opcao_Clientes = input("\nDigite a opção desejada: ").strip()
        if Opcao_Clientes not in ('1','2','3','4'):
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
    print("\nVoltando ao menu principal...")

def Menu_Produto():
    while True:
        print('''\n---Opções de Produto---
[1] - Cadastrar Produto
[2] - Listar Produtos Cadastrados
[3] - Excluir Cadastro de um Produto
[4] - Voltar ao Menu Principal''')
        Opcao_Produto = input("\nDigite a opção desejada: ").strip()
        if Opcao_Produto not in ('1','2','3','4'):
            print("\nResposta inválida!")
            continue
        match Opcao_Produto:
            case '1':
                Produto.Cadastrar_Produto(Produtos_Cadastrados)
            case '2':
                Produto.Listar_Produtos(Produtos_Cadastrados)
            case '3':
                Produto.Excluir_Cadastro_Produto(Produtos_Cadastrados)
            case '4':
                break
    print("\nVoltando ao menu principal...")

def Menu_Estoque():
    while True:
        print('''\n---Opções de Estoque---
[1] - Listar Produtos em Estoque
[2] - Reabastecer Estoque de um Produto
[3] - Retirar uma Quantidade de um Produto no Estoque
[4] - Voltar ao Menu Principal''')
        Opcao_Estoque = input("\nDigite a opção desejada: ").strip()
        if Opcao_Estoque not in ('1','2','3','4'):
            print("\nResposta inválida!")
            continue
        match Opcao_Estoque:
            case '1':
                Visualizar_Estoque(Estoque_Produtos, Produtos_Cadastrados)
            case '2':
                Reabastecer_Estoque(Estoque_Produtos)
            case '3':
                Retirar_Produto(Estoque_Produtos)
            case '4':
                break
    print("\nVoltando ao menu principal...")

def Menu_Principal():
    while True:
        print('''\n---Menu de opções---
[1] - Opções de Produto
[2] - Opções de Estoque
[3] - Opções de Clientes
[4] - Sair do programa''')
        Opcao_Menu = input("\nDigite a opção desejada: ").strip()
        if Opcao_Menu not in ('1','2','3','4'):
            print("\nResposta inválida!")
            continue
        match Opcao_Menu:
            case '1':
                Menu_Produto()
            case '2':
                Menu_Estoque()
            case '3':
                Menu_Clientes()
            case '4':
                print("\nSaindo do programa...")
                break

if __name__ == "__main__":
    iniciar_programa()
    Menu_Principal()
    finalizar_programa()
