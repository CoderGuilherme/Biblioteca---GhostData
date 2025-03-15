import pandas as pd 
from faker import Faker
from datetime import date
import random
import json
import uuid

class SetEstabelecimento:
    domains = ['gmail.com', 'outlook.com', 'hotmail.com']

    def __init__(self):
        self.fake = Faker('pt-BR')
        self.id_estabelecimento = str(uuid.uuid4())[:8]  # Simula um ID único
        self.nome = f"{self.fake.company_suffix()} {self.fake.company()}"
        self.cnpj = self.gerar_cnpj()
        self.telefone = self.fake.phone_number()
        self.email = self.gerar_email()
        self.endereco = self.fake.street_address()
        self.bairro = self.fake.bairro()
        self.cidade = self.fake.city()
        self.estado = self.fake.state()
        self.cep = self.fake.postcode()
        self.id_oficial = self.gerar_id_unico()

    def gerar_id_unico(self):
        primeiros_digitos_nome = self.nome[:4] if len(self.nome) >= 4 else self.nome
        return primeiros_digitos_nome + self.id_estabelecimento
    def gerar_cnpj(self):
        """Gera um CNPJ aleatório no formato XX.XXX.XXX/0001-XX"""
        bloco1 = random.randint(10, 99)
        bloco2 = random.randint(100, 999)
        bloco3 = random.randint(100, 999)
        bloco4 = "0001"
        bloco5 = random.randint(10, 99)
        return f"{bloco1}.{bloco2}.{bloco3}/{bloco4}-{bloco5}"

    def gerar_email(self):
        """Gera um email baseado no nome do estabelecimento + domínio aleatório"""
        nome_formatado = self.nome.lower().replace(" ", "_").replace(",", "").replace(".", "")
        dominio = random.choice(self.domains)
        return f"{nome_formatado}@{dominio}"

    def get_data(self):
        return {
            "ID_Estabelecimento": self.id_oficial,
            "Nome": self.nome,
            "CNPJ": self.cnpj,
            "Telefone": self.telefone,
            "Email": self.email,
            "Endereço": self.endereco,
            "Bairro": self.bairro,
            "Cidade": self.cidade,
            "Estado": self.estado,
            "CEP": self.cep
        }


class SetProduto:
    def __init__(self):
        self.produtos_disponiveis = self.carregar_produtos_do_json("Data\produtos.json")  # Carrega os produtos do arquivo JSON
        self.categoria, self.nome, self.id_produto, self.preco = self.gerar_produto()

    def carregar_produtos_do_json(self, nome_arquivo):
        """Carrega os dados dos produtos a partir de um arquivo JSON."""
        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo: # Adicionado encoding utf-8
                return json.load(arquivo)
        except FileNotFoundError:
            print(f"Erro: arquivo '{nome_arquivo}' não encontrado.")
            return {}
        except json.JSONDecodeError:
            print(f"Erro: arquivo '{nome_arquivo}' inválido. Verifique o formato JSON.")
            return {}

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


class SetVenda:
    def __init__(self):
        self.produto = SetProduto
        self.estabelecimento = SetEstabelecimento
        self.id_venda = str(uuid.uuid4())[:8]
        self.id_produto = self.produto.id_produto
        self.id_estabelecimento = self.estabelecimento.id_estabelecimento
        self.nome_produto = self.produto.nome
        self.quantidade = random.randint(1, 10)
        self.total = round(self.quantidade * self.produto.preco, 2)

    def get_data(self):
        return {
            "id_venda": self.id_venda,
            "id_produto": self.id_produto,
            "id_estabelecimento": self.id_estabelecimento,
            "nome_produto": self.nome_produto,
            "quantidade": self.quantidade,
            "total": self.total
        }


# Função para gerar o dataset
def gerar_dataset(classe, num_registros):
    dados = []
    for _ in range(num_registros):
        obj = classe()  
        dados.append(obj.get_data()) 
    df = pd.DataFrame(dados)
    return df


venda = SetVenda()

print(venda.get_data())
