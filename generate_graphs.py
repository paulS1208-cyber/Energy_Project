import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Créer le dossier images dans le même dossier que le script
os.makedirs('images', exist_ok=True)

# Charger le fichier nettoyé
df = pd.read_csv(r'C:\Users\pauls\OneDrive\Documents\Projet Energie\nrj_nettoye_vf.csv')

# 1. Graphique des valeurs manquantes
nan_pourcent = df.isnull().mean() * 100
nan_pourcent[nan_pourcent > 0].sort_values().plot(kind='barh', figsize=(10,6))
plt.title("Pourcentage de valeurs manquantes par colonne")
plt.tight_layout()
plt.savefig('images/graph_nan_pourcent.png')
plt.close()

# 2. Matrice de corrélation
corr_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(20,20))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", center=0, linewidths=0.5)
plt.title("Matrice de corrélation")
plt.tight_layout()
plt.savefig('images/graph_correlation.png')
plt.close()

# 3. Boxplots par région pour la consommation
plt.figure(figsize=(14,6))
sns.boxplot(data=df, x='Région', y='Consommation', hue='Région')
plt.xticks(rotation=45)
plt.title('Consommation en MW par régions de 2013 à 2022')
plt.tight_layout()
plt.savefig('images/graph_boxplot_conso.png')
plt.close()

# 4. Boxplot énergie solaire
plt.figure(figsize=(14,6))
sns.boxplot(data=df, x='Région', y='Solaire', hue='Région')
plt.xticks(rotation=45)
plt.title('Production en MW d\'énergie solaire par régions de 2013 à 2022')
plt.tight_layout()
plt.savefig('images/graph_boxplot_solaire.png')
plt.close()

# 5. Boxplot bioénergies
plt.figure(figsize=(14,6))
sns.boxplot(data=df, x='Région', y='Bioénergies', hue='Région')
plt.xticks(rotation=45)
plt.title('Production en MW de bioénergies par régions de 2013 à 2022')
plt.tight_layout()
plt.savefig('images/graph_boxplot_bio.png')
plt.close()