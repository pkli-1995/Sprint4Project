import streamlit as st
import pandas as pd
import plotly.express as px

vehicles = pd.read_csv("/datasets/vehicles_us.csv",sep=",")

print(vehicles)