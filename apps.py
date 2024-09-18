import streamlit as st
import pandas as pd

st.header('Job details')
data= pd.read_csv('/workspaces/Bank_Details/mentornow/bank.csv')


a= data['job'].unique()


option= st.selectbox('Select the job',(a))
st.write(option)
jobs = data 

df= data[data['job']== option]
st.write(df)

ave=df['age'].mean()

st.write(round(ave))

st.metric(label="Avarage Age", value="39", delta="10" )
