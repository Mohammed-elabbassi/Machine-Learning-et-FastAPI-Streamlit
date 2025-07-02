


from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from cassandra.cluster import Cluster
import uuid

# Charger le modèle et les colonnes
model = joblib.load("E:\\data mining\\tous\\covid_model.pkl")
model_columns = joblib.load("E:\\data mining\\tous\\model_columns.pkl")

# Connexion à Cassandra 
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('covid_prediction')


app = FastAPI()

class CovidPatient(BaseModel):
    age: int
    intubed: int
    icu: int
    pneumonia: int
    contact_other_covid: int
    diabetes: int
    hypertension: int
    obesity: int
    tobacco: int
    other_disease: int
    renal_chronic: int
    cardiovascular: int
    inmsupr: int
    copd: int
    patient_type_2: int

@app.post("/predict")
def predict_death(data: CovidPatient):
    input_data = [getattr(data, col) for col in model_columns]
    prediction = model.predict([input_data])[0]
    result = "mort" if prediction == 1 else "vivant"
   
    session.execute("""
        INSERT INTO predictions (
            id, age, intubed, icu, pneumonia, contact_other_covid,
            diabetes, hypertension, obesity, tobacco, other_disease,
            renal_chronic, cardiovascular, inmsupr, copd, patient_type_2,
            prediction, resultat
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        uuid.uuid4(),
        data.age,
        data.intubed,
        data.icu,
        data.pneumonia,
        data.contact_other_covid,
        data.diabetes,
        data.hypertension,
        data.obesity,
        data.tobacco,
        data.other_disease,
        data.renal_chronic,
        data.cardiovascular,
        data.inmsupr,
        data.copd,
        data.patient_type_2,
        int(prediction),
        result
    ))

    return {"prediction": int(prediction), "resultat": result}
