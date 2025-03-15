import pandas as pd 
from faker import Faker
from datetime import date
import random
import json
import uuid
import os


# Classe SetPessoa que contém os dados comuns a todas as pessoas
class SetPessoa:
    def __init__(self):
        self.fake = Faker('pt-BR')
        self.name = self.fake.first_name()  # Nome próprio
        self.last_name = self.fake.last_name()  # Sobrenome
        self.phone_number = self.fake.phone_number()  # Número de telefone
        self.state = self.fake.state()  # Estado
        self.city = self.fake.city()  # Cidade 
        self.birth = self.fake.date_of_birth(minimum_age=18, maximum_age=80)
        self.age = self.calculate_age()
        domains = ['gmail.com', 'outlook.com', 'hotmail.com']
        self.email = (f"{self.name.lower()}.{self.last_name.lower()}@{random.choice(domains)}").replace(" ","-")

    # Método para calcular a idade
    def calculate_age(self):
        today = date.today()
        return today.year - self.birth.year - ((today.month, today.day) < (self.birth.month, self.birth.day))

    # Método que retorna todos os dados
    def get_data(self):
        data = {
            "name": self.name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "state": self.state,
            "city": self.city,
            "birth": self.birth.strftime('%d/%m/%Y'),
            "age": self.age,
            "email": self.email
        }
        return data


class SetFuncionario(SetPessoa):
    departamentos = {
    "TI": {
        "Desenvolvedor": ["Estagiário", "Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Analista de Dados": ["Estagiário", "Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Engenheiro de Software": ["Estagiário", "Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Administrador de Sistemas": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Arquiteto de Soluções": ["Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Cientista de Dados": ["Estagiário", "Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Suporte Técnico": ["Estagiário", "Júnior", "Pleno", "Sênior", "Coordenador", "Gerente"],
        "Especialista em Segurança da Informação": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Gerente de Projetos de TI": ["Gerente", "Diretor"],
        "Analista de Qualidade de Software": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente"],
        "Especialista em Cloud Computing": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Engenheiro de DevOps": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Analista de Redes": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Especialista em Inteligência Artificial": ["Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Especialista em Machine Learning": ["Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Especialista em UX/UI": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"]
    },
    "Financeiro": {
        "Contador": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Analista Financeiro": ["Estagiário", "Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Gestor Financeiro": ["Gerente", "Diretor"],
        "Tesoureiro": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Controller": ["Gerente", "Diretor"],
        "Especialista em Investimentos": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Auditor Interno": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Analista de Crédito": ["Estagiário", "Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Analista de Custos": ["Estagiário", "Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Gerente de Controladoria": ["Gerente", "Diretor"],
        "Especialista em Planejamento Financeiro": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Analista de Impostos": ["Estagiário", "Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"]
    },
    "RH": {
        "Analista de RH": ["Estagiário", "Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Gestor de Pessoas": ["Gerente", "Diretor"],
        "Recrutador": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Business Partner": ["Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Consultor de RH": ["Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Especialista em Benefícios": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Analista de Treinamento e Desenvolvimento": ["Estagiário", "Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Gerente de Recursos Humanos": ["Gerente", "Diretor"],
        "Especialista em Remuneração": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Analista de Departamento Pessoal": ["Estagiário", "Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Especialista em Diversidade e Inclusão": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Especialista em Comunicação Interna": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"]
    },
    "Marketing": {
        "Analista de Marketing": ["Estagiário", "Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Gestor de Mídias": ["Gerente", "Diretor"],
        "Diretor de Marketing": ["Diretor"],
        "Especialista em SEO": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Redator Publicitário": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Designer Gráfico": ["Estagiário", "Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Social Media Manager": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Analista de Marketing Digital": ["Estagiário", "Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Especialista em Marketing de Conteúdo": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Gerente de Produto": ["Gerente", "Diretor"],
        "Analista de Inteligência de Mercado": ["Estagiário", "Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Especialista em E-mail Marketing": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Especialista em Branding": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Especialista em Inbound Marketing": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"]
    },
    "Vendas": {
        "Representante Comercial": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Executivo de Vendas": ["Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Gerente de Contas": ["Gerente", "Diretor"],
        "Analista de CRM": ["Estagiário", "Júnior", "Pleno", "Sênior", "Coordenador", "Gerente", "Diretor"],
        "Coordenador de Vendas": ["Coordenador", "Gerente", "Diretor"],
        "Diretor Comercial": ["Diretor"],
        "Especialista em Vendas Internacionais": ["Júnior", "Pleno", "Sênior"]}
    }



    faixa_salarial = {
            'Estagiário': (1000, 2000),
            'Júnior': (2000, 4000),
            'Pleno': (4000, 8000),
            'Sênior': (8000, 15000),
            'Coordenador': (10000, 18000),
            'Gerente': (15000, 25000),
            'Diretor': (25000, 50000)
        }
    
    def __init__(self):
        super().__init__()
        self.departamento, self.cargo = self.gerar_departamento_e_cargo()
        self.nivel = self.gerar_nivel()
        self.salario = self.gerar_salario()
        self.data_contratacao = self.fake.date_this_decade()

    def gerar_departamento_e_cargo(self):
        departamento = random.choice(list(self.departamentos.keys()))
        cargo = random.choice(list(self.departamentos[departamento].keys()))
        return departamento, cargo

    def gerar_nivel(self):
        niveis_possiveis = self.departamentos[self.departamento][self.cargo]
        return random.choice(niveis_possiveis)

    def gerar_salario(self):
        faixa = self.faixa_salarial.get(self.nivel)
        if faixa:
            return random.randint(faixa[0], faixa[1])
        return 2000  # Valor padrão caso não encontre

    def get_data(self):
        return {
            "name": self.name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "state": self.state,
            "city": self.city,
            "birth": self.birth.strftime('%d/%m/%Y'),
            "age": self.age,
            "email": self.email,
            "departamento": self.departamento,
            "cargo": self.cargo,
            "nivel": self.nivel,
            "salario": self.salario,
            "data_contratacao": self.data_contratacao.strftime('%d/%m/%Y')
        }
        
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
            # Obtém o caminho absoluto do diretório onde está GhostData.py
            base_dir = os.path.dirname(os.path.abspath(__file__))
            json_path = os.path.join(base_dir, "..", "Data", "produtos.json")

            self.produtos_disponiveis = self.carregar_produtos_do_json(json_path)
            self.categoria, self.nome, self.id_produto, self.preco = self.gerar_produto()

    def carregar_produtos_do_json(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            print(f"Erro: arquivo '{nome_arquivo}' não encontrado.")
            return {}
        except json.JSONDecodeError:
            print(f"Erro: arquivo '{nome_arquivo}' inválido. Verifique o formato JSON.")
            return {}

    def gerar_produto(self):
        if not self.produtos_disponiveis:
            return None, None, None, None

        categoria = random.choice(list(self.produtos_disponiveis.keys()))
        nome = random.choice(list(self.produtos_disponiveis[categoria].keys()))
        id_produto = self.produtos_disponiveis[categoria][nome]["id"]
        preco = float(self.produtos_disponiveis[categoria][nome].get("preco", 0))
        return categoria, nome, id_produto, preco

    def get_data(self):
        """Retorna os dados do produto em um dicionário."""
        if self.categoria is None:
            return {"erro": "Produtos não disponíveis"}
        return {
            "id_produto": self.id_produto,
            "categoria": self.categoria,
            "nome": self.nome,
            "preco": self.preco
        }

# Função para gerar vendas
def gerar_vendas(numero_de_registros):
    produtos = []
    estabelecimentos = []
    vendas = []

    for _ in range(numero_de_registros):
        # Criar Produto e Estabelecimento
        produto = SetProduto()
        estabelecimento = SetEstabelecimento()

        # Armazenar nos DataFrames
        produtos.append(produto.get_data())
        estabelecimentos.append(estabelecimento.get_data())

        # Criar Venda
        id_venda = str(uuid.uuid4())[:8]
        quantidade = random.randint(1, 10)
        total = round(quantidade * produto.preco, 2)

        vendas.append({
            "id_venda": id_venda,
            "id_produto": produto.id_produto,
            "id_estabelecimento": estabelecimento.id_oficial,
            "nome_produto": produto.nome,
            "quantidade": quantidade,
            "total": total
        })

    # Criar DataFrames
    df_produtos = pd.DataFrame(produtos)
    df_estabelecimentos = pd.DataFrame(estabelecimentos)
    df_vendas = pd.DataFrame(vendas)

    return df_produtos, df_estabelecimentos, df_vendas
# Função para gerar o dataset
def gerar_dataset(classe, num_registros):
    dados = []
    for _ in range(num_registros):
        obj = classe()  
        dados.append(obj.get_data()) 
    df = pd.DataFrame(dados)
    return df
