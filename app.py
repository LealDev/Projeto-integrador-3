import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dados Sisu", page_icon=":📉:", layout="wide")

#Retira funções do Streamlit no canto superior direito
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


# Criando dados aleatórios para o exemplo
cidades = ['São Paulo', 'Rio de Janeiro',
           'Belo Horizonte', 'Curitiba', 'Fortaleza']
dados = {'Cidade': cidades,
         'População': np.random.randint(100000, 500000, size=len(cidades)),
         'PIB': np.random.randint(1000000000, 10000000000, size=5, dtype=np.int64),
         'IDH': np.round(np.random.uniform(0.5, 1, size=len(cidades)), 2)}

# Criar uma função para o menu HOME


def home():
    st.title("Panorama geral")
    st.write("Aqui está um resumo dos dados das cidades.")
    st.write('')

    # Dividindo a tela em duas colunas
    col1, col2 = st.columns(2)

    # Gráfico de barra com a população das cidades
    with col1:
        fig1, ax1 = plt.subplots()
        ax1.bar(dados['Cidade'], dados['População'])
        ax1.set_ylabel('População')
        ax1.set_xticklabels(dados['Cidade'], rotation=90)
        st.pyplot(fig1)

    # Gráfico de barra com o PIB das cidades
    with col2:
        fig2, ax2 = plt.subplots()
        ax2.bar(dados['Cidade'], dados['PIB'])
        ax2.set_ylabel('PIB')
        ax2.set_xticklabels(dados['Cidade'], rotation=90)
        st.pyplot(fig2)

    # Dividindo a tela em duas colunas
    col3, col4 = st.columns(2)

    # Gráfico de barra com o IDH das cidades
    with col3:
        fig3, ax3 = plt.subplots()
        ax3.bar(dados['Cidade'], dados['IDH'])
        ax3.set_ylabel('IDH')
        ax3.set_xticklabels(dados['Cidade'], rotation=90)
        st.pyplot(fig3)

    # Gráfico de barra com a média da população, PIB e IDH por região
    dados_regiao = pd.DataFrame({'Região': ['Sudeste', 'Sudeste', 'Sul', 'Nordeste', 'Sul'],
                                 'População': dados['População'],
                                 'PIB': dados['PIB'],
                                 'IDH': dados['IDH']})
    dados_regiao = dados_regiao.groupby('Região').mean().reset_index()

    with col4:
        fig4, ax4 = plt.subplots()
        ax4.bar(dados_regiao['Região'],
                dados_regiao['População'], label='População')
        ax4.bar(dados_regiao['Região'], dados_regiao['PIB'], label='PIB')
        ax4.bar(dados_regiao['Região'], dados_regiao['IDH'], label='IDH')
        ax4.set_ylabel('Média')
        ax4.legend()
        st.pyplot(fig4)

# Criar uma função para a página Regiões


def regioes():
    st.title("Dados por regiões")
    st.write("Aqui estão os dados agrupados por regiões.")
    st.write('')

    # Adicione o filtro de data
    data_inicio = st.date_input("Selecione a data de início")
    data_fim = st.date_input("Selecione a data de fim")

    # Crie o dataframe com dados das cidades/estados
    dados_cidades_estados = pd.DataFrame({
        'Cidade/Estado': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Fortaleza'],
        'População': [12325232, 6747815, 2521564, 2872347, 2686612]
    })

    # Ordene o dataframe pela população
    dados_cidades_estados = dados_cidades_estados.sort_values(
        by='População', ascending=False)

    # Crie o gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(dados_cidades_estados['Cidade/Estado'],
           dados_cidades_estados['População'])
    ax.set_ylabel('População')
    ax.set_xticklabels(dados_cidades_estados['Cidade/Estado'], rotation=90)

    # Exiba o gráfico no Streamlit
    st.pyplot(fig)


# Criar o menu de navegação do aplicativo
menu = ['Home', 'Regiões']
pagina = st.sidebar.selectbox("Selecione uma página:", menu)

# Exibir a página selecionada
if pagina == 'Home':
    home()
elif pagina == 'Regiões':
    regioes()

# Path: Sisu\app.py
