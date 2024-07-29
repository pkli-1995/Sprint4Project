import streamlit as st
import pandas as pd
import plotly.express as px
import os

file_path = os.path.join('Dataset/vehicles_us_modified.csv')
vehicles = pd.read_csv(file_path)

st.header("Used Vehicle List Data Analysis")
st.dataframe(vehicles)

st.header("Totol Amount of Car Based on Condition in Each Make")
fig1 = px.histogram(df, x="make", animation_frame = 'condition')

fig1.update_layout(
    title="Total of Cars' Condition by Make",
    xaxis_title='Make of Car',
    yaxis_title='Count',
)
fig1["layout"].pop("updatemenus") 
st.plotly_chart(fig1)

st.header("Total Amount of the Types of Car with Each Make")
fig2 = px.histogram(df, x="make", animation_frame = 'type')

fig2.update_layout(
    title="Amount of Make Within Each Type",
    xaxis_title='Type of Car',
    yaxis_title='Count',
)
fig2["layout"].pop("updatemenus")  
st.plotly_chart(fig2)

st.header("Prices Compared to the Odometer of Each Make Listed")
fig3 = px.histogram(df, x="type", animation_frame = 'make')

fig3.update_layout(
    title="Types of Car in each Make",
    xaxis_title='Type of Car',
    yaxis_title='Count',
)
fig3["layout"].pop("updatemenus") 
st.plotly_chart(fig3)

st.header("Prices Compared to the Model Year of Each Make Listed")
fig4 = px.scatter(df, x='price', y='odometer', animation_frame ='condition')

fig4.update_layout(
    title="Price vs Odometer by Condition",
    xaxis_title='Price of Car',
    yaxis_title='Odometer (millions)',
    height = 500
)
fig4["layout"].pop("updatemenus") 
st.plotly_chart(fig4)

st.header("Model Year and Price with their Condition")
fig5 = px.scatter(df, x='model_year', y='price', animation_frame='condition')

fig5.update_layout(
    title="Model Year vs Price by Condition",
    xaxis_title='Model Year of Car',
    yaxis_title='Price of Car in Thousands',
    height = 500
)
fig5["layout"].pop("updatemenus") 
st.plotly_cahrt(fig5)

st.header('Compare Model Years of Car Between Make')
if st.checkbox('Show only cars before Model Year 2000'):
    # Filter DataFrame
    st.write(vehicles[(vehicles['model_year'] <= 1999)])

if st.checkbox('Show only cars between Model Year 2000 and 2010'):
    # Filter DataFrame
    st.write(vehicles[(vehicles['model_year'] >= 2000) & (vehicles['model_year'] <= 2010)])

if st.checkbox('Show only cars after Model Year 2010'):
    # Filter DataFrame
    st.write(vehicles[(vehicles['model_year'] >= 2011)])
