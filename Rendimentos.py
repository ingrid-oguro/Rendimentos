import pandas as pd
import numpy as np
import streamlit as st
import altair as alt

import pip
pip.main(["install", "openpyxl"])
PAGE_CONFIG = {"page_title": "Indicadores", "page_icon": ":label:", "layout": "wide"}
st.set_page_config(**PAGE_CONFIG)

#GRÁFICO DISICPLINA
mf0 = pd.read_excel('mediafinal.xlsx')
mf = mf0.query('NOTA <= 10')

st.subheader('Média Final na Disciplina')
disciplina = sorted(mf.DISCIPLINA.unique())
disciplina_selecionada = st.selectbox('Disciplina',disciplina)
disci2 = mf.query('DISCIPLINA == @disciplina_selecionada ')

alt.data_transformers.enable('default', max_rows=None)
grafico_final = alt.Chart(disci2).mark_circle(size=100).encode(
    alt.X('CODPERLET:O',scale=alt.Scale(zero=False) ,axis=alt.Axis( title='Periodo') ),
    alt.Y('NOTA',axis=alt.Axis(title='Nota', orient = "left") ),
    tooltip = ['NOME','RA'],
    #color=alt.Color('SIT_MATR',  legend=None )
    ).interactive().properties(width=800,height=400)
st.altair_chart(grafico_final, use_container_width=True)

#GRÁFICO CURSO
mg = pd.read_excel('mediageral.xlsx')

st.subheader('Média geral na Graduação')


####
cursos3 = ['Todos','Administração','Ciências Econômicas','Engenharia da Computação','Engenharia de Produção','Direito']
#cursos3.extend(curso3)
curso_selecionado3 = st.selectbox('Graduação:',cursos3)
curso2 = mg
if 'Todos' not in curso_selecionado3: 
    curso2 = mg.query('COMPLEMENTO == @curso_selecionado3 ')

####

aluno = sorted(curso2.NOME.unique())
alunos = ['Todos']
alunos.extend(aluno)
aluno_selecionado = st.selectbox('Aluno',alunos)


if 'Todos' not in aluno_selecionado: 
    curso2 = curso2.query('NOME == @aluno_selecionado ')



curso3 = curso2[curso2['NOTA'].notna()]

grafico_geral = alt.Chart(curso3).mark_circle(size=100).encode(
alt.X('CODPERLET:O',scale=alt.Scale(zero=False) ,axis=alt.Axis( title='Periodo') ),
alt.Y('NOTA',axis=alt.Axis(title='Nota', orient = "left") ),
tooltip = ['NOME','RA'],
#color=alt.Color('SIT_MATR',  legend=None )
 ).interactive().properties(width=800,height=400)
st.altair_chart(grafico_geral, use_container_width=True)


if 'Todos' not in curso_selecionado3: 
    mg = mg.query('COMPLEMENTO == @curso_selecionado3 ')

a = mg.groupby(['RA',  'NOME','COMPLEMENTO'])['NOTA'].mean()
b = a.to_frame()
c = b.reset_index()
d = c.sort_values(by=['NOTA'], ascending=False)



st.dataframe(d.style.format({"RA": "{:.0f}"}),width=800, height=400)
