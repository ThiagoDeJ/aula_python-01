import streamlit as st
import pandas as pd
import plotly.express as px

#CRIAÇÃO DO TITULO
st.title("Dashboard de Funcionarios")

#CARREGAMENTO DOS DADOS
df = pd.read_csv("novos_dados.csv")
st.subheader("Tabela de dados")
st.dataframe(df)

#CRIAÇÃO DE FILTRO
departamento = st.selectbox("Selecione o Departamento", df["departamento"].unique())
df_filtrado = df[df["departamento"]== departamento]
st.subheader("Dados Filtrados")
st.write(df_filtrado)

#ELABORAAÇÃO DE GRAFICO

barra = px.bar(
        df_filtrado,
        x="nome_completo",
        y="salario_mensal_brl",
        color="nome_completo",
        title="Salario dos Funcionários"
)

st.plotly_chart(barra)