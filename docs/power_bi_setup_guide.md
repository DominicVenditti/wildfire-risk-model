# Power BI Setup Guide

## Step 1: Import Data
1. Open Power BI Desktop
2. Click **Get Data** → **Text/CSV**
3. Select files from `03_PowerBI_Ready/`:
   - `current_risk.csv`
   - `enhanced_7day_outlook.csv`
   - `date_dimension.csv`
   - `locations_reference.csv`

## Step 2: Create Relationships
- Link `enhanced_7day_outlook[date]` to `date_dimension[date]`
- Link `enhanced_7day_outlook[location_id]` to `locations_reference[name]`

## Step 3: Build Visualizations

### Map Visualization
- **Visual:** Map
- **Latitude:** latitude
- **Longitude:** longitude
- **Color saturation:** risk_score
- **Legend:** alert_flag

### Time Series
- **Visual:** Line chart
- **X-axis:** date
- **Y-axis:** fire_probability
- **Legend:** location_id

### Cards
- **Visual:** Card
- **Fields:** extreme_count, avg_risk, locations_monitored

## Step 4: Add Slicers
- **Date range:** For filtering time period
- **Location:** For filtering specific areas
- **Risk level:** For filtering by severity

## Step 5: Publish
- Click **Publish** to Power BI Service
- Set up scheduled refresh for daily updates