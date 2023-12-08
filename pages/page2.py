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

#Individual Country Filter
indvidual_country = st.multiselect("Specific Country", eco['Countries'].unique())

if indvidual_country:
    eco = eco[eco['Countries'].isin(indvidual_country)]


#Options for the Select box
selected_x_var = st.selectbox('Please Select your X variable:',
column_list, index=0, placeholder="Choose an option")
selected_y_var = st.selectbox('Please Select your Y variable:', column_list, index=0, placeholder="Choose an option")

scatter = alt.Chart(eco).mark_circle().encode(
    alt.X(selected_x_var).scale(zero=False),
    alt.Y(selected_y_var).scale(zero=False, padding=1),
    # color='species',
    # size='petalWidth'
)

st.altair_chart(scatter, use_container_width=True)


gradient = alt.Chart(eco).mark_area(
    line={'color':'darkgreen'},
    color=alt.Gradient(
        gradient='linear',
        stops=[alt.GradientStop(color='white', offset=0),
               alt.GradientStop(color='darkgreen', offset=1)],
        x1=1,
        x2=1,
        y1=1,
        y2=0
    )
).encode(
    alt.X('Year:T'),
    alt.Y('Economic Freedom Summary Index:Q')
)

st.altair_chart(gradient, use_container_width=True)

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