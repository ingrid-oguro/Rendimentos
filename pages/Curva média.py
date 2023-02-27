import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import numpy as np
import altair as alt
import pip
pip.main(["install", "plotly.express"])

#Gráfico 3
mg = pd.read_excel('mediageral.xlsx')

st.subheader('Média geral semestral')

d = mg.groupby(['CODPERLET',  'COMPLEMENTO'])['NOTA'].mean()
e = d.to_frame()
f = e.reset_index()

g = mg.groupby(['CODPERLET'])['NOTA'].mean()
h = g.to_frame()
i = h.reset_index()

# curso = sorted(mg.COMPLEMENTO.unique())
# curso_selecionado002 = st.selectbox('Curso :',curso)
# curso002 = f.query('COMPLEMENTO == @curso_selecionado002')

###########
cursos3 = ['Todos','Administração','Ciências Econômicas','Engenharia da Computação','Engenharia de Produção','Direito']
#cursos3.extend(curso3)
curso_selecionado3 = st.selectbox('Graduação:',cursos3)
curso002 = i
if 'Todos' not in curso_selecionado3: 
    curso002 = f.query('COMPLEMENTO == @curso_selecionado3 ')
###########


media_curso = alt.Chart(curso002).mark_line().encode(
    x='CODPERLET:O',
    y='NOTA'
).interactive()
st.altair_chart(media_curso, use_container_width=True)

# curso = sorted(mg.COMPLEMENTO.unique())
# curso_selecionado = st.selectbox('Curso',curso)

# semestre = sorted(mg.CODPERLET.unique())
# semestre_selecionado = st.selectbox('Semestre',semestre)
# curso2 = mg.query('COMPLEMENTO == @curso_selecionado & CODPERLET == @semestre_selecionado')
# rankdf = curso2.query('CODPERLET == @semestre_selecionado')
# sorted_df = curso2.sort_values(by=['NOTA'], ascending=False).reset_index()
# st.dataframe(sorted_df.style.background_gradient(cmap='CMRmap'))

