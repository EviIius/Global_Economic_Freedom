import streamlit as st
import pandas as pd
import altair as alt
import time

st.set_page_config(layout='wide')

url = 'https://raw.githubusercontent.com/EviIius/TableauFinalP/main/economicdata2003-2021.csv'
df = pd.read_csv(url, sep=',')

eco = pd.DataFrame(df)
eco['Year'] = eco['Year'].astype('datetime64[ns]')
eco['Year'] = pd.to_datetime(eco['Year'], format='%y%m%d')
eco.info()


# df['Year'] = pd.to_datetime(df['Year']).dt.strftime('%Y')
# print(df['Year'])
st.write("# Welcome to the example of my dataframe👋")
st.header("# It so far isn't much but whatever")
st.sidebar.success("WIP.")

# user_file = st.file_uploader(
#     'Select Your Local User CSV (default provided)')

# if user_file is not None:
#     user_df = pd.read_csv(user_file)
# else:
#     st.stop()

st.dataframe(eco)


# @st.cache_data()
# def load_file(user_file):
#     time(5)
#     if user_file is not None:
#         df = pd.read_csv(user_file)
#     else:
#         df = pd.read_csv('Midterm Data.csv')
#     return(df)

# df=load_file(user_file)
