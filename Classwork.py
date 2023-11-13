import pandas as pd
import streamlit as st


mt= pd.read_csv('/Users/jakebrulato/Downloads/Midterm Data.csv')

st.dataframe(mt)

