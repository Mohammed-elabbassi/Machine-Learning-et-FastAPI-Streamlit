
# 📊 Analyse Exploratoire des Données (EDA)

Ce document décrit l’analyse exploratoire réalisée sur les données cliniques liées au COVID-19.

---

##  Objectifs de l’EDA

- Comprendre les distributions des variables
- Identifier les valeurs manquantes ou aberrantes
- Étudier les corrélations entre variables
- Visualiser les liens entre les variables explicatives et la cible `died`

---

##  Prétraitement appliqué

- Remplacement des valeurs `97`, `99` par `NaN`
- Remplissage des `NaN` par la "valeur la plus fréquente" (`mode`)
- Transformation des colonnes booléennes (`True/False` → `1/0`)
- Normalisation des variables binaires pour une cohérence totale

---

##  Étapes de l’EDA

### 1. Informations générales
- Dimensions du dataset
- Types de données
- Statistiques descriptives de base

### 2. Visualisation des valeurs manquantes
- Carte de chaleur (`heatmap`) des NaN

### 3. Distribution de l’âge
- Histogramme avec `kde=True`

### 4. Boxplot de l’âge selon la cible `died`
- Visualisation de l’effet de l’âge sur la mortalité

### 5. Distribution des variables binaires
- Diagrammes en barres  pour chaque variable 0/1

### 6. Matrice de corrélation
- Corrélation visuelle entre toutes les variables numériques


### 7. Taux de mortalité par tranche d’âge
- Regroupement par classes d’âge et visualisation du taux moyen de décès

---

## 🧠 Interprétations principales

- La mortalité augmente avec l’âge
- Certaines comorbidités (diabète, hypertension, obésité) sont liées à une mortalité plus élevée
- L’intubation, les soins intensifs (`icu`) et la pneumonie sont des indicateurs de gravité

---


