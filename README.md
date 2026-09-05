# Diabetes Risk Prediction System

An end-to-end machine learning project that predicts one of three diabetes-risk classes from health and lifestyle indicators:

- `0` - No diabetes
- `1` - Pre-diabetes
- `2` - Diabetes

The project includes a Streamlit user interface for entering patient indicators and a FastAPI service that loads the trained model and serves predictions.

## Features

- Interactive Streamlit form for collecting health indicators
- FastAPI prediction endpoint with Pydantic request validation
- Saved scikit-learn model loaded from `models/model.pkl`
- Categorical input mapping from the UI to the numeric feature format used by the model
- Exploratory analysis and model-building notebooks
- DVC-tracked new-data sample
- Docker configuration for running the API service

## Project Structure

```text
.
├── api/
│   └── main_api.py                 # FastAPI application
├── data/
│   ├── new_data/                   # DVC-tracked sample data
│   └── raw_data/                   # BRFSS diabetes datasets
├── models/
│   └── model.pkl                   # Trained model used by the API
├── notebooks/
│   ├── EDA.ipynb                   # Exploratory data analysis
│   └── build_model.ipynb           # Model development
├── src/
│   ├── config.py                   # Project paths
│   └── mapping.py                  # UI-to-model feature mapping
├── app.py                          # Streamlit frontend
├── Dockerfile
├── requirements.txt
└── README.md
```

## Tech Stack

Python, pandas, scikit-learn, FastAPI, Uvicorn, Streamlit, MLflow, DVC, Docker, matplotlib, and seaborn.

## Setup

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

macOS/Linux:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

The API expects `models/model.pkl` to exist. If the model or DVC-managed data is not present in your checkout, restore the required project artifacts before running the application.

## Run Locally

The Streamlit frontend calls the API, so start both services in separate terminals from the project root.

Terminal 1 - start the API:

```bash
uvicorn api.main_api:app --reload --host 127.0.0.1 --port 8000
```

Terminal 2 - start the Streamlit app:

```bash
streamlit run app.py
```


## API Usage

The endpoint accepts these numeric features:

`HighBP`, `HighChol`, `CholCheck`, `BMI`, `Smoker`, `Stroke`, `HeartDiseaseorAttack`, `PhysActivity`, `Fruits`, `Veggies`, `HvyAlcoholConsump`, `AnyHealthcare`, `NoDocbcCost`, `GenHlth`, `MentHlth`, `PhysHlth`, `DiffWalk`, `Sex`, and `Age`.

The UI converts friendly selections into the encoded values expected by the model. In particular, `GenHlth` is encoded from 1 (excellent) to 5 (poor), and `Age` is represented by the dataset's age group encoding.

## Run with Docker

Build and start the API container:

```bash
docker build -t diabetes-risk-api .
docker run --rm -p 8000:8000 diabetes-risk-api
```

The container exposes the FastAPI service at `http://localhost:8000`. The current Docker configuration runs the API only; run Streamlit separately if you want the web interface.

## Data and Model Development

The project uses diabetes health-indicator data based on the Behavioral Risk Factor Surveillance System (BRFSS) dataset. Raw datasets are stored under `data/raw_data/`, while the sample in `data/new_data/` is tracked with DVC. Use `notebooks/EDA.ipynb` for exploration and `notebooks/build_model.ipynb` for model development.










