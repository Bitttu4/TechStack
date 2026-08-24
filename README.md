# TechStack

AI-powered platform for water-quality forecasting. The repository currently contains the complete data-preparation and initial ML workflow.

## Current Structure

```text
data/raw/                         Original water-quality and weather files
data/processed/                   Clean masters, model data, metrics, predictions
notebooks/01_data_preparation_and_ml.ipynb
                                  Merged preparation, training, evaluation, and handoff
models/                           Saved regression pipelines and metadata
images/                           Notebook figures
simulator/                        Synthetic IoT demo pipeline
```

## ML Workflow

The merged notebook trains and compares Linear Regression, Random Forest, and Gradient Boosting models for dissolved oxygen. It uses a chronological holdout, saving the model comparison, predictions, model metadata, fitted pipelines, and evaluation figures.

The current best model is selected by lowest chronological holdout RMSE. Satellite data is intentionally excluded from the initial ML model, and synthetic IoT readings are not treated as historical ground truth.

Run the notebook from the repository root with Jupyter, or execute its cells top-to-bottom in `notebooks/01_data_preparation_and_ml.ipynb`.
