#Imports
import pandas as pd
import streamlit as st
import pandas as pd
import altair as alt
import time
import matplotlib.pyplot as plt
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame

#Page Configuration
st.set_page_config(layout='wide')

#Data Reading and URL Linkage to repository
url = 'https://raw.githubusercontent.com/EviIius/TableauFinalP/main/economicdata2003-2021.csv'
url2 = 'https://raw.githubusercontent.com/EviIius/TableauFinalP/main/countries.csv'

df1 = pd.read_csv(url, sep=',')
df2 = pd.read_csv(url2, sep=',')

df = pd.merge(df1, df2, on='Countries', how='inner')


#Creating a new dataframe different from original data
eco = df
eco['Year'] = pd.to_datetime(eco['Year'],format='%Y', errors='coerce')
eco.info()


#Format of page potentially
st.write("# Welcome to the example of my dataframe👋")
st.header("# It so far isn't much but whatever")

#Optional Sidebar Just testing
st.sidebar.header('Word Cloud Settings')
max_word = st.sidebar.slider("Max Words",min_value=10,max_value=200,value=100, step=10)
max_font = st.sidebar.slider("Size of largest Word",min_value=50,max_value=350,value=60, step=10)
img_width = st.sidebar.slider("Image Width",min_value=100,max_value=800,value=600, step=10)
random = st.sidebar.slider("Random State", min_value=30,max_value=100,value=20)
remove_stop_words = st.sidebar.checkbox("Remove Stop Words?",value=True)
st.sidebar.header('Word Count Settings')
word_count = st.sidebar.slider("Minimum count of words",min_value=5,max_value=100,value=40, step=1)

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
st.dataframe(df)

#Display a Map

# plt.scatter(x=eco['longitude'], y=eco['latitude'])
# plt.show()

# geometry = [Point(xy) for xy in zip(eco['longitude'], eco['latitude'])]
# gdf = GeoDataFrame(eco, geometry=geometry)   

# #this is a simple map that goes with geopandas
# world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# gdf.plot(ax=world.plot(figsize=(10, 6)), marker='o', color='red', markersize=15);
# st.pyplot(gdf)

st.map(data= eco, latitude='latitude', longitude='longitude')

#Caching the data

# @st.cache_data()
# def load_file(user_file):
#     time(5)
#     if user_file is not None:
#         df = pd.read_csv(user_file)
#     else:
#         df = pd.read_csv('Midterm Data.csv')
#     return(df)

# df=load_file(user_file)
