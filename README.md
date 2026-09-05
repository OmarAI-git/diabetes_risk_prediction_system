# Diabetes Risk Prediction System

An end-to-end machine learning project that predicts one of three diabetes-risk classes from health and lifestyle indicators:

- `0` - No diabetes
- `1` - Pre-diabetes
- `2` - Diabetes

The project includes a Streamlit user interface for entering patient indicators and a FastAPI service that loads the trained model and serves predictions.

## Concepts Demonstrated

This project demonstrates the complete path from health data to a usable machine learning application.

### 1. Exploratory Data Analysis

The project begins by exploring diabetes health-indicator data to understand its structure, distributions, relationships, and potential data-quality issues. The analysis is documented in `notebooks/EDA.ipynb` and uses tables and visualizations to support modeling decisions.

### 2. Supervised Machine Learning

This is a supervised multiclass classification problem. The model learns from labeled health and lifestyle records and predicts one of three target classes:

- `0` - No diabetes
- `1` - Pre-diabetes
- `2` - Diabetes

Model development and experimentation are documented in `notebooks/build_model.ipynb`.

### 3. Feature Preparation and Encoding

The model requires numeric features, while the Streamlit interface uses readable choices such as “Yes”, “No”, “excellent”, and “poor”. The mapping layer in `src/mapping.py` converts these user-friendly values into the numeric representation expected by the trained model. This includes binary encoding, general-health encoding, and age-group encoding.

### 4. Model Serialization and Inference

After training, the model is serialized as `models/model.pkl`. The FastAPI service loads this artifact when it starts, receives validated feature values, creates a pandas DataFrame, and returns a prediction during inference.

### 5. API and Frontend Integration

The application separates the user experience from the prediction service:

- **Streamlit** provides the interactive form.
- **FastAPI** exposes the `/predict` endpoint.
- **HTTP requests** connect the frontend to the backend.
- **Pydantic** validates incoming API data.

This separation makes the model available both through the web interface and as a reusable API.

### 6. Reproducible Data and Experimentation

The project introduces practical MLOps concepts by tracking data with DVC and storing MLflow artifacts for experiment and model management. The goal is to keep data, experiments, and model files organized and reproducible as the project evolves.

### 7. Containerization

The included Dockerfile packages the FastAPI service with its Python dependencies. This provides a consistent environment for running the prediction API locally or deploying it to another system.

## Tools and Technologies

### Programming and Data Science

- **Python** - Main programming language
- **pandas** - Data loading, tabular transformation, and inference input preparation
- **NumPy** - Numerical computing support
- **scikit-learn** - Machine learning model development and prediction
- **imbalanced-learn** - Tools for handling imbalanced classification data

### Analysis and Visualization

- **Jupyter Notebook** - Interactive analysis and model experimentation
- **matplotlib** - General-purpose data visualization
- **seaborn** - Statistical and exploratory visualizations

### Application and API

- **Streamlit** - Interactive frontend for collecting user inputs
- **FastAPI** - REST API framework for serving predictions
- **Uvicorn** - ASGI server used to run the FastAPI application
- **Pydantic** - Request schema definition and validation
- **Requests** - Communication between the Streamlit frontend and API

### MLOps and Deployment

- **MLflow** - Experiment and model artifact management
- **DVC** - Version control for data files
- **Docker** - Containerization of the prediction API
- **virtualenv / venv** - Isolated Python environment for dependencies

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










