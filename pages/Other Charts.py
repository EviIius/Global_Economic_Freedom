#Imports
import pandas as pd
import numpy as np
import streamlit as st
import pandas as pd
import altair as alt
from altair import datum
import matplotlib.pyplot as plt
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame

st.set_page_config(layout='wide')
st.title("Global Economic Freedom")
st.subheader("Some other charts I created with the spare time in the project")
st.write("Please select two variables for or any filters that you would like to look at:")

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

tab1,tab2 = st.tabs(['Gradient Chart','Sorted Bar Chart'])

with tab1:
    st.write("Gradient overall I thought was neat to look at with this kind of data is it showed the area comparison.")
    gradient = alt.Chart(eco).mark_area(
    line={'color':'white'},
    color=alt.Gradient(
        gradient='linear',
        stops=[alt.GradientStop(color='white', offset=0),
               alt.GradientStop(color='#ff0000', offset=1)],
        x1=1,
        x2=1,
        y1=1,
        y2=0
    )
).encode(
    alt.X(selected_x_var),
    alt.Y(selected_y_var)
)
    st.altair_chart(gradient, use_container_width=True)

with tab2:
    st.write("Just a simple sorted bar graph")
    sort = alt.Chart(eco).mark_bar(color='#ff0000').encode(
    x= selected_x_var,
    y=alt.Y(selected_y_var).sort('-x')
)
    st.altair_chart(sort, use_container_width=True)

#Display a Map
map_data = 'https://cdn.jsdelivr.net/npm/vega-datasets@2.7.0/data/world-110m.json'

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


#Rerun Button
st.sidebar.write("If any issues occur, please click the rerun button.")
st.sidebar.button("Rerun")