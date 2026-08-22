# TechStack — ML Team Task Note

## For: Ruchi
## Responsibility: ML Model Development + Evaluation
## Repository: `https://github.com/Bitttu4/TechStack`

---

# 1. Why this note exists

This note explains the ML portion of the TechStack project from the point where the data-preparation work is handed over to you.

The previous stage is responsible for:

```text
Raw Data
   ↓
Data Exploration
   ↓
Cleaning / Standardization
   ↓
Master Dataset
   ↓
Model-Data Filtering
   ↓
Feature Selection
```

Your work starts **after this point**.

Your job is to take the prepared model-ready data, build and evaluate the ML forecasting side, and leave the project ready for later DSS and CLI integration.

You are **not expected to build the CLI** in this phase.

---

# 2. Final project direction

Initial version:

```text
Historical Water-Quality Data
             +
        Weather Data
             +
          IoT Data
             ↓
          ML Model
             ↓
    Future Water-Quality Prediction
             ↓
            DSS
             ↓
       Risk / Early Warning
             ↓
            CLI
```

## Important scope decision

**Satellite data is NOT part of the initial ML model.**

Sentinel-2 / spectral features are a future enhancement.

Do not add satellite features to the first model. A later version can compare the initial model against an enhanced model with satellite features.

---

# 3. What you receive from the previous stage

Expected processed files:

```text
data/processed/
├── water_quality_master.csv
├── weather_master.csv
└── model_dataset.csv
```

The main input for your ML work is:

```text
data/processed/model_dataset.csv
```

The previous notebook should also document:

- what was cleaned
- what was filtered
- what features were selected
- what the target represents
- unresolved data-quality issues

Do not bypass the preparation stage unless you find a genuine problem.

---

# 4. Clone the repository

Open PowerShell / Terminal and choose your GitHub projects folder.

Example:

```powershell
cd "C:\Users\<YOUR_NAME>\Desktop\Github"
```

Clone:

```powershell
git clone https://github.com/Bitttu4/TechStack.git
```

Enter the repository:

```powershell
cd TechStack
```

Check:

```powershell
git status
git branch
```

---

# 5. Create your own branch

Do not develop directly on `main`.

```powershell
git checkout -b ml-development
```

Verify:

```powershell
git branch
```

Expected:

```text
* ml-development
  main
```

---

# 6. Python environment

From the repository root:

```powershell
python -m venv .venv
```

Activate:

```powershell
.\.venv\Scripts\Activate.ps1
```

Check Python:

```powershell
python --version
```

Install the basic data/ML tools:

```powershell
python -m pip install --upgrade pip
python -m pip install pandas numpy matplotlib seaborn scikit-learn jupyter ipykernel joblib
```

Do not install deep-learning frameworks unless the dataset actually justifies an LSTM/deep-learning experiment.

---

# 7. Create/open the ML notebook

The ML notebook should be:

```text
notebooks/
└── 03_model_training_and_evaluation.ipynb
```

Start Jupyter:

```powershell
python -m notebook
```

Open:

```text
notebooks/03_model_training_and_evaluation.ipynb
```

Do not modify the data-preparation notebook unless a real data issue is found.

---

# 8. Inspect the model-ready dataset first

Start with:

```python
from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path.cwd().parent

MODEL_DATA = ROOT / "data" / "processed" / "model_dataset.csv"

df = pd.read_csv(MODEL_DATA)

print("Shape:", df.shape)
display(df.head())
print(df.dtypes)
display(df.isna().sum())
```

Also inspect:

```python
display(df.describe(include="all").T)
```

The first goal is simply to confirm that the handed-off data is actually usable.

---

# 9. Identify the target

The project is a water-quality forecasting system.

Use only a target that actually exists in the prepared dataset.

Possible targets may include:

- Dissolved Oxygen
- BOD
- Fecal Coliform

The final choice must be based on the actual prepared data and the documentation from the previous stage.

Document:

```text
Target:
Why this target was selected:
What one prediction represents:
Prediction/forecasting setup:
```

Do not invent targets.

---

# 10. Regression vs classification

If the target is a continuous numerical value such as:

```text
DO = 6.4
BOD = 4.8
```

then this is a regression problem.

The ML model should predict a numerical value.

Risk classes such as:

```text
Low
Medium
High
```

can be produced later by DSS logic and thresholds. Do not force the ML task into classification without a reason.

---

# 11. Use a forecasting-aware data split

This is a forecasting project.

Do not blindly use a random shuffled split if a reliable time/year field exists.

Prefer a time-aware approach such as:

```text
Older observations
        ↓
      TRAIN

Newer observations
        ↓
      TEST
```

This reduces the risk of training on future information when evaluating future prediction.

If the available dataset does not support a genuine forecasting split, document that limitation clearly.

---

# 12. Establish a baseline

Before advanced models, create a simple baseline.

The baseline answers:

> How much performance can we get without a complex ML model?

The exact baseline can depend on the actual dataset.

Do not skip the baseline.

---

# 13. Candidate models

Start with practical tabular models.

Suggested order:

### Model 1 — Baseline
A simple baseline appropriate for the target.

### Model 2 — Random Forest
Useful for nonlinear tabular relationships.

### Model 3 — Gradient Boosting / XGBoost
Use XGBoost only if it is justified and the dependency is convenient.

### Model 4 — Optional LSTM / deep learning
Only consider this if enough useful sequential data exists.

Do not use LSTM just because it sounds more advanced.

The objective is:

> **Choose the approach that gives the most reliable performance on unseen data.**

---

# 14. Evaluation

For numerical prediction, use appropriate regression metrics.

### MAE
Mean Absolute Error.

Lower is better.

### RMSE
Root Mean Squared Error.

Lower is better.

### R²
Coefficient of determination.

Higher is generally better.

Create a real comparison table:

```text
Model              MAE     RMSE     R²
-----------------------------------------
Baseline            ...
Random Forest       ...
Gradient Boosting   ...
XGBoost             ...
```

Use actual experimental results only.

---

# 15. How to select the final model

Do not choose the model using training performance alone.

Consider:

- MAE
- RMSE
- R²
- performance on unseen data
- stability across validation periods
- training complexity
- inference speed
- explainability
- suitability for later CLI deployment

Document the selection:

```text
Selected model:
Reason:
Validation method:
MAE:
RMSE:
R²:
Important features:
Known limitations:
```

---

# 16. Feature importance / interpretation

Inspect how the selected model uses the available features.

For suitable tree-based models, feature importance can be useful.

Use this primarily to:

- understand the model
- check whether selected features make sense
- identify unexpected behaviour
- provide information for later documentation

Do not remove a feature automatically because it has low importance in one model.

---

# 17. Avoid data leakage

Do not use information that would only be available after the prediction time.

For example, if predicting a future water-quality value, do not accidentally include future observations of the same target or other derived values that reveal the future target.

Keep preprocessing and inference inputs consistent.

---

# 18. Save the trained model

Once the final model is selected, save it using `joblib`.

Example:

```python
import joblib

joblib.dump(
    model,
    "model.joblib"
)
```

Prefer a model artifact directory:

```text
models/
└── water_quality_model.joblib
```

If preprocessing is required, save that as well.

---

# 19. Save model metadata

The CLI/integration side will need more than the model binary.

Record:

```text
model name
target
feature list
training data version
validation method
evaluation metrics
model version
```

A practical metadata file can be:

```text
models/model_metadata.json
```

---

# 20. Recommended notebook structure

Keep `03_model_training_and_evaluation.ipynb` organized as:

```text
1. Imports
2. Load model-ready dataset
3. Dataset inspection
4. Target definition
5. Feature/target split
6. Time-aware train/test split
7. Baseline
8. Random Forest
9. Gradient Boosting / XGBoost
10. Evaluation comparison
11. Feature importance
12. Final model selection
13. Save model
14. Save metadata
15. Final summary
```

The notebook should be understandable to another teammate without needing a verbal explanation.

---

# 21. Do NOT do these things in the ML phase

Do not:

- add satellite features to the initial model
- invent missing years
- fabricate target labels
- treat synthetic IoT data as real historical ground truth
- randomly shuffle time-series data without justification
- choose a model only because it is more advanced
- report training scores as final results
- overwrite raw data
- unnecessarily rewrite the simulator
- build the CLI in this branch
- build DSS logic here
- build the dashboard here

---

# 22. Expected output

Your work should eventually create something close to:

```text
TechStack/
├── data/
│   ├── raw/
│   └── processed/
│       ├── water_quality_master.csv
│       ├── weather_master.csv
│       └── model_dataset.csv
│
├── notebooks/
│   ├── 01_data_exploration_and_cleaning.ipynb
│   ├── 02_model_data_preparation_and_feature_selection.ipynb
│   └── 03_model_training_and_evaluation.ipynb
│
└── models/
    ├── water_quality_model.joblib
    └── model_metadata.json
```

Do not create unnecessary files.

---

# 23. Handoff to CLI integration

Once the ML model is selected and saved, your ML work reaches the handoff point.

The CLI developer will need:

```text
Model file
Feature list
Expected input format
Target meaning
Preprocessing steps
Evaluation metrics
Model version
```

You do not need to implement the CLI.

The CLI side will later load the saved model and use the same expected preprocessing/input structure.

---

# 24. Git workflow

After a logical milestone:

```powershell
git status
```

Review the changes.

Commit:

```powershell
git add .
git commit -m "Add ML training and model evaluation"
```

Push your branch:

```powershell
git push -u origin ml-development
```

Do not push directly to `main`.

When the ML work is ready, tell Aarya that the branch is ready for review/merge.

---

# 25. Handoff message

When finished, provide:

```text
ML WORK COMPLETE

Target:
Selected model:

Validation method:

MAE:
RMSE:
R²:

Final features:
1.
2.
3.

Saved model:
models/...

Metadata:
models/...

Known limitations:
...

Branch:
ml-development
```

---

# 26. Your exact responsibility

Your responsibility is:

**Prepared data → ML experimentation → model evaluation → select the most reliable model → save model + metadata → hand it over for DSS/CLI integration.**

After this point, the work moves to the integration side.
