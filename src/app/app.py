import os
import sys

import humanize
import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from GhostData.GhostData import *



def compactar(numero):
    # Usa o humanize para converter o número em formato legível
    numero_formatado = humanize.intword(numero)
    
    # Substitui os termos para o português
    numero_formatado = numero_formatado.replace("thousand", "mil")
    numero_formatado = numero_formatado.replace("million", "Mi")
    numero_formatado = numero_formatado.replace("billion", "Bi")
    numero_formatado = numero_formatado.replace("trillion", "Tri")

    return numero_formatado

st.header("👻📊 GhostData Datasets Aleatórios", divider="violet")



def load_data(data,num):
    df = gerar_dataset(data,num)
    return df

st.sidebar.header("⚙️ Configurações", divider="violet")

# 📌 Seção: Definição do Número de Registros
st.sidebar.subheader("📊 Definição de Registros", divider="blue")
num = st.sidebar.number_input("Quantidade de registros:", step=1, min_value=1, max_value=500000)
st.sidebar.write(f"📌 Sua base terá **{compactar(num)}** registros.")

# 📌 Seção: Escolha do Tema do Dataset
st.sidebar.subheader("📌 Escolha um Tema", divider="green")
option_map = {
    0: "👤 Pessoas",
    1: "💼 Funcionários",
    2: "📦 Produtos",
    3: "🏬 Lojas",
    4: "🛒 Vendas",
}

selection = st.sidebar.pills(
    "Escolha um tema",
    options=option_map.keys(),
    format_func=lambda option: option_map[option],
    selection_mode="single"
)

# 🔄 Mapeamento de escolha e título correspondente
match selection:
    case 0:
        escolha = SetPessoa
        titulo = "👤 **Tabela de Pessoas**"
    case 1:
        escolha = SetFuncionario
        titulo = "💼 **Tabela de Funcionários**"
    case 2:
        escolha = SetProduto
        titulo = "📦 **Tabela de Produtos**"
    case 3:
        escolha = SetEstabelecimento
        titulo = "🏬 **Tabela de Lojas**"
    case 4:
        escolha = "vendas"
        titulo = "🛒 **Tabelas de Vendas**"
    case _:
        escolha = None
        titulo = "⚠️ **Nenhuma opção selecionada**"

# 📌 Seção: Botão de Geração de Dados
st.sidebar.subheader("🚀 Geração de Dados", divider="red")
botao = st.sidebar.button("Gerar Dataset", type="primary")

# 📦 Processamento e Exibição dos Dados
if botao:
    if escolha:
        with st.spinner("⏳ Gerando dados..."):
            titulo_completo = f"{titulo} **com** {compactar(num)} **Registros**"
            
            if escolha == "vendas":  
                df_produtos, df_estabelecimentos, df_vendas = gerar_vendas(num) 
                
                st.subheader(titulo_completo, divider="grey")

                st.subheader("📦 Produtos", divider="grey")
                st.dataframe(df_produtos, use_container_width=True)

                st.subheader("🏬 Estabelecimentos", divider="grey")
                st.dataframe(df_estabelecimentos, use_container_width=True)

                st.subheader("🛒 Vendas", divider="grey")
                st.dataframe(df_vendas, use_container_width=True)

            else:
                df = gerar_dataset(escolha, num)

                if df is not None and not df.empty:
                    st.subheader(titulo_completo, divider="grey")
                    st.dataframe(df, use_container_width=True)
                else:
                    st.warning("🚨 Nenhum dado encontrado para essa escolha.", icon="⚠️")
    else:
        st.warning("⚠️ Tema não selecionado ou não cadastrado.", icon="⚠️")