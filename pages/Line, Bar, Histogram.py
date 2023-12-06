#Imports
import pandas as pd
import streamlit as st
import pandas as pd
import altair as alt
from altair import datum
import matplotlib.pyplot as plt
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import folium as f
# from vega_datasets import data

st.set_page_config(layout='wide')
st.title("Global Economic Freedom")
st.header("# It so far isn't much but whatever")

#Data Reading and URL Linkage to repository
url = 'https://raw.githubusercontent.com/EviIius/Global_Economic_Freedom/main/economicdata2003-2021.csv'
url2 = 'https://raw.githubusercontent.com/EviIius/Global_Economic_Freedom/main/countries.csv'
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

@st.cache_data  # 👈 Add the caching decorator
def load_data(url3):
    df = pd.read_csv(url3)
    return df

df3 = load_data(url3)


#Creating a new dataframe different from original data
eco = df
eco['Year'] = pd.to_datetime(eco['Year'],format='%Y', errors='coerce')
eco.info()
column_list = eco.columns.unique().tolist()

#Country Region Filter
regions = st.multiselect("Country Category", eco['Country (group)'].unique())

if regions:
    eco = eco[eco['Country (group)'].isin(regions)]


#Options for the Select box
selected_x_var = st.selectbox('Please Select your X variable:',
column_list, index=0, placeholder="Choose an option")
selected_y_var = st.selectbox('Please Select your Y variable:', column_list, index=0, placeholder="Choose an option")

tab1,tab2,tab3 = st.tabs(['Line Chart','Bar Chart', 'Histogram Chart'])

with tab1:
    st.write("hello")
    alt_chart = (
        alt.Chart(eco, title= f"Line Chart of {selected_x_var} and {selected_y_var} by {regions}").mark_line().encode(
            x=selected_x_var,
        y=selected_y_var,
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)

with tab2:
    st.write("hello")
    alt_chart = (
        alt.Chart(eco, title=f"Bar of {selected_x_var} and {selected_y_var} by {regions}").mark_bar().encode(
            x=selected_x_var,
        y=selected_y_var,
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)

with tab3:
    st.write("hello")
    alt_chart = (
        alt.Chart(eco, title=f"Histogram of {selected_x_var} and the count of each value by {regions}").mark_bar(color='#ff0000').encode(
            x=selected_x_var,
        y='count()'
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)