import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

# 🔹 Charger les données prétraitées
df = pd.read_csv(r"C:\Users\aymaa\Desktop\my_project\01_Data\supermarket_sales_cleaned.csv")  

# 🔹 Sélection des variables catégoriques à encoder
categorical_cols = ['Branch', 'City', 'Customer type', 'Gender', 'Product line']
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)  # Encodage OneHot

# 🔹 Définition des features et de la cible
X = df_encoded.drop(columns=['Quantity'])  # Exclure la target du dataset
y = df_encoded['Quantity']  # Variable cible

# 🔹 Séparer en données d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🔹 Modèle de sélection de features
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 🔹 Importance des features
importances = model.feature_importances_
feature_importance_df = pd.DataFrame({'Feature': X.columns, 'Importance': importances})
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

# 🔹 Affichage des résultats
plt.figure(figsize=(10, 6))
sns.barplot(data=feature_importance_df, x='Importance', y='Feature', palette='coolwarm')
plt.title("Importance des Features (Random Forest)")
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.show()

# 🔹 Sélection des meilleures features
selected_features = feature_importance_df[feature_importance_df['Importance'] > 0.01]['Feature'].tolist()
print("Features sélectionnées :", selected_features)

# 🔹 Sauvegarde des features sélectionnées pour la suite
df_selected = df_encoded[selected_features + ['Quantity']]
df_selected.to_csv(r"C:\Users\aymaa\Desktop\my_project\01_Data\selected_features.csv", index=False)

print("✅ Feature selection terminée et sauvegardée.")
