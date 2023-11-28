import pandas as pd
import streamlit as st
import pandas as pd
import altair as alt
import time

st.set_page_config(layout='wide')
st.title("Yurr")
st.write("# Welcome to the example of my dataframe👋")
st.header("# It so far isn't much but whatever")



url = 'https://raw.githubusercontent.com/EviIius/TableauFinalP/main/economicdata2003-2021.csv'
df = pd.read_csv(url, sep=',')


#Creating a new dataframe different from original data
eco = pd.DataFrame(df)
column_list = eco.columns.unique().tolist()

selected_x_var = st.selectbox('What do you want the x variable to be?',
column_list)
selected_y_var = st.selectbox('What about the y?', column_list)

tab1,tab2 = st.tabs(['Line Chart','Bar Chart'])

with tab1:
    alt_chart = (
        alt.Chart(eco, title= f"Line Chart of {selected_x_var} and {selected_y_var}").mark_line().encode(
            x=selected_x_var,
        y=selected_y_var,
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)

with tab2:
    alt_chart = (
        alt.Chart(eco, title=f"Bar of {selected_x_var} and {selected_y_var}").mark_bar().encode(
            x=selected_x_var,
        y=selected_y_var,
        )
        .interactive()
        )
    st.altair_chart(alt_chart, use_container_width=True)