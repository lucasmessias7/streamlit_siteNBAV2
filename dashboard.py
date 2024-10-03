import streamlit as st
import pandas as pd
from io import StringIO


st.title('upload de arquivo')


def faz_busca(busca):
    pesquisa = st.text_input('Digite sua pesquisa:')
    if pesquisa:
        dados_filtrados = busca[busca.apply(lambda row: row.astype(str).str.contains(pesquisa, case=False).any(), axis=1)]
        st.write(f"Resultados para '{pesquisa}':")
        st.dataframe(dados_filtrados)
    else:
        st.write("Digite algo na barra de pesquisa para ver os resultados.")



dados = None
inserir_arquivo = st.file_uploader('Insira o arquivo CSV', type='csv')
if inserir_arquivo is not None:
    st.title('Dados gerais dos jogadores da NBA 23-24')
    dados = pd.read_csv(inserir_arquivo, delimiter=',')
    dados=dados[['Player','FG', 'GS','Pos','MP','FGA','FG%','3P','3P%','2P','2PA','2P%','ORB','DRB','TRB','AST','BLK','PTS']]
    st.write(dados)
    filtro = ['Pontos','Rebotes', 'Assistencias']
    filtrado = st.sidebar.selectbox('NBA', filtro)



assistencias = dados[['Player', 'GS', 'Pos', 'AST']]
pontos = dados[['Player', 'GS', 'Pos', 'PTS']]
rebotes = dados[['Player', 'GS','Pos', 'TRB']]


if filtrado == 'Pontos':
    st.title('Pontos por Jogador')
    faz_busca(pontos)
    pontos


if filtrado == 'Rebotes':
    st.title('Rebotes por jogador')
    faz_busca(rebotes)
    rebotes


if filtrado == 'Assistencias':
    st.title('Assistência por jogador')
    faz_busca(assistencias)
    assistencias
