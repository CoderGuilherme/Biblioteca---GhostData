# GhostData

**GhostData** é uma biblioteca Python projetada para gerar datasets aleatórios de forma rápida e eficiente. Ideal para testes, prototipação e validação de modelos, o **GhostData** cria dados sintéticos realistas que podem simular diferentes cenários e estruturas de informações.

## Evolução do Projeto

### Início do Desenvolvimento

**Data:** 10 de Março de 2025

Hoje, dei início ao desenvolvimento da primeira classe e função do projeto **GhostData**. O objetivo foi criar uma base sólida para testar a ideia e a funcionalidade da biblioteca.

### Implementação Inicial

- **Classe `Pessoa`:** A primeira classe desenvolvida é a `Pessoa`. Ela é responsável por gerar dados aleatórios sobre uma pessoa, como nome, idade, endereço e email. A classe utiliza a biblioteca `Faker` para gerar dados realistas.
- **Função `gerar_dataset`:** Para validar a funcionalidade da classe, foi criada uma função chamada `gerar_dataset`. Ela é responsável por gerar um conjunto de dados (dataset) a partir de um número definido de registros. A função é reutilizável e pode ser aplicada a outras classes no futuro.

### Próximos Passos

A partir de hoje, a ideia é expandir o projeto, criando novas classes para gerar diferentes tipos de dados, como produtos, transações, ou até mesmo dados financeiros. A função `gerar_dataset` será mantida como um elemento central, pois pode ser aplicada a qualquer classe que gere dados aleatórios.

## Funcionalidade Atual

- **Classe `Pessoa`:** Gera dados de pessoas aleatórias, incluindo nome, idade, endereço e email.
- **Função `gerar_dataset`:** Cria um dataset de dados aleatórios com base na função de geração de dados fornecida (por exemplo, a classe `Pessoa`).

### Exemplo de Uso

```python
from GhostData import SetPessoa
from GhostData import gerar_dataset

# Criando o objeto Pessoa
pessoa = SetPessoa()

# Gerando um dataset com 10 registros
dataset_pessoas = gerar_dataset(pessoa.gerar_dados, 10)

# Exibindo o dataset
print(dataset_pessoas)
```
# Exemplo de Saída do Dataset

| **Nome** | **Sobrenome** | **Telefone**    | **Estado**      | **Cidade**      | **Data de Nascimento** | **Idade** | **Email**                      |
|----------|---------------|-----------------|-----------------|-----------------|------------------------|-----------|--------------------------------|
| João     | Silva         | (11) 98765-4321 | São Paulo      | São Paulo       | 01/01/1990             | 35        | joao.silva@gmail.com           |
| Maria    | Oliveira      | (21) 12345-6789 | Rio de Janeiro | Rio de Janeiro  | 15/05/1985             | 39        | maria.oliveira@hotmail.com     |
| Pedro    | Santos        | (31) 23456-7890 | Minas Gerais   | Belo Horizonte  | 20/10/1995             | 29        | pedro.santos@gmail.com         |
| Ana      | Costa         | (41) 87654-3210 | Paraná         | Curitiba        | 10/12/2000             | 24        | ana.costa@outlook.com          |
| Carlos   | Pereira       | (61) 34567-8901 | Brasília       | Brasília        | 05/03/1992             | 33        | carlos.pereira@gmail.com       |
