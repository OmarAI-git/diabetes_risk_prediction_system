import pandas as pd
import pickle
from fastapi import FastAPI
from pydantic import BaseModel
from src.config import MODELS, BASE_DIR

app = FastAPI()


# load the model
with open(MODELS/'model.pkl', 'rb') as f:
    model = pickle.load(f)


class PredictionRequest(BaseModel):
    HighBP:int
    HighChol:int
    CholCheck:int
    BMI:int
    Smoker:int
    Stroke:int
    HeartDiseaseorAttack:int
    PhysActivity:int
    Fruits:int
    Veggies:int
    HvyAlcoholConsump:int
    AnyHealthcare:int
    NoDocbcCost:int
    GenHlth:int
    MentHlth:int
    PhysHlth:int
    DiffWalk:int
    Sex:int
    Age:int

@app.get('/')
async def home():
    return {'health': 'OK'}


@app.post('/predict')
async def predict(parameters: PredictionRequest):
    par = pd.DataFrame([parameters.model_dump()])

    result = model.predict(par)

    prediction_value = int(result[0])

    return {'Diabetes Prediction': prediction_value}

