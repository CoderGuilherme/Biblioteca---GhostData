import pandas as pd 
from faker import Faker
from datetime import date
import random
import json
import uuid
import os


def carregar_produtos_do_json(caminho_relativo):
    try:
        # Constrói o caminho absoluto correto
        caminho_absoluto = os.path.join(os.path.dirname(os.path.abspath(__file__)), caminho_relativo)

        with open(caminho_absoluto, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_relativo}' não encontrado.")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro: Falha ao decodificar JSON do arquivo '{caminho_relativo}': {e}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao carregar {caminho_relativo}: {e}")
        return None

class SetProduto:
    def __init__(self):
        self.produtos_disponiveis = self.carregar_produtos_do_json("..\Data\produtos.json")  # Carrega os produtos do arquivo JSON
        self.categoria, self.nome, self.id_produto, self.preco = self.gerar_produto()

    def carregar_produtos_do_json(self, caminho_relativo):
        try:
            # Constrói o caminho absoluto correto
            caminho_absoluto = os.path.join(os.path.dirname(os.path.abspath(__file__)), caminho_relativo)

            with open(caminho_absoluto, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
            return dados
        except FileNotFoundError:
            print(f"Erro: Arquivo '{caminho_relativo}' não encontrado.")
            return None
        except json.JSONDecodeError:
            print(f"Erro: Falha ao decodificar JSON do arquivo '{caminho_relativo}'.")
            return None
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            return None

    def gerar_produto(self):
        categoria = random.choice(list(self.produtos_disponiveis.keys()))
        nome = random.choice(list(self.produtos_disponiveis[categoria].keys()))
        id_produto = self.produtos_disponiveis[categoria][nome]["id"]
        preco = float(self.produtos_disponiveis[categoria][nome].get("preco", 0))  # Garante que seja float
        return categoria, nome, id_produto, preco

    def get_data(self):
        """Retorna os dados do produto em um dicionário."""
        if self.categoria is None: # adicionado validação de produtos indisponiveis
            return {"erro": "Produtos não disponíveis"}
        return {
            "id_produto": self.id_produto,
            "categoria": self.categoria,
            "nome": self.nome,
            "preco": self.preco
        }

produto = SetProduto()

print(produto.get_data())