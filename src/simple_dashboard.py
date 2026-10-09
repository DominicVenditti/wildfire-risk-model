import streamlit as st
import pandas as pd

st.title("🔥 California Wildfire Risk Analysis")

# Load data
fires = pd.read_csv("/Users/nickvenditti/Desktop/Californai Wildfire Project/Data/fires_all_with_transmission_proximity.csv")
fires["ALARM_DATE"] = pd.to_datetime(fires["ALARM_DATE"])

# Date filter
min_date = fires["ALARM_DATE"].min().date()
max_date = fires["ALARM_DATE"].max().date()
date_range = st.sidebar.date_input("Select date range", value=[min_date, max_date])

if len(date_range) == 2:
    filtered = fires[(fires["ALARM_DATE"].dt.date >= date_range[0]) & 
                     (fires["ALARM_DATE"].dt.date <= date_range[1])]
else:
    filtered = fires

st.write(f"Showing {len(filtered):,} fires from {date_range[0]} to {date_range[1]}")

# Statistics
st.write("### Key Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Fires", len(filtered))
col2.metric("Avg Fire Size", f"{filtered['GIS_ACRES'].mean():,.0f} acres")
col3.metric("Near Power Lines", (filtered['dist_to_line_miles'] < 1).sum())

# Charts using Streamlit native charts
st.write("### Fire Size Distribution")
size_chart = filtered['GIS_ACRES'].value_counts(bins=10).sort_index()
st.bar_chart(size_chart)

st.write("### Distance to Power Lines")
dist_chart = filtered['dist_to_line_miles'].value_counts(bins=10).sort_index()
st.bar_chart(dist_chart)

st.write("### Fire Data")
st.dataframe(filtered[['FIRE_NAME', 'ALARM_DATE', 'GIS_ACRES', 'dist_to_line_miles']].head(50))
