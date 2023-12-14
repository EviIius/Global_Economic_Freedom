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
st.subheader("Here are some variables I have selected that would best suit the data, each with their own description " +
             "in the four main types of charts I will be focusing on.")

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


tab1,tab2,tab3,tab4 = st.tabs(['Bar Chart','Line Chart', 'Histogram Chart', 'Scatter Chart'])

with tab1:
    st.write('Here we have a summary index of the Economic Freedom over time to get a general idea of how a country\'s economic freedom has progressed.'
    + " Filtering this either by Country group or Individually will show the skewness or dips in specific years on the bars.")
             
    st.subheader("Economic Freedom Summary Index and Year")
    alt_chart = (
        alt.Chart(eco).mark_bar(color='#ff0000').encode(
            x= 'Year:T',
            y= 'Economic Freedom Summary Index',
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)

    st.write('The size of the government and its Military\'s involvement could potentially decrease a country\'s economic freedom.'
             + ' Displayed is the overall skewness with noticable outliers on a large scale. Some countries possibly gain and lose economic freedom ' +
             'as the size of the government increases.')

    st.subheader("Size of Government and Military interference in rule of law and politics")
    alt_chart = (
        alt.Chart(eco).mark_bar(color='#ff0000').encode(
            x= 'Size of Government:Q',
            y= 'Military interference in rule of law and politics:Q',
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)

    st.write("The freedom to trade on an international level is extremely important to any country\'s economic freedom" +
             'if they are limited in any capacity, it will be more difficult for them to procure items especially if there is an '
             + "ongoing issue in the country itself. Here we can see if a country has either increased or decreased over time.")
    st.subheader("Freedom to trade internationally over time")
    alt_chart = (
        alt.Chart(eco).mark_bar(color='#ff0000').encode(
            x= 'Year:T',
            y= 'Freedom to trade internationally',
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)

with tab2:
    st.write("Here is Economic Freedom over time, the freedom of a countries economy is very important." + 
             " On a large level, it is difficult to see the fluctuations for most countries but using a filter will help on an indiviual level, showcasing the overall freedom for countries. "+
             "Looking at specific countries would be best for this chart as it will be best for comparison. "
             + "These values showcase just how a country can progress over time and increase their freedom with diminishing returns, and potenially harmful ones.")
    st.subheader("Economic Freedom Summary Index and Year")
    alt_chart = (
        alt.Chart(eco).mark_line(color='#ff0000').encode(
            x= 'Year:T',
            y= 'Economic Freedom Summary Index',
            color='ISO Code'
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)

    st.write("Similarly to the bar chart, there is a large amalgmation of data that showcases each country Military to the size of the government"
             + ". It is difficult to read when all the countries are selected but you can still see noticable dips for some countries. "
             + "When filtered, it can help indicate what point in the government size was beneficial or not and how they adapted to the military\'s interference. " 
             + "In eastern countries, military is a very important aspect for a lot of people, whether it be family or security. "
             + "However there have been cases in the past where if a military interferes too much, it can affect the country as a whole.")
    
    st.subheader("Size of Government and Military interference in rule of law and politics")
    alt_chart = (
        alt.Chart(eco).mark_line(color='#ff0000').encode(
            x= 'Size of Government',
            y= 'Military interference in rule of law and politics',
            color='ISO Code'
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)

    st.write("A country\'s ability to trade internationally has become incredibly important for any type of market at his point. " +
             "If this ability to trade was weakened at any point, it could potentially have a direct causal effect on a country\'s " +
             "overall economic freedom. Similarly to the previous line charts, it would be best to filter before using it so its not as cluttered over time." +
             " The United States for example is heavily dependent on trade for our economy, so if our freedom to trade was diminished in any capacity, it would be definetly hurt our economic freedom.")
    st.subheader("Freedom to trade internationally over time")
    alt_chart = (
        alt.Chart(eco).mark_line(color='#ff0000').encode(
            x= 'Year:T',
            y= 'Freedom to trade internationally',
            color='ISO Code'
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)

with tab3:
    st.write("This tab is specifically different compared to the others as its overall only going to be taking account of how many of that specific index occured"
             + " at all in the dataset. This allows us to see on an overall what score was most common for all countries.")
    st.subheader("Economic Freedom Summary Index")
    alt_chart = (
        alt.Chart(eco).mark_bar(color='#ff0000').encode(
            x= 'Economic Freedom Summary Index',
            y= 'count()',
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)

    st.write("This tab is specifically different compared to the others as its overall only going to be taking account of how many of that specific military interference occured"
             + " at all in the dataset. This allows us to see on an overall what score was most common for all countries.")
    st.subheader("Military interference in rule of law and politics")
    alt_chart = (
        alt.Chart(eco).mark_bar(color='#ff0000').encode(
            x= 'Military interference in rule of law and politics',
            y= 'count()',
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)

    st.write("This tab is specifically different compared to the others as its overall only going to be taking account of how many of that specific Freedom to trade internationally occured"
             + " at all in the dataset. This allows us to see on an overall what score was most common for all countries.")
    st.subheader("Freedom to trade internationally")
    alt_chart = (
        alt.Chart(eco).mark_bar(color='#ff0000').encode(
            x= 'Freedom to trade internationally',
            y= 'count()',
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)
with tab4:
    st.write("A scatter plot showing all the Economic Freedom Index over time, showing the how similar they all are dotted next to each other. "+
             "Similar to the line, you can see some noticable outliers in the data over time, signifyiing the a decrease or increase as time went on.")
    st.subheader("Economic Freedom Summary Index and Year")
    alt_chart = (
        alt.Chart(eco).mark_circle(color='#ff0000').encode(
            x= 'Year:T',
            y= 'Economic Freedom Summary Index',
            color='ISO Code'
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)
    st.write("A scatter plot showing the Size of Government over Military interference in rule of law and politics, referencing a lot of correlation in the data. "+
             "Notiacably though, most countries with a large government size near the same level, have a similar military interference.")
    st.subheader("Size of Government and Military interference in rule of law and politics")
    alt_chart = (
        alt.Chart(eco).mark_circle(color='#ff0000').encode(
            x= 'Size of Government',
            y= 'Military interference in rule of law and politics',
            color='ISO Code'
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)

    st.write("A scatter plot showing the Freedom to trade internationally over year, showing trends of countries slowly losing or gaining the ability to trade internationally "+
             "If you filter by any western category countries, then you can see a higher degree of freedom compared to eastern.")
    st.subheader("Freedom to trade internationally over time")
    alt_chart = (
        alt.Chart(eco).mark_circle(color='#ff0000').encode(
            x= 'Year:T',
            y= 'Freedom to trade internationally',
            color='ISO Code'
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)

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