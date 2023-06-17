import streamlit as st
from streamlit_autorefresh import st_autorefresh
import psycopg2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dados Sisu", page_icon=":📉:", layout="wide")

# Database connection parameters
db_params = {
    "host": "postgres",
    "port": 5432,
    "user": "postgres",
    "password": "example",
    "database": "prouni"
}

# Retira funções do Streamlit no canto superior direito
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Criar uma função para o menu HOME

def trata_resposta(resultado):
    indice = []
    dados = []
    for row in resultado:
        indice.append(row[0])
        dados.append(row[1])
    return indice, dados

def home():

    querys = []
    caminhos = [
        '/var/streamlit/scripts/modalidade_de_ensino.sql', 
        '/var/streamlit/scripts/indice_pcd.sql', 
        '/var/streamlit/scripts/indice_racial.sql', 
        '/var/streamlit/scripts/indice_sexo.sql', 
        '/var/streamlit/scripts/tipo_de_bolsa.sql', 
        '/var/streamlit/scripts/turno_bolsa.sql']
    nome_query = ['modalidade', 
                  'pcd', 
                  'raca', 
                  'sexo', 
                  'tipo_bolsa', 
                  'turno_bolsa']
    query_result = []
    for path in caminhos:
        find_file = open(path, 'r')
        querys.append(find_file.read())
        find_file.close()

    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        for query in querys:
            cur.execute(query)
            # Fetch data from the database
            query_result.append(cur.fetchall())
        
        # Close the database connection
        cur.close()
        conn.close()
    except:
        st.write("aguarde")

    resultado = dict(zip(nome_query, query_result))



    # Display the fetched data in Streamlit
    st.title("Panorama geral")
    st.write("Aqui está um resumo dos dados das bolsas ofertadas.")
    st.write('')

    # Dividindo a tela em duas colunas
    graph_tipo_bolsa, graph_modalidade = st.columns(2)
    
    
    # Gráfico de barra com tipo de bolsa
    tipo_bolsa, quant_tipo_bolsa = trata_resposta(resultado['tipo_bolsa'])
    with graph_tipo_bolsa:
        fig1, ax1 = plt.subplots()
        graph1 = ax1.bar(tipo_bolsa, quant_tipo_bolsa)
        ax1.set_ylabel('Total de bolsas')
        ax1.set_xticklabels(tipo_bolsa, rotation=45)
        ax1.set_title("Tipo de bolsa ofertada")
        ax1.bar_label(graph1)
        st.pyplot(fig1)

    # Gráfico de barra com modalidade de ensino
    modalidade, quant_modalidade = trata_resposta(resultado['modalidade'])
    with graph_modalidade:
        fig2, ax2 = plt.subplots()
        graph2 = ax2.bar(modalidade, quant_modalidade)
        ax2.set_ylabel('Total de bolsas')
        ax2.set_xticklabels(modalidade, rotation=45)
        ax2.set_title("Modalidade de bolsa ofertada")
        ax2.bar_label(graph2)
        st.pyplot(fig2)

    # Dividindo a tela em duas colunas
    graph_raca, graph_sexo = st.columns(2)

    # Gráfico de barra com raça dos beneficiários
    raca, quant_raca = trata_resposta(resultado['raca'])
    with graph_raca:
        fig3, ax3 = plt.subplots()
        graph3 = ax3.bar(raca, quant_raca)
        ax3.set_ylabel('Total de bolsas')
        ax3.set_xticklabels(raca, rotation=45)
        ax3.set_title("Distribuição racial dos baneficiados")
        ax3.bar_label(graph3)
        st.pyplot(fig3)

    # Gráfico de barra com Sexo do beneficiário
    sexo, quant_sexo = trata_resposta(resultado['sexo'])
    with graph_sexo:
        fig4, ax4 = plt.subplots()
        graph4 = ax4.bar(sexo, quant_sexo)
        ax4.set_ylabel('Total de bolsas')
        ax4.set_xticklabels(sexo, rotation=45)
        ax4.set_title("Distribuição dos beneficiados por sexo")
        ax4.bar_label(graph4)
        st.pyplot(fig4)

    graph_turno_curso, graph_pcd = st.columns(2)

    # Gráfico com Turno do curso
    turno_curso, quant_turno_curso = trata_resposta(resultado['turno_bolsa'])
    with graph_turno_curso:
        fig5, ax5 = plt.subplots()
        graph5 = ax5.bar(turno_curso, quant_turno_curso)
        ax5.set_ylabel('Total de bolsas')
        ax5.set_xticklabels(turno_curso, rotation=45)
        ax5.set_title("Distribuição de bolsas por turno")
        ax5.bar_label(graph5)
        st.pyplot(fig5)

    # Gráfico com PCD ou não
    pcd, quant_pcd = trata_resposta(resultado['pcd'])
    with graph_pcd:
        fig6, ax6 = plt.subplots()
        graph6 = ax6.bar(pcd, quant_pcd)
        ax6.set_ylabel('Total de bolsas')
        ax6.set_xticklabels(pcd, rotation=45)
        ax6.set_title("Distribuição de bolsas oferecidas")
        ax6.bar_label(graph6)
        st.pyplot(fig6)



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
    ax.set_xticklabels(dados_cidades_estados['Cidade/Estado'], rotation=45)

    # Exiba o gráfico no Streamlit
    st.pyplot(fig)


# Cria função página Universidades
def universidade():
    st.title("Dados por universidade")
    st.write("Aqui estão os dados agrupados por universidades.")
    st.write('')

# Cria o DataFrame das universidades
    dados_universidade = pd.DataFrame({'Universidade': ['USP', 'UNICAMP', 'UFMG', 'UFRJ', 'UNESP', 'UFES', 'UFRGS'],
                                       'População': [152365, 111236, 132560, 125404, 121056, 114202, 110236]})
    dados_universidade = dados_universidade.sort_values(by='Universidade')

# Cria o gráfico
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.bar(dados_universidade['Universidade'],
           dados_universidade['População'])
    ax.set_ylabel('População')
    ax.set_xticklabels(dados_universidade['Universidade'], rotation=45)

# Exibe o gráfico
    st.pyplot(fig)

# Cria a função página Curso


def curso():
    st.title("Dados por curso")
    st.write("Aqui estão os dados agrupados por curso.")
    st.write('')

# Cria o DataFrame dos cursos
    dados_curso = pd.DataFrame({'Curso': ['Medicina', 'Sisitemas de Informação', 'Marketing', 'Engenharia Civil', 'Direito', 'Administração', 'COntábeis'],
                                'População': [152365, 111236, 132560, 125404, 121056, 114202, 110236]})
    dados_curso = dados_curso.sort_values(by='Curso')

# Cria o gráfico
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.bar(dados_curso['Curso'],
           dados_curso['População'])
    ax.set_ylabel('População')
    ax.set_xticklabels(dados_curso['Curso'], rotation=85)

# Exibe o gráfico
    st.pyplot(fig)

    # Cria a função página Distribuição por idade


def idade():
    st.title("Dados por Idade")
    st.write("Aqui estão os dados agrupados por idade.")
    st.write('')

# Cria o DataFrame das idades
    dados_idade = pd.DataFrame({'Idade': ['18', '20', '25', '30', '32', '52', '40'],
                                'População': [12540, 11230, 10360, 15962, 15350, 14650, 10230]})


# Cria o gráfico
    fig, ax = plt.subplots()
    ax.bar(dados_idade['Idade'],
           dados_idade['População'], color='orange')
    ax.set_ylabel('População')
    ax.set_xticklabels(dados_idade['Idade'], rotation=85)

# Exibe o gráfico
    st.pyplot(fig)


# Criar o menu de navegação do aplicativo
menu = ['Dados Gerais', 'Regiões', 'Universidade',
        'Cursos', 'Distribuição por idade']
pagina = st.sidebar.selectbox("Selecione uma página:", menu)

# Exibir a página selecionada
if pagina == 'Dados Gerais':
    home()
elif pagina == 'Regiões':
    regioes()
elif pagina == "Universidade":
    universidade()
elif pagina == "Cursos":
    curso()
elif pagina == "Distribuição por idade":
    idade()

# Path: Sisu\app.py
