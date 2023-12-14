# Global Economic Freedom
### Authors: Jake Brulato

## Background Information
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Fraser_Institute_logo.svg/1200px-Fraser_Institute_logo.svg.png" alt="drawing" width="200" height = "200"/>

- Fraser Institute is a Canadian Organization that improve the quality of life for Canadians, their families, and future generations by studying, measuring, and broadly communicating the effects of government policies, entrepreneurship, and choice on their well-being. However this is not limited to their country alone as
they obtain information yearly from many different countries to showcase the different types of attributes that make up Economic Freedom. 
- In their own words, "The cornerstones of economic freedom are 
    - (1) personal choice
    - (2) voluntary exchange coordinated by markets
    - (3) freedom to enter and compete in markets
    - (4) protection of persons and their property from aggression by others."
- The overall goal is to showcase how the economic freedom of a country can fluctuate from internal and external factors over time, showcasing growth and degredation over different types of visualizations.
- To be informative of the growth of other countries is important especially in the modern world, showing how free a country is able to contribute on a global scale and their progress is why I created this app.
- Here I have the link to my data where it takes all of the Economic Freedom from 2003 - 2021 and merged with two other datasets to get groupings and longitude and latitude:
    - [Economic-Freedom-Data](https://www.fraserinstitute.org/economic-freedom/dataset?geozone=world&page=dataset&min-year=2003&max-year=2021&filter=1&date-type=range)
    - [Countries](https://developers.google.com/public-data/docs/canonical/countries_csv)
    - [Countrys (group)](https://github.com/EviIius/Global_Economic_Freedom/blob/main/datacsvs/Countries%20by%20category.csv)

## Video from the Fraser Institute for more information on Economic Freedom and its benefits
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/3_HnZa2XSrc/0.jpg)](https://www.youtube.com/watch?v=3_HnZa2XSrc)


## Link to the app
The final version of the app will always be  up on Streamlit for anyone's viewing pleasure:
[Global Economic Freedom](https://global-economic-freedom.streamlit.app/ 'Global Economic Freedom')


## For the people who want to run it on their own: Fork the repository

## Create the virtual enviorment for the files
```
python -m venv <GlobalEconomicFreedom>
```

## Import all the required packages
```
import pandas as pd
import numpy as np
import streamlit as st
import pandas as pd
import altair as alt
from altair import datum
import matplotlib.pyplot as plt
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDat
```

This will already be in the requirements.

## Run the Introduction.py file
- Open your terminal in your virtual enviorment.
- Type the following line of code and click enter:
```
streamlit run Introduction.py
```
- It will then take you to your defualt browser and display the app and its features.

## App Information
- There are four pages that are introduced to you:
    - Introduction: A page that will show off the dataframe and the amount of countries via a map.
    - Examples: Some variables and visualizations that are important .
    - Line, Bar, Histogram, Scatter: A page with fully customizable variables of your choosing as well as a map to show what filters are selected.
    - Other Charts: A page I threw together with some other charts that is similar to the previous one.
- All pages have two filters, Indiviual Country for specifics and Country group based on denomination, these will be on the sidebar of the first two pages and above the X and Y variables selectboxes on the last two.
- There is a large amount of data ranging from 2003 - 2021 so it will overall be easier to filter by specifics to get a better outlook on the variables.
- I selected variables that I thought showcased the best of the visualizations but that many not be the case, if you think one of the other charts would be better, use pages Line, Bar, Histogram, Scatter, and Other Charts to make your visualizations.


## Further Information About Economic Freedom
- [Economic Freedom: Toward a Theory of Measurement](https://books.google.com/books?id=T-lAnvB8r9QC&printsec=frontcover#v=onepage&q&f=false)
- [The concept and measurement of economic freedom](https://www.sciencedirect.com/science/article/pii/S0176268003000077?casa_token=z8NnHG3SHIMAAAAA:HfISf-LCoX4qlLCDTxVvENVC2tQkBNK-Z2ViPruSWG59SpInxU1Q1hMP_JM0TVVKZduvXpv8qIQ)
- ***An Older Version***
[Economic Freedom of the World](https://books.google.com/books?hl=en&lr=&id=79ut_adIb8oC&oi=fnd&pg=PR4&dq=Economic+Freedom+of+the+World&ots=rzoG22CXbK&sig=fSGhG4PRhry8vTisGSzuDyZcUZU#v=onepage&q=Economic%20Freedom%20of%20the%20World&f=false) 