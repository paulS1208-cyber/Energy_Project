# Projet Énergie – Analyse et Visualisation Régionale

Ce projet explore la consommation et la production d'énergie en France par région (2013-2022).  
Il contient des données brutes, nettoyées, des analyses Python et des visualisations Power BI.

## 📂 Contenu du dépôt

| Fichier | Description |
|---------|-------------|
| `BI Projet énergie.pbix` | Rapport Power BI interactif |
| `Code Nettoyage.ipynb` | Notebook Python pour nettoyage et analyse |
| `eco2mix-regional-cons-def.csv` | Données brutes |
| `nrj_nettoye_vf.csv` | Données nettoyées |
| `Population 2018.csv` | Données démographiques régionales |
| `images/` | Graphiques Python et exports Power BI |

---

## 📊 Aperçu Graphiques Python

### Valeurs manquantes
![Valeurs manquantes](images/graph_nan_pourcent.png)

### Matrice de corrélation
![Matrice de corrélation](images/graph_correlation.png)

### Consommation par région
![Consommation](images/graph_boxplot_conso.png)

### Énergie solaire par région
![Solaire](images/graph_boxplot_solaire.png)

### Bioénergies par région
![Bioénergies](images/graph_boxplot_bio.png)

---

## 📈 Aperçu Visualisations Power BI

Les 13 pages exportées du rapport Power BI sont disponibles dans `images/BI Graphs/` :

![Page 1](images/BI%20Graphs/BI%20Projet%20énergie_page-0001.jpg)
![Page 2](images/BI%20Graphs/BI%20Projet%20énergie_page-0002.jpg)
![Page 3](images/BI%20Graphs/BI%20Projet%20énergie_page-0003.jpg)

---

## Objectifs

- Analyser la consommation et la production énergétique régionale en France.
- Croiser les données de consommation avec la population pour identifier des tendances.
- Détecter une dépendance de la France à l'énergie nucléaire. 
- Analyser l'évolution des énergies renouvelables.
- Visualiser les résultats via Power BI.