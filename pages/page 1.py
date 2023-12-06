import pandas as pd
import streamlit as st
import pandas as pd
import altair as alt
import time

st.set_page_config(layout='wide')
st.title("Yurr")
st.write("# Welcome to the example of my dataframe👋")
st.header("# It so far isn't much but whatever")

#Data Reading and URL Linkage to repository
url = 'https://raw.githubusercontent.com/EviIius/TableauFinalP/main/economicdata2003-2021.csv'
url2 = 'https://raw.githubusercontent.com/EviIius/TableauFinalP/main/countries.csv'
url3 = 'https://raw.githubusercontent.com/EviIius/Global_Economic_Freedom/main/Countries%20by%20category.csv'

df1 = pd.read_csv(url, sep=',')
df2 = pd.read_csv(url2, sep=',')
df3 = pd.read_csv(url3, sep=',')

merge1 = pd.merge(df1, df2, on='Countries', how='inner')
df = pd.merge(merge1, df3, on='Countries', how='inner')


#Caching
@st.cache_data  # 👈 Add the caching decorator
def load_data(url):
    df = pd.read_csv(url)
    return df

df1 = load_data(url)

@st.cache_data  # 👈 Add the caching decorator
def load_data(url2):
    df = pd.read_csv(url2)
    return df

df2 = load_data(url2)


#Creating a new dataframe different from original data
eco = df
eco['Year'] = pd.to_datetime(eco['Year'],format='%Y', errors='coerce')
eco.info()
column_list = eco.columns.unique().tolist()

selected_x_var = st.selectbox('What do you want the x variable to be?',
column_list)
selected_y_var = st.selectbox('What about the y?', column_list)

tab1,tab2 = st.tabs(['Line Chart','Bar Chart'])

with tab1:
    alt_chart = (
        alt.Chart(eco, title= f"Line Chart of {selected_x_var} and {selected_y_var}").mark_line().encode(
            x=selected_x_var,
        y=selected_y_var,
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)

with tab2:
    alt_chart = (
        alt.Chart(eco, title=f"Bar of {selected_x_var} and {selected_y_var}").mark_bar().encode(
            x=selected_x_var,
        y=selected_y_var,
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)