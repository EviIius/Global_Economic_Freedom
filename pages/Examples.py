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
st.subheader("Here I have selected variables that I think would be best to showcase overall in our data" +
             "this includes potenial reasons for the Economic Freedom Summary Index being vastly different for most countries.")

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
st.sidebar.write("Filtering on any level will help the graphs look cleaner as there is a large amount of data over many years:")
regions = st.sidebar.multiselect("Country Category", eco['Country (group)'].unique())

if regions:
    eco = eco[eco['Country (group)'].isin(regions)]

#Individual Country Filter
indvidual_country = st.sidebar.multiselect("Specific Country", eco['Countries'].unique())

if indvidual_country:
    eco = eco[eco['Countries'].isin(indvidual_country)]


tab1,tab2,tab3,tab4 = st.tabs(['Line Chart','Bar Chart', 'Histogram Chart', 'Scatter Chart'])

with tab1:
    st.write("Here are some example line charts that will show some of the best points of the data:")
    st.subheader("Economic Freedom Summary Index and Year")
    alt_chart = (
        alt.Chart(eco).mark_line(color='#ff0000').encode(
            x= 'Year:T',
            y= 'Economic Freedom Summary Index',
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)
    st.subheader("Size of Government and Military interference in rule of law and politics")
    alt_chart = (
        alt.Chart(eco).mark_line(color='#ff0000').encode(
            x= 'Size of Government',
            y= 'Military interference in rule of law and politics',
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)

    st.subheader("Freedom to trade internationally over time")
    alt_chart = (
        alt.Chart(eco).mark_line(color='#ff0000').encode(
            x= 'Year:T',
            y= 'Freedom to trade internationally',
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)

with tab2:
    st.subheader("Economic Freedom Summary Index and Year")
    alt_chart = (
        alt.Chart(eco).mark_bar(color='#ff0000').encode(
            x= 'Year:T',
            y= 'Economic Freedom Summary Index',
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)
    st.subheader("Size of Government and Military interference in rule of law and politics")
    alt_chart = (
        alt.Chart(eco).mark_bar(color='#ff0000').encode(
            x= 'Size of Government',
            y= 'Military interference in rule of law and politics',
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)

    st.subheader("Freedom to trade internationally over time")
    alt_chart = (
        alt.Chart(eco).mark_bar(color='#ff0000').encode(
            x= 'Year:T',
            y= 'Freedom to trade internationally',
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)

with tab3:
    st.subheader("Economic Freedom Summary Index and Year")
    alt_chart = (
        alt.Chart(eco).mark_bar(color='#ff0000').encode(
            x= 'Economic Freedom Summary Index',
            y= 'count()',
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)
    st.subheader("Size of Government and Military interference in rule of law and politics")
    alt_chart = (
        alt.Chart(eco).mark_bar(color='#ff0000').encode(
            x= 'Military interference in rule of law and politics',
            y= 'count()',
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)

    st.subheader("Freedom to trade internationally over time")
    alt_chart = (
        alt.Chart(eco).mark_bar(color='#ff0000').encode(
            x= 'Freedom to trade internationally',
            y= 'count()',
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)
with tab4:
    st.subheader("Economic Freedom Summary Index and Year")
    alt_chart = (
        alt.Chart(eco).mark_circle(color='#ff0000').encode(
            x= 'Year:T',
            y= 'Economic Freedom Summary Index',
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)
    st.subheader("Military interference in rule of law and politics")
    alt_chart = (
        alt.Chart(eco).mark_circle(color='#ff0000').encode(
            x= 'Size of Government',
            y= 'Military interference in rule of law and politics',
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)

    st.subheader("Freedom to trade internationally over time")
    alt_chart = (
        alt.Chart(eco).mark_circle(color='#ff0000').encode(
            x= 'Year:T',
            y= 'Freedom to trade internationally',
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)



# gradient = alt.Chart(eco).mark_area(
#     line={'color':'darkgreen'},
#     color=alt.Gradient(
#         gradient='linear',
#         stops=[alt.GradientStop(color='white', offset=0),
#                alt.GradientStop(color='darkgreen', offset=1)],
#         x1=1,
#         x2=1,
#         y1=1,
#         y2=0
#     )
# ).encode(
#     alt.X('Year:T'),
#     alt.Y('Economic Freedom Summary Index:Q')
# )

# st.altair_chart(gradient, use_container_width=True)

#Display a Map
# map_data = 'https://cdn.jsdelivr.net/npm/vega-datasets@2.7.0/data/world-110m.json'
# countries = alt.topo_feature(map_data, 'countries')

# background = alt.Chart(countries).mark_geoshape(
#     fill='#CBC3E3',
#     stroke='white',
#     tooltip='Countries'
# ).project(
#     "equirectangular"
# ).properties(
#     width=800,
#     height=800
# ).interactive()

# points = alt.Chart(eco).mark_circle().encode(
#     longitude='longitude:Q',
#     latitude='latitude:Q',
#     size=alt.value(50),
#     color= 'Country (group)',
#     tooltip='ISO Code'
# ).interactive()

# map = background + points

# st.altair_chart(map, use_container_width=True)

#Rerun Button
st.sidebar.write("If any issues occur, please click the rerun button.")
st.sidebar.button("Rerun")