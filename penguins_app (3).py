import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import random
import seaborn as sns

st.title('Nana Frimpong')

#Bring in the data
df=sns.load_dataset('penguins')
df=df.dropna()

#show the data
st.dataframe(df)

#show the barplot
penguin_counts=df['island'].value_counts().reset_index()
fig=px.bar(penguin_counts,x ='island', y='count', color='island', title="Count by Island")
st.plotly_chart(fig)

#show the boxplot
fig=px.box(df, x='island', y='body_mass_g')
st.plotly_chart(fig)

#show the scatterplot
fig_scatter=px.scatter(df, x='body_mass_g', y='bill_length_mm', color='species')
st.plotly_chart(fig_scatter)

# Load the dataset from seaborn
penguins = sns.load_dataset("penguins").dropna()

# Create a violin plot
fig = px.violin(
    penguins,
    x="species",
    y="body_mass_g",
    color="sex",           
    box=True,             
    points="all"  
    
)

fig.update_layout(title="Penguin Body Mass by Species and Sex")
st.plotly_chart(fig)
