import streamlit as st
import pandas as pd

st.title("🔥 California Wildfire Risk Analysis")

fires = pd.read_csv("/Users/nickvenditti/Desktop/Californai Wildfire Project/Data/fires_all_with_transmission_proximity.csv")

# Prepare data for st.map()
map_data = fires[['centroid_lat', 'centroid_lon']].dropna()
map_data.columns = ['lat', 'lon']

st.write(f"Showing {len(map_data):,} fires on map")
st.map(map_data)

st.write("### Statistics")
st.write(f"Average distance to power line: {fires['dist_to_line_miles'].mean():.2f} miles")
st.write(f"Fires near power lines (<1 mile): {(fires['dist_to_line_miles'] < 1).sum()}")
