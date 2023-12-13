# Global Economic Freedom
### Authors: Jake Brulato

## Background Information
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Fraser_Institute_logo.svg/1200px-Fraser_Institute_logo.svg.png" alt="drawing" width="200" height = "200"/>
[Fraser Institute](https://www.fraserinstitute.org/economic-freedom/dataset?geozone=world&page=dataset&min-year=2003&max-year=2021&filter=1&date-type=range)

## Video from the Fraser Institute for more information on Economic Freedom and its benefits
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/3_HnZa2XSrc/0.jpg)](https://www.youtube.com/watch?v=3_HnZa2XSrc)


## Link to the app
The final version of the app will always be  up on Streamlit for anyones viewing pleasure.
[Global Economic Freedom] (https://global-economic-freedom.streamlit.app/ 'Global Economic Freedom')


## For the people who want to run it on their own: Fork the repository

## Create the virtual enviorment for the files
```
python -m venv <name_of_virtualenv>
```

## Import all the required packages
```
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
```

This will already be in the requirements

## Run the Introduction.py file
- Open your terminal in your virtual enviorment
- Type the following line of code and click enter:
```
streamlit run Introduction.py
```
- It will then take you to your defualt browser and display the app and its features

## App Information
- There are four pages that are introduced to you:
    - Introduction: A page that will show off the dataframe and the amount of countries via a map
    - Examples: Some variables and visualizations that are important 
    - Line, Bar, Histogram, Scatter: A page with fully customizable variables of your choosing as well as a map to show what filters are selected
    - Other Charts: A page I threw together with some other charts that is similar to the previous one
- All pages have two filters, Indiviual Country for specifics and Country group based on denomination, these will be on the sidebar of the first two pages and above the X and Y variables selectboxes on the last two.
- There is a large amount of data ranging from 2001 - 2021 so it will overall be easier to filter by specifics to get a better outlook on the variables


