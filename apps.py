import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

st.header('Job details')
data= pd.read_csv('/workspaces/Bank_Details/mentornow/bank.csv')


a= data['job'].unique()


option= st.selectbox('Select the job',(a))
st.write(option)
jobs = data 

df= data[data['job']== option]
st.write(df)

col1,col2,col3=st.columns(3)
c1,c2=st.columns(2)
ave=df['age'].mean()

st.write(round(ave))

col1.metric(label="Avarage Age", value=39 )

counts=df['marital'].value_counts()['married']
col2.metric(label="Married", value= counts)

ave=df['balance'].mean()

col3.metric(label='avarage balance',value=ave)



fig = px.density_heatmap(df, x="marital", y="age")

c1.plotly_chart(fig)

fig2=px.histogram(df,x="age" )

c2.plotly_chart(fig2)

