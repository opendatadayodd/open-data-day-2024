# Escreva o seu codigo aqui
import streamlit as st
import pandas as pd
import plotly.express as px

from pathlib import Path

st.set_page_config(page_icon=':sunglasses:', page_title='Open Data Day')

summary_file = Path.cwd() / "data" / "processed" / f"summary_recursos_disponiveis.pkl"

st.title('OPEN DATA DAY 2024 :sunglasses:')



df = pd.read_pickle(summary_file)

ano_selecionado = st.selectbox('Selecione um ano', df['Ano'].unique())

dados = df[df['Ano'].isin([ano_selecionado])]

st.dataframe(dados, use_container_width=True)

fig = px.pie(dados, names='Objetivo', values='Valor', title='Recursos disponíveis para os ODS')
st.plotly_chart(fig, use_container_width=True)