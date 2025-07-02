
import streamlit as st 
import requests

st.title("🧪 Prédiction de la mortalité COVID")


model_columns = [
    "age", "intubed", "icu", "pneumonia", "contact_other_covid", "diabetes",
    "hypertension", "obesity", "tobacco", "other_disease", "renal_chronic",
    "cardiovascular", "inmsupr", "copd", "patient_type_2"
]

inputs = {}
cols_per_row = 3

for i in range(0, len(model_columns), cols_per_row):
    cols = st.columns(cols_per_row)
    for j in range(cols_per_row):
        if i + j < len(model_columns):
            col_name = model_columns[i + j]
            with cols[j]:
                value = st.number_input(f"{col_name} :", min_value=0, max_value=110, step=1)
                inputs[col_name] = value

# Bouton de prédiction
if st.button("Prédire"):
    # Appel à l'API FastAPI
    response = requests.post("http://localhost:8000/predict", json=inputs)

    if response.status_code == 200:
        result = response.json()
        label = "🔴 Mort" if result["prediction"] == 1 else "🟢 Vivant"
        st.success(f"Résultat de la prédiction : {label}")
    else:
        st.error("Erreur lors de la requête à l'API.")

