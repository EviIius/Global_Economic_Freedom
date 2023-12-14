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
url = 'https://raw.githubusercontent.com/EviIius/Global_Economic_Freedom/main/datacsvs/economicdata2003-2021.csv'
url2 = 'https://raw.githubusercontent.com/EviIius/Global_Economic_Freedom/main/datacsvs/countries.csv'
url3 = 'https://raw.githubusercontent.com/EviIius/Global_Economic_Freedom/main/datacsvs/Countries%20by%20category.csv'

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

#Sidebar
st.sidebar.write("Here are some functions that will help make it easier to visualize the data on an individual level.")
#Country Group Filter

regions = st.sidebar.multiselect("Country Category", eco['Country (group)'].unique())

if regions:
    eco = eco[eco['Country (group)'].isin(regions)]


#Individual Country Filter
indvidual_country = st.sidebar.multiselect("Specific Country", eco['Countries'].unique())

if indvidual_country:
    eco = eco[eco['Countries'].isin(indvidual_country)]

#Optional file uploader
# user_file = st.file_uploader(
#     'Select Your Local User CSV (default provided)')

# if user_file is not None:
#     user_df = pd.read_csv(user_file)
# else:
#     st.stop()

st.markdown('''
            The following is data gathered from the Fraiser Institute, 
            a Canadian organization that has worked to gather the data of Economic 
            Freedom from many countries around the world. Our primary focus is to display how the economic freedom of a country is
            important to its ability to thrive over time and if a higher Economic Freedom means less potential poverty. Some factors include the Size of the Government, Market Openness,
            and Tax Compliance. All of these could represent a countries freedom to buy or sell and affect their overall economy and help explain to people just how important"
            + " a persons own indviduallity is heavily reliant on freedom and so is a countries ability to survive.
            ''')

#Displaying Dataframe
st.header("A dataframe containing the primary information of the all the countries different metrics along with their latitude and longitude:")
st.dataframe(eco)

#Display a Map
map_data = 'https://cdn.jsdelivr.net/npm/vega-datasets@2.7.0/data/world-110m.json'

st.header("A map that will change based off the filters you select, that way you could see multiple countries or groupings:")
countries = alt.topo_feature(map_data, 'countries')

background = alt.Chart(countries).mark_geoshape(
    fill='#808080',
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

#Rerun Button
st.sidebar.button("Rerun")