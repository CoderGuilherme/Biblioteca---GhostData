import pandas as pd 
from faker import Faker
from datetime import date
import random

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

# Função para gerar o dataset
def gerar_dataset(classe, num_registros):
    dados = []
    for _ in range(num_registros):
        obj = classe()  
        dados.append(obj.get_data()) 
    df = pd.DataFrame(dados)
    return df



