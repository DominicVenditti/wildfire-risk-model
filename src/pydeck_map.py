import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("🔥 California Wildfire Risk Analysis")

# Load data
@st.cache_data
def load_data():
    fires = pd.read_csv("/Users/nickvenditti/Desktop/Californai Wildfire Project/Data/fires_all_with_transmission_proximity.csv")
    fires["ALARM_DATE"] = pd.to_datetime(fires["ALARM_DATE"])
    return fires

fires = load_data()

# Sidebar filters
st.sidebar.header("Filter Options")

# Date range filter
min_date = fires["ALARM_DATE"].min().date()
max_date = fires["ALARM_DATE"].max().date()

date_range = st.sidebar.date_input(
    "Select date range",
    value=[min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Apply filters
if len(date_range) == 2:
    filtered = fires[
        (fires["ALARM_DATE"].dt.date >= date_range[0]) & 
        (fires["ALARM_DATE"].dt.date <= date_range[1])
    ].copy()
else:
    filtered = fires.copy()

st.sidebar.write(f"Showing **{len(filtered):,}** fires")

# Color code based on distance to power line
def get_color(dist):
    if dist < 1:
        return [255, 0, 0]  # Red - near power lines
    elif dist < 3:
        return [255, 165, 0]  # Orange - moderate distance
    else:
        return [255, 255, 0]  # Yellow - far from lines

filtered["color"] = filtered["dist_to_line_miles"].apply(get_color)

# Prepare data for PyDeck
filtered["lon"] = filtered["centroid_lon"]
filtered["lat"] = filtered["centroid_lat"]

# Create PyDeck layer
layer = pdk.Layer(
    "ScatterplotLayer",
    data=filtered,
    get_position=["lon", "lat"],
    get_color="color",
    get_radius="GIS_ACRES",
    radius_scale=10,
    radius_min_pixels=2,
    radius_max_pixels=50,
    pickable=True,
)

# Set view
view_state = pdk.ViewState(
    latitude=36.7783,
    longitude=-119.4179,
    zoom=6,
    pitch=0
)

# Create deck with tooltip
deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={
        "html": "<b>Fire:</b> {FIRE_NAME}<br>"
                "<b>Date:</b> {ALARM_DATE}<br>"
                "<b>Size:</b> {GIS_ACRES:,.0f} acres<br>"
                "<b>Distance to line:</b> {dist_to_line_miles:.2f} miles<br>"
                "<b>Nearest line:</b> {nearest_line_kV}kV",
        "style": {"backgroundColor": "steelblue", "color": "white"}
    }
)

st.write(f"### Fire Map: {date_range[0]} to {date_range[1]}")

# Display map
st.pydeck_chart(deck)

# Legend
st.write("**Legend:**")
col1, col2, col3 = st.columns(3)
col1.markdown("🔴 **Red:** Near power lines (<1 mi)")
col2.markdown("🟠 **Orange:** Moderate distance (1-3 mi)")
col3.markdown("🟡 **Yellow:** Far from lines (>3 mi)")

# Statistics
st.write("### Statistics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Fires", f"{len(filtered):,}")
col2.metric("Avg Fire Size", f"{filtered['GIS_ACRES'].mean():,.0f} acres")
col3.metric("Avg Distance to Line", f"{filtered['dist_to_line_miles'].mean():.2f} miles")
col4.metric("Near Power Lines", f"{(filtered['dist_to_line_miles'] < 1).sum()}")

# Sample data
st.write("### Fire Data Sample")
st.dataframe(filtered[['FIRE_NAME', 'ALARM_DATE', 'GIS_ACRES', 'dist_to_line_miles', 'nearest_line_kV']].head(20))
