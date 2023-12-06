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

#Page Configuration
st.set_page_config(layout='wide')

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



#Format of page potentially
st.write("# Global Economic Freedom")

#Optional Sidebar Just testing

regions = st.sidebar.multiselect("Country Category", eco['Country (group)'].unique())

if regions:
    eco = eco[eco['Country (group)'].isin(regions)]

#Optional file uploader
# user_file = st.file_uploader(
#     'Select Your Local User CSV (default provided)')

# if user_file is not None:
#     user_df = pd.read_csv(user_file)
# else:
#     st.stop()

st.markdown('''
            Hello
            ''')

#Displaying Dataframe
st.header("A dataframe containing the primary information of the all the countries different metrics along with latitude and longitude")
st.dataframe(eco)

#Rerun Button
st.button("Rerun")

#Display a Map
map_data = 'https://cdn.jsdelivr.net/npm/vega-datasets@2.7.0/data/world-110m.json'

st.header("Interactable map that can show you country groupings")
countries = alt.topo_feature(map_data, 'countries')

background = alt.Chart(countries).mark_geoshape(
    fill='lightgray',
    stroke='white',
    tooltip='Countries'
).project(
    "equirectangular"
).properties(
    width=800,
    height=800
).interactive()

points = alt.Chart(eco).mark_circle().encode(
    longitude='longitude:Q',
    latitude='latitude:Q',
    size=alt.value(50),
    color= 'Country (group)',
    tooltip='ISO Code'
).interactive()

map = background + points

st.altair_chart(map, use_container_width=True)

# st.map(data= eco, latitude='latitude', longitude='longitude', color= '#FF0000', use_container_width=True, size= 100)
