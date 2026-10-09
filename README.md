# Wildfire Risk Prediction - Transfer Learning with Spatial Validation

Predicting wildfire risk from weather + geospatial features, using transfer
learning and honest spatial block cross-validation.

## Headline result
- Baseline XGBoost ROC-AUC: 0.660
- Transfer-learned model ROC-AUC: 0.987
- Validated with spatial block CV (not random CV)


## Results

| Metric | Value |
|---|---|
| ROC-AUC | 0.986 |
| Recall | 0.947 |
| Precision | 0.857 |
| F2 | 0.928 |
| Decision threshold | 0.41 |
| Baseline XGBoost ROC-AUC | 0.660 |

Validated with spatial block cross-validation. Probabilities calibrated;
uncertainty quantified via 100,000-iteration Monte Carlo.


## Economic Impact

Translating model performance into dollars (baseline: ~$16.26B/yr in California
wildfire costs):

| Metric | Value |
|---|---|
| Dataset | 48,756 weather records (34,929 wildland), 11 features |
| System investment | $530K / yr |
| Projected annual savings | $971.6M |
| Net benefit | $971.1M / yr |
| Payback period | under 1 month |

Projected outcomes: 88 fewer large fires per year, 87% early-detection rate,
35% reduction in fire size, 50-100 lives saved and ~500K acres preserved annually.

*Note: the headline ROI is large because savings are measured against the total
baseline cost base, not the project budget.*

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
