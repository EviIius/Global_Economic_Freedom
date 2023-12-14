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
st.subheader("There are many other variables in the data so here is a page for you to explore specific ones yourself")
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
eco['No Filter'] = None
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


tab1,tab2,tab3,tab4 = st.tabs(['Line Chart','Bar Chart', 'Histogram Chart', 'Scatter Chart'])

with tab1:
        if "visibility" not in st.session_state:
            st.session_state.visibility = "visible"
            st.session_state.disabled = False

        st.checkbox("Disable Line Color Option", key="disabled")

        color = st.selectbox('Please Select your Line Color variable:', column_list, index=69, placeholder="Choose an option", 
                     label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled)
        st.write("Here you can create any Line Chart that you choose to better explore that data yourself")
        alt_chart = (
        alt.Chart(eco, title= f"Line Chart of {selected_x_var} and {selected_y_var}").mark_line(color='#ff0000').encode(
            x=selected_x_var,
        y=selected_y_var,
        color= color
        )
        .interactive()
        )
        st.altair_chart(alt_chart, use_container_width=True)

with tab2:

    st.write("Here you can create any Bar Graph that you choose to better explore that data yourself")
    alt_chart = (
        alt.Chart(eco, title=f"Bar of {selected_x_var} and {selected_y_var}").mark_bar(color='#ff0000').encode(
            x=selected_x_var,
        y=selected_y_var,
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)

with tab3:
    st.write("Here you can create any Histogram that you choose to better explore that data yourself")
    alt_chart = (
        alt.Chart(eco, title=f"Histogram of {selected_x_var} and the count of each value").mark_bar(color='#ff0000').encode(
            x=selected_x_var,
        y='count()'
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)
with tab4:
        if "visibility" not in st.session_state:
            st.session_state.visibility = "visible"
            st.session_state.disabled = False

        st.checkbox("Disable Scatter Color Option", key="d")

        color2 = st.selectbox('Please Select your Scatter Color variable:', column_list, index=69, placeholder="Choose an option", 
                     label_visibility=st.session_state.visibility,
        disabled=st.session_state.d)
        st.write("Here you can create any Scatter Chart that you choose to better explore that data yourself")
        alt_chart = (
        alt.Chart(eco, title= f"Scatter Chart of {selected_x_var} and {selected_y_var}").mark_circle(color='#ff0000').encode(
            x=selected_x_var,
        y=selected_y_var,
        color= color2
        )
        .interactive()
        )
        st.altair_chart(alt_chart, use_container_width=True)

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