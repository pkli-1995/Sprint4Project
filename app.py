import streamlit as st
import pandas as pd
import plotly.express as px
import os

file_path = os.path.join('C:\\Users\\pimsi\\OneDrive\\Documents\\GitHub\\Sprint4Project\\Dataset', 'vehicles_us_modified.csv')  # Update with your actual path

vehicles = pd.read_csv(file_path)

st.header("Used Vehicle List Data Analysis")
st.dataframe(vehicles)

st.header("Totol Amount of Car Based on Condition in Each Make")
fig1 = px.histogram(vehicles, x="make", color = 'condition')

fig1.update_layout(
    title="Total of Cars' Condition by Make",
    xaxis_title='Make of Car',
    yaxis_title='Count',
)

st.plotly_chart(fig1)

st.header("Total Amount of the Types of Car with Each Make")
fig2 = px.histogram(vehicles, x="type", color = 'make')

fig2.update_layout(
    title="Types of Car in Each Make",
    xaxis_title='Type of Car',
    yaxis_title='Count',
)

st.plotly_chart(fig2)

st.header("Prices Compared to the Odometer of Each Make Listed")
fig3 = px.scatter(vehicles, x='price', y='odometer', color='make', marginal_y="rug")

fig3.update_layout(
    title="Price vs Odometer by Make",
    xaxis_title='Price of Car',
    yaxis_title='Odometer (millions)',
)

st.plotly_chart(fig3)

st.header("Prices Compared to the Model Year of Each Make Listed")
fig4 = px.scatter(vehicles, x='model_year', y='price', color='make', marginal_y="rug")

fig4.update_layout(
    title="Model Year vs Price by Make",
    xaxis_title='Model Year of Car',
    yaxis_title='Price of Car in Thousands',
)

st.plotly_chart(fig4)

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
