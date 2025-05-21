import json
import os

ARQUIVO = "estoque.json"

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_dados(estoque):
    with open(ARQUIVO, "w") as f:
        json.dump(estoque, f, indent=4)
