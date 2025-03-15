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



### Semana 2 - 15/03/2025

A GhostData foi atualizada com novas funcionalidades e uma interface gráfica intuitiva para facilitar a geração de dados sintéticos.

## O Que Há de Novo?

### Interface Streamlit

Agora, a GhostData possui uma interface gráfica construída com Streamlit, que permite:

* **Seleção de Tema:** Escolha o tema do conjunto de dados que deseja gerar.
* **Definição de Quantidade:** Determine o número de registros a serem gerados.
* **Visualização Instantânea:** Visualize a tabela gerada diretamente na interface.
* **Exportação Facilitada:** Exporte os dados gerados de forma rápida e prática.

### Novas Funcionalidades

Quatro novas funções foram adicionadas para expandir as capacidades da biblioteca:

* **`SetProduto`:** Gera um conjunto de dados com informações de produtos.
* **`SetEstabelecimento`:** Cria um conjunto de dados com detalhes de estabelecimentos comerciais.
* **`SetFuncionarios`:** Produz um conjunto de dados com informações de funcionários.
* **`gerar_vendas`:** Gera um conjunto de dados de vendas, utilizando os dados gerados por `SetProduto` e `SetEstabelecimento`.


## Exemplo de Uso na importação

Aqui está um exemplo simples de como usar as novas funcionalidades:

```python
from ghostdata import SetProduto, SetEstabelecimento, SetFuncionarios, gerar_vendas

produtos = SetProduto(num_rows=100)
estabelecimentos = SetEstabelecimento(num_rows=50)
funcionarios = SetFuncionarios(num_rows=200)
vendas = gerar_vendas(produtos, estabelecimentos, num_rows=1000)

print(vendas.head())
