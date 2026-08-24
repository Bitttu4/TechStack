# TechStack Future Tasks

## Completed Through ML

- [x] Raw data exploration and validation
- [x] Water-quality standardization and master dataset
- [x] Weather standardization as a separate master dataset
- [x] Model-data filtering and feature selection
- [x] Merged data-preparation and ML notebook
- [x] Three dissolved-oxygen regression models trained
- [x] Chronological holdout evaluation and model comparison
- [x] Best model pipeline, metadata, predictions, metrics, and figures saved

## ML Handoff Result

- Target: `dissolved_oxygen`
- Features: `state`, `station_name`, `year`
- Evaluation: train on years before 2020; test on 2020
- Models compared: Linear Regression, Random Forest, Gradient Boosting
- Selected model: Linear Regression
- Test MAE: `0.4878`
- Test RMSE: `0.6049`
- Test R2: `0.7300`

The complete workflow is in `notebooks/01_data_preparation_and_ml.ipynb`. The model comparison is saved in `data/processed/model_comparison.csv`, and the primary model is `models/best_water_quality_model.joblib`.

## Remaining Team Tasks

1. Validate the selected model on additional unseen periods or stations.
2. Review model robustness and leakage assumptions with the ML team.
3. Integrate weather only after historical date compatibility is established.
4. Integrate the simulated IoT pipeline for demonstration/inference inputs.
5. Build IoT/n8n integration.
6. Build DSS and risk logic.
7. Build CLI integration.
8. Complete final system testing.

## Scope Constraints

- Do not include satellite in the initial ML model. Sentinel-2 features are a future enhancement only.
- Synthetic IoT readings are simulation data, not historical ground truth.
- `RS_Session_255_AU_90.2.csv` has no year field; its year remains unknown and those rows are excluded from chronological ML training.
- Weather and historical water-quality records were not blindly merged because date compatibility has not been established.
