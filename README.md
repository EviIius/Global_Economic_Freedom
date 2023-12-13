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


