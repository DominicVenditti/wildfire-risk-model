import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('🔥 California Wildfire Risk Analysis')
st.write('Interactive dashboard showing fire locations and risk factors')

# Load data
@st.cache_data
def load_data():
    fires = pd.read_csv('/Users/nickvenditti/Desktop/Californai Wildfire Project/Data/fires_all_with_transmission_proximity.csv')
    fires['ALARM_DATE'] = pd.to_datetime(fires['ALARM_DATE'])
    return fires

fires = load_data()

# Sidebar filters
st.sidebar.header('Filter Options')

# Date range filter
min_date = fires['ALARM_DATE'].min().date()
max_date = fires['ALARM_DATE'].max().date()

date_range = st.sidebar.date_input(
    "Select date range",
    value=[min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Apply filters
if len(date_range) == 2:
    start_date, end_date = date_range
    filtered = fires[
        (fires['ALARM_DATE'].dt.date >= start_date) & 
        (fires['ALARM_DATE'].dt.date <= end_date)
    ].copy()
else:
    filtered = fires.copy()

st.sidebar.write(f"Showing **{len(filtered)}** fires")

# Title with date range
st.write(f"### Fire Locations: {date_range[0]} to {date_range[1]}")

# Create scatter plot
fig, ax = plt.subplots(figsize=(12, 8))

# Color based on distance to power line
colors = ['red' if d < 1 else 'orange' if d < 3 else 'yellow' for d in filtered['dist_to_line_miles']]

scatter = ax.scatter(
    filtered['centroid_lon'], 
    filtered['centroid_lat'],
    c=colors,
    s=filtered['GIS_ACRES']/500,
    alpha=0.6,
    edgecolors='black',
    linewidth=0.5
)

ax.set_xlabel('Longitude', fontsize=12)
ax.set_ylabel('Latitude', fontsize=12)
ax.set_title(f'California Fire Locations (n={len(filtered)})', fontsize=14)

# Add grid
ax.grid(True, alpha=0.3)

# Custom legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='red', label='Near power line (<1 mi)'),
    Patch(facecolor='orange', label='Moderate distance (1-3 mi)'),
    Patch(facecolor='yellow', label='Far from lines (>3 mi)')
]
ax.legend(handles=legend_elements, loc='upper right')

st.pyplot(fig)

# Statistics
st.write("### Statistics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Fires", f"{len(filtered):,}")
col2.metric("Avg Fire Size", f"{filtered['GIS_ACRES'].mean():,.0f} acres")
col3.metric("Avg Distance to Line", f"{filtered['dist_to_line_miles'].mean():.2f} miles")
col4.metric("Near Power Lines", f"{(filtered['dist_to_line_miles'] < 1).sum()}")

# Charts
st.write("### Analysis")

col_left, col_right = st.columns(2)

with col_left:
    st.write("**Fires by Distance to Power Line**")
    dist_bins = pd.cut(filtered['dist_to_line_miles'], bins=[0, 1, 3, 5, 10, 100])
    dist_counts = dist_bins.value_counts().sort_index()
    dist_counts.index = [str(x) for x in dist_counts.index]
    st.bar_chart(dist_counts)

with col_right:
    st.write("**Fire Size Distribution**")
    size_bins = pd.cut(filtered['GIS_ACRES'], bins=[0, 100, 1000, 10000, 100000, float('inf')])
    size_counts = size_bins.value_counts().sort_index()
    size_counts.index = [str(x) for x in size_counts.index]
    st.bar_chart(size_counts)

# Data table
st.write("### Fire Data Sample")
st.dataframe(filtered[['FIRE_NAME', 'ALARM_DATE', 'GIS_ACRES', 'dist_to_line_miles', 'nearest_line_kV']].head(20))
