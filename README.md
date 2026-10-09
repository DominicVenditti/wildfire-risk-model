# Wildfire Risk Prediction - Transfer Learning with Spatial Validation

Predicting wildfire risk from weather + geospatial features, using transfer
learning and honest spatial block cross-validation.

## Headline result
- Baseline XGBoost ROC-AUC: 0.660
- Transfer-learned model ROC-AUC: 0.987
- Validated with spatial block CV (not random CV)

## Pipeline
ingestion -> feature engineering -> baseline -> transfer learning -> spatial CV -> Monte Carlo ROI

## Repo structure
- `data/` data + provenance
- `notebooks/` step-by-step analysis
- `src/` reusable scripts
- `models/` trained artifacts
- `results/` figures + metrics
- `dashboards/` Power BI assets
- `docs/` writeups
- `paper/` the paper (pdf + tex)

## How to reproduce
1. `pip install -r requirements.txt`
2. data steps
3. `python src/train.py`

## Paper
See `paper/wildfire_paper.pdf`.

## Contact
Dominic O. Venditti
