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
    produtos = {"Eletrônicos": {
        "Smartphone": {"preco": 1200, "id": "eletr-001"},
        "Notebook": {"preco": 2500, "id": "eletr-002"},
        "Tablet": {"preco": 800, "id": "eletr-003"},
        "Fone de Ouvido": {"preco": 150, "id": "eletr-004"},
        "Smartwatch": {"preco": 600, "id": "eletr-005"},
        "Câmera Digital": {"preco": 900, "id": "eletr-006"},
        "Impressora": {"preco": 400, "id": "eletr-007"},
        "Monitor": {"preco": 500, "id": "eletr-008"},
        "Televisão": {"preco": 1800, "id": "eletr-009"},
        "Console de Videogame": {"preco": 1500, "id": "eletr-010"},
        "Caixa de Som Bluetooth": {"preco": 200, "id": "eletr-011"},
        "Roteador Wi-Fi": {"preco": 100, "id": "eletr-012"},
        "Pen Drive": {"preco": 50, "id": "eletr-013"},
        "HD Externo": {"preco": 300, "id": "eletr-014"},
        "Carregador Portátil": {"preco": 80, "id": "eletr-015"}
    },
    "Alimentos": {
        "Arroz": {"preco": 15, "id": "alim-001"},
        "Feijão": {"preco": 12, "id": "alim-002"},
        "Macarrão": {"preco": 8, "id": "alim-003"},
        "Chocolate": {"preco": 10, "id": "alim-004"},
        "Café": {"preco": 20, "id": "alim-005"},
        "Açúcar": {"preco": 7, "id": "alim-006"},
        "Sal": {"preco": 5, "id": "alim-007"},
        "Óleo": {"preco": 18, "id": "alim-008"},
        "Leite": {"preco": 6, "id": "alim-009"},
        "Ovos": {"preco": 12, "id": "alim-010"},
        "Pão": {"preco": 4, "id": "alim-011"},
        "Queijo": {"preco": 25, "id": "alim-012"},
        "Frango": {"preco": 22, "id": "alim-013"},
        "Carne Bovina": {"preco": 30, "id": "alim-014"},
        "Peixe": {"preco": 28, "id": "alim-015"},
        "Frutas": {"preco": 15, "id": "alim-016"},
        "Legumes": {"preco": 18, "id": "alim-017"},
        "Verduras": {"preco": 10, "id": "alim-018"},
        "Iogurte": {"preco": 8, "id": "alim-019"},
        "Cereal": {"preco": 12, "id": "alim-020"},
        "Biscoitos": {"preco": 7, "id": "alim-021"},
        "Sucos": {"preco": 10, "id": "alim-022"},
        "Refrigerantes": {"preco": 9, "id": "alim-023"},
        "Cerveja": {"preco": 6, "id": "alim-024"},
        "Vinho": {"preco": 35, "id": "alim-025"}
    },
    "Roupas": {
        "Camiseta": {"preco": 30, "id": "roup-001"},
        "Calça": {"preco": 80, "id": "roup-002"},
        "Jaqueta": {"preco": 150, "id": "roup-003"},
        "Tênis": {"preco": 120, "id": "roup-004"},
        "Meias": {"preco": 10, "id": "roup-005"},
        "Cuecas": {"preco": 15, "id": "roup-006"},
        "Sutiã": {"preco": 25, "id": "roup-007"},
        "Vestido": {"preco": 90, "id": "roup-008"},
        "Saia": {"preco": 60, "id": "roup-009"},
        "Blusa": {"preco": 45, "id": "roup-010"},
        "Casaco": {"preco": 180, "id": "roup-011"},
        "Suéter": {"preco": 100, "id": "roup-012"},
        "Calçado Social": {"preco": 150, "id": "roup-013"},
        "Roupa de Banho": {"preco": 70, "id": "roup-014"},
        "Roupa Íntima": {"preco": 35, "id": "roup-015"},
        "Pijama": {"preco": 50, "id": "roup-016"},
        "Roupa Esportiva": {"preco": 110, "id": "roup-017"},
        "Acessórios": {"preco": 20, "id": "roup-018"},
        "Cinto": {"preco": 40, "id": "roup-019"},
        "Boné": {"preco": 25, "id": "roup-020"},
        "Chapéu": {"preco": 30, "id": "roup-021"},
        "Luvas": {"preco": 18, "id": "roup-022"},
        "Cachecol": {"preco": 35, "id": "roup-023"}
    },
    "Livros": {
        "Romance": {"preco": 30, "id": "livr-001"},
        "Ficção Científica": {"preco": 35, "id": "livr-002"},
        "Fantasia": {"preco": 40, "id": "livr-003"},
        "Suspense": {"preco": 28, "id": "livr-004"},
        "Terror": {"preco": 32, "id": "livr-005"},
        "Biografia": {"preco": 45, "id": "livr-006"},
        "Autoajuda": {"preco": 25, "id": "livr-007"},
        "Infantil": {"preco": 20, "id": "livr-008"},
        "Didático": {"preco": 50, "id": "livr-009"},
        "História": {"preco": 38, "id": "livr-010"},
        "Poesia": {"preco": 22, "id": "livr-011"},
        "Mangá": {"preco": 15, "id": "livr-012"},
        "Quadrinhos": {"preco": 18, "id": "livr-013"},
        "Livro de Receitas": {"preco": 30, "id": "livr-014"},
        "Livro de Arte": {"preco": 55, "id": "livr-015"}
    },
    "Móveis": {
        "Sofá": {"preco": 1200, "id": "move-001"},
        "Cama": {"preco": 800, "id": "move-002"},
        "Mesa": {"preco": 400, "id": "move-003"},
        "Cadeira": {"preco": 150, "id": "move-004"},
        "Guarda-Roupa": {"preco": 900, "id": "move-005"},
        "Estante": {"preco": 300, "id": "move-006"},
        "Criado-Mudo": {"preco": 100, "id": "move-007"},
        "Cômoda": {"preco": 450, "id": "move-008"},
        "Rack": {"preco": 350, "id": "move-009"},
        "Painel de TV": {"preco": 500, "id": "move-010"},
        "Armário de Cozinha": {"preco": 700, "id": "move-011"},
        "Poltrona": {"preco": 250, "id": "move-012"},
        "Mesa de Centro": {"preco": 200, "id": "move-013"},
        "Escrivaninha": {"preco": 380, "id": "move-014"},
        "Cadeira de Escritório": {"preco": 320, "id": "move-015"}
    },
    "Ferramentas": {
        "Chave de Fenda": {"preco": 20, "id": "ferr-001"},
        "Martelo": {"preco": 30, "id": "ferr-002"},
        "Alicate": {"preco": 25, "id": "ferr-003"},
        "Furadeira": {"preco": 180, "id": "ferr-004"},
        "Parafusadeira": {"preco": 150, "id": "ferr-005"},
        "Serra": {"preco": 120, "id": "ferr-006"},
        "Trena": {"preco": 15, "id": "ferr-007"},
        "Nível": {"preco": 40, "id": "ferr-008"},
        "Chave Inglesa": {"preco": 50, "id": "ferr-009"},
        "Jogo de Chaves": {"preco": 80, "id": "ferr-010"},
        "Lanterna": {"preco": 35, "id": "ferr-011"},
        "Fita Isolante": {"preco": 10, "id": "ferr-012"},
        "Cola": {"preco": 8, "id": "ferr-013"},
        "Lixa": {"preco": 5, "id": "ferr-014"},
        "Óculos de Proteção": {"preco": 22, "id": "ferr-015"}
    },
    "Brinquedos": {
        "Boneca": {"preco": 50, "id": "brin-001"},
        "Carrinho": {"preco": 40, "id": "brin-002"},
        "Quebra-Cabeça": {"preco": 30, "id": "brin-003"},
        "Jogo de Tabuleiro": {"preco": 60, "id": "brin-004"},
        "Videogame": {"preco": 1500, "id": "brin-005"},
        "Bola": {"preco": 25, "id": "brin-006"},
        "Bicicleta": {"preco": 300, "id": "brin-007"},
        "Patinete": {"preco": 120, "id": "brin-008"},
        "Pelúcia": {"preco": 35, "id": "brin-009"},
        "Lego": {"preco": 80, "id": "brin-010"},
        "Massinha": {"preco": 18, "id": "brin-011"},
        "Dominó": {"preco": 22, "id": "brin-012"},
        "Cartas": {"preco": 12, "id": "brin-013"},
        "Jogo de Construção": {"preco": 70, "id": "brin-014"},
        "Instrumento Musical": {"preco": 200, "id": "brin-015"}
    },
    "Esportes": {
        "Bola de Futebol": {"preco": 40, "id": "espt-001"},
        "Bola de Basquete": {"preco": 45, "id": "espt-002"},
        "Bola de Vôlei": {"preco": 38, "id": "espt-003"},
        "Raquete de Tênis": {"preco": 150, "id": "espt-004"},
        "Rede de Vôlei": {"preco": 100, "id": "espt-005"},
        "Corda de Pular": {"preco": 15, "id": "espt-006"},
        "Halteres": {"preco": 80, "id": "espt-007"},
        "Esteira": {"preco": 1800, "id": "espt-008"},
        "Bicicleta Ergométrica": {"preco": 1200, "id": "espt-009"},
        "Roupa de Natação": {"preco": 60, "id": "espt-010"},
        "Óculos de Natação": {"preco": 30, "id": "espt-011"},
        "Prancha de Surf": {"preco": 400, "id": "espt-012"},
        "Skate": {"preco": 250, "id": "espt-013"},
        "Patins": {"preco": 180, "id": "espt-014"},
        "Equipamento de Camping": {"preco": 350, "id": "espt-015"}
    }
}

    def __init__(self):
        self.produtos_disponiveis = SetProduto.produtos  # Usa o atributo estático
        self.categoria, self.nome, self.id_produto, self.preco = self.gerar_produto()

    def gerar_produto(self):
        if not self.produtos_disponiveis:
            return None, None, None, None

        categoria = random.choice(list(self.produtos_disponiveis.keys()))
        nome = random.choice(list(self.produtos_disponiveis[categoria].keys()))
        id_produto = self.produtos_disponiveis[categoria][nome]["id"]
        preco = float(self.produtos_disponiveis[categoria][nome].get("preco", 0))
        return categoria, nome, id_produto, preco

    def get_data(self):
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
