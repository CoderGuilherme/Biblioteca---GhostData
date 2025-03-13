import streamlit as st
import pandas as pd
from GhostData import SetPessoa
from GhostData import gerar_dataset
import humanize
import time

def compactar(numero):
    # Usa o humanize para converter o número em formato legível
    numero_formatado = humanize.intword(numero)
    
    # Substitui os termos para o português
    numero_formatado = numero_formatado.replace("thousand", "mil")
    numero_formatado = numero_formatado.replace("million", "Mi")
    numero_formatado = numero_formatado.replace("billion", "Bi")
    numero_formatado = numero_formatado.replace("trillion", "Tri")

    return numero_formatado

st.header("GhostData", divider="violet") 



def load_data(data,num):
    df = gerar_dataset(data,num)
    return df

st.sidebar.header("Configurações",divider="violet")

num = st.sidebar.number_input("Defina a quantidade de registros da sua base",step=1,max_value=500000)
st.sidebar.write("Sua base terá ",compactar(num), "registros")

option_map = {
    0:"Pessoas",
    1:"Funcionarios",
    2:"Produtos"
}


st.sidebar.subheader("Temas Dataset")
selection = st.sidebar.pills(
    "Escolha um tema",
    options=option_map.keys(),
    format_func=lambda option: option_map[option],
    selection_mode="single"
)


match selection:
    case 0:
        escolha = SetPessoa
    case _:
        escolha = None

botao = st.sidebar.button("Criar", type="secondary")

if botao:
    if escolha: 
        with st.spinner("Gerando...", show_time=True):
            df = gerar_dataset(escolha,num)

        if df is not None and not df.empty:  # Verifica se o dataframe não está vazio
            st.subheader(f"Tabela de {option_map[selection]} com {compactar(num)} Registros",divider="grey")
            st.dataframe(df, use_container_width=True)
        else:
            st.warning("Nenhum dado encontrado para essa escolha.", icon="⚠️")
    else:
        st.warning("Tema não selecionado ou não cadastrado.", icon="⚠️")
