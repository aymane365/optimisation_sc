import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données
df = pd.read_csv(r"C:\Users\aymaa\Desktop\my_project\01_Data\supermarket_sales_cleaned.csv")

# 🔹 1. Encodage des variables catégorielles
df_encoded = pd.get_dummies(df, drop_first=True)

# 🔹 2. Matrices de corrélations

# Pearson (linéaire)
corr_pearson = df_encoded.corr(method='pearson')
# Spearman (monotone)
corr_spearman = df_encoded.corr(method='spearman')
# Kendall (ordinale)
corr_kendall = df_encoded.corr(method='kendall')

# 🔹 3. Définition d'une fonction pour affichage clair
def plot_correlation_matrix(corr_matrix, title):
    plt.figure(figsize=(8, 6))  # Taille plus grande pour lisibilité
    sns.heatmap(corr_matrix, cmap='coolwarm', center=0, annot=True, fmt=".2f", linewidths=0.5)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks(fontsize=10)
    plt.show()  # Affichage instantané sans fermer les autres fenêtres

# 🔹 4. Affichage des matrices séparément
plot_correlation_matrix(corr_pearson, "Corrélation de Pearson")
plot_correlation_matrix(corr_spearman, "Corrélation de Spearman")
plot_correlation_matrix(corr_kendall, "Corrélation de Kendall")