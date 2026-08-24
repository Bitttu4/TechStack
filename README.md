# TechStack

TechStack is a scalable water-quality forecasting platform intended to support multiple rivers. The current implementation is a Ganga River baseline/reference case that demonstrates the complete data-preparation, ML training, evaluation, and artifact-saving workflow.

The long-term architecture is:

```text
Multiple Rivers
      -> Standardized Data Pipeline
      -> Feature Engineering
      -> ML Models
      -> Water-Quality Forecasting
```

The current prototype should not be interpreted as a model trained on multiple rivers.

## Repository Structure

```text
data/raw/                         Original water-quality and weather files
data/processed/                   Clean masters, model data, metrics, predictions
notebooks/01_data_preparation_and_ml.ipynb
                                  Merged preparation, ML, evaluation, and handoff notebook
models/                           Saved regression pipelines and metadata
images/                           Notebook-generated visualization outputs
simulator/                        Synthetic IoT demonstration pipeline
```

## Data and ML Workflow

The merged notebook loads the prepared water-quality and weather masters, validates the data, prepares a chronological train/test split, and trains three dissolved-oxygen regression models:

- Linear Regression
- Random Forest
- Gradient Boosting

The current features are `state`, `station_name`, and `year`. The latest observed year is held out for evaluation. Model metrics, predictions, metadata, and fitted pipelines are saved under `data/processed/` and `models/`.

The notebook also produces visualizations covering data quality, parameter distributions, correlations, temporal trends, station/state comparisons, train/test distributions, model predictions, model comparison, and residual diagnostics. Each figure is displayed in notebook output and saved as a PNG under `images/`.

## Current Baseline Result

The current Ganga baseline selects Linear Regression using chronological holdout RMSE:

```text
MAE:  0.4878
RMSE: 0.6049
R2:   0.7300
```

These results describe this baseline dataset only and are not universal claims for other rivers.

## Running the Notebook

From the repository root, open the notebook with Jupyter and run all cells from a fresh kernel:

```powershell
python -m jupyter notebook notebooks/01_data_preparation_and_ml.ipynb
```

Satellite data is intentionally excluded from the initial ML model. Synthetic IoT readings are simulation data and are not treated as historical ground truth.
