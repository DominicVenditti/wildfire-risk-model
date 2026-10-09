# California Wildfire Prediction System v6.0
## Complete Package for Power BI

**Generated:** 2026-10-03 18:39:49

---

## FOLDER STRUCTURE

### 01_Cleaned_Data/
- `cleaned_fire_weather_data.csv` - Main dataset with all fire/weather matches
- `test_set_with_predictions.csv` - Test set with model predictions
- `wildland_only_data.csv` - Filtered to CAL FIRE scope (excludes urban cores)
- `feature_importance.csv` - Model feature rankings

### 02_Models/
- `wildfire_risk_model.pkl` - Trained XGBoost model
- `production_calibrator.pkl` - Isotonic calibration model
- `iberian_model.pkl` - Iberian transfer learning model
- `model_config.json` - Model configuration and metadata

### 03_PowerBI_Ready/
- `current_risk.csv` - Current day risk by location
- `7day_outlook.csv` - 7-day forecast time series
- `7day_summary.csv` - Daily aggregated summary
- `enhanced_7day_outlook.csv` - Full forecast with alert flags
- `locations_reference.csv` - Location metadata
- `date_dimension.csv` - Date table for Power BI time intelligence

### 04_Documentation/
- This README
- `metrics_summary.json` - All performance metrics
- `power_bi_setup_guide.md` - Step-by-step Power BI instructions

---

## KEY METRICS

- **AUC-ROC:** 0.9862
- **Precision:** 85.7%
- **Recall:** 94.7%
- **F2-Score:** 0.928
- **Wildland Coverage:** 71.6%

---

## POWER BI SETUP

1. Open Power BI Desktop
2. Click **Get Data** → **Text/CSV**
3. Import files from `03_PowerBI_Ready/`
4. Create relationships between tables (date, location)
5. Build visualizations using the guide in Documentation folder

---

## REFRESH SCHEDULE

- **Daily:** 6:00 AM PST
- **Model Retraining:** Monthly
- **Drift Check:** Weekly

---

## CONTACT

For questions about this model, contact the development team.