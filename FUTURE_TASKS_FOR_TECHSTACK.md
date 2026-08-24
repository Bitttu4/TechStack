# TechStack Future Tasks

## Completed Through Current ML Baseline

- [x] Raw data exploration and validation
- [x] Water-quality standardization and master dataset
- [x] Weather standardization as a separate master dataset
- [x] Model-data filtering and feature selection
- [x] Merged data-preparation and ML notebook
- [x] Three dissolved-oxygen regression models trained
- [x] Chronological holdout evaluation and model comparison
- [x] Best model pipeline, metadata, predictions, and metrics saved
- [x] Data-quality, temporal, station, state, model, and residual visualizations added
- [x] Every notebook visualization displayed in output and saved under `images/`

## Current Baseline Handoff

- Scope: Ganga River reference/baseline implementation
- Target: `dissolved_oxygen`
- Features: `state`, `station_name`, `year`
- Evaluation: train on years before 2020; test on 2020
- Models compared: Linear Regression, Random Forest, Gradient Boosting
- Selected model: Linear Regression
- Test MAE: `0.4878`
- Test RMSE: `0.6049`
- Test R2: `0.7300`

The complete workflow is in `notebooks/01_data_preparation_and_ml.ipynb`. Model comparison is saved in `data/processed/model_comparison.csv`, predictions are saved in `data/processed/best_model_predictions.csv`, and the primary model is `models/best_water_quality_model.joblib`.

These metrics describe the current Ganga baseline only. They do not establish performance across multiple rivers.

## Future Multi-River Roadmap

1. Integrate standardized datasets from additional Indian rivers.
2. Add a river identifier to the shared data schema.
3. Standardize river-specific stations and monitoring records.
4. Develop river-aware feature engineering.
5. Compare generalized models with river-specific models.
6. Validate performance across rivers, stations, and unseen time periods.
7. Expand the supported forecasting targets.
8. Build larger and more consistent historical datasets.

## Remaining Platform Tasks

1. Integrate weather only after historical date compatibility is established.
2. Integrate the simulated IoT pipeline for demonstration and inference inputs.
3. Build IoT/n8n integration.
4. Build DSS and risk logic.
5. Build CLI integration.
6. Complete final system testing.

## Scope Constraints

- Do not include satellite in the initial ML model. Sentinel-2 features are a future enhancement only.
- Synthetic IoT readings are simulation data, not historical ground truth.
- `RS_Session_255_AU_90.2.csv` has no year field; its year remains unknown and those rows are excluded from chronological ML training.
- Weather and historical water-quality records were not blindly merged because date compatibility has not been established.
- Do not claim multi-river model generalization until multiple river datasets have been standardized and evaluated.
