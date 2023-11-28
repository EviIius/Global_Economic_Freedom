
import pandas as pd
import streamlit as st


mt= pd.read_csv('/Users/jakebrulato/Downloads/Midterm Data.csv')

st.write("# Welcome to the example of my tableau dataframe👋")
st.sidebar.success("Select a demo above.")



st.dataframe(mt)