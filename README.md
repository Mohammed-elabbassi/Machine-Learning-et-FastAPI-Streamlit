

# Prédiction de la mortalité COVID-19 avec Machine Learning et FastAPI + Streamlit

Ce projet a pour objectif de prévoir si un patient atteint du COVID-19 est vivant ou mort,
 en se basant sur ses données médicales, grâce à l'emploi d'un modèle « Random Forest », 
 d'une « API FastAPI », d'une « base de données Cassandra » pour le stockage des informations, 
 et d'une interface utilisateur « Streamlit ».

## Structure du projet

covid_prediction_project/

1 model/# data_finale
a covid_data_cleaned_01.csv # Données nettoyées
b covid_model.pkl # Modèle entraîné
c model_columns.pkl # Liste des colonnes du modèle

2 api/ main.py # API FastAPI

3 streamlit_app.py # Interface utilisateur Streamlit
4 Cassandra

## Installer les dépendances

pip install -r requirements.txt

## Entraînement du modèle

-->#data_finale

## Lancer l'API FastAPI

cd api
uvicorn main:app --reload

## Lancer l’interface Streamlit

cd ui
streamlit run streamlit_app.py

## Exemple de requête API
POST /predict

{
  "age": 65,
  "intubed": 0,
  "icu": 0,
  "pneumonia": 1,
  "contact_other_covid": 1,
  "diabetes": 1,
  "hypertension": 1,
  "obesity": 0,
  "tobacco": 0,
  "other_disease": 0,
  "renal_chronic": 0,
  "cardiovascular": 0,
  "inmsupr": 0,
  "copd": 0,
  "patient_type_2": 1
}

## Table Cassandra (Keyspace covid_prediction)
CREATE TABLE predictions (
    id UUID PRIMARY KEY,
    age int,
    intubed int,
    icu int,
    pneumonia int,
    contact_other_covid int,
    diabetes int,
    hypertension int,
    obesity int,
    tobacco int,
    other_disease int,
    renal_chronic int,
    cardiovascular int,
    inmsupr int,
    copd int,
    patient_type_2 int,
    prediction int,
    resultat text
);

##Interprétation des Codes Numériques
🎯 Colonnes avec significations spécifiques :
intubed, icu

97 → Donnée manquante → Remplacer par np.nan

1 → Non / Négatif → Convertir en 0

0 → Oui / Positif → Convertir en 1

pneumonia

1 → Non → Convertir en 0

0 → Oui → Convertir en 1

contact_other_covid

99 → Inconnu / Manquant → Remplacer par np.nan

1 → Non → Convertir en 0

diabetes, hypertension, obesity, tobacco, other_disease, renal_chronic, cardiovascular, inmsupr, copd

1 → Non → Convertir en 0

0 → Oui → Convertir en 1

patient_type_2

False → Patient ambulatoire → Convertir en 0

True → Hospitalisé → Convertir en 1



## Liste des variables et leur signification
age : Âge du patient (en années)

intubed : Le patient est-il intubé ? (1 = oui, 0 = non)

icu : Le patient est-il en unité de soins intensifs ? (1 = oui, 0 = non)

pneumonia : Le patient a-t-il une pneumonie ? (1 = oui, 0 = non)

contact_other_covid : Contact avec un autre cas COVID (1 = oui, 0 = non)

diabetes : Le patient est-il diabétique ? (1 = oui, 0 = non)

hypertension : Le patient a-t-il de l'hypertension ? (1 = oui, 0 = non)

obesity : Le patient est-il obèse ? (1 = oui, 0 = non)

tobacco : Le patient est-il fumeur ? (1 = oui, 0 = non)

other_disease : Autres maladies présentes ? (1 = oui, 0 = non)

renal_chronic : Maladie rénale chronique ? (1 = oui, 0 = non)

cardiovascular : Maladies cardiovasculaires ? (1 = oui, 0 = non)

inmsupr : Le patient est-il immunodéprimé ? (1 = oui, 0 = non)

copd : Maladie pulmonaire obstructive chronique ? (1 = oui, 0 = non)

patient_type_2 : Type de patient :

0 = ambulatoire

1 = hospitalisé




## ✉️ Contact
Pour toute question ou amélioration, tu peux me contacter via [med.elabbassi00@gmail.com].
