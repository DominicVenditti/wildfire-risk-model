import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Fire Map Test")

fires = pd.read_csv("/Users/nickvenditti/Desktop/Californai Wildfire Project/Data/fires_all_with_transmission_proximity.csv")

fig = px.scatter_mapbox(
    fires, 
    lat="centroid_lat", 
    lon="centroid_lon",
    zoom=5,
    height=600
)
fig.update_layout(mapbox_style="open-street-map")

st.plotly_chart(fig)
