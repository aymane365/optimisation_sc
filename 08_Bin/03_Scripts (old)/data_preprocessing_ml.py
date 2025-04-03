import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 📂 Charger le dataset nettoyé
df = pd.read_csv(r"C:\Users\aymaa\Desktop\my_project\01_Data\supermarket_sales_cleaned.csv")

# 📅 Convertir la colonne Date au bon format
df['Date'] = pd.to_datetime(df['Date'])

# 📌 Définition d'une rupture de stock (hypothèse) :
# Un produit est en rupture de stock s'il n'est pas vendu pendant plusieurs jours consécutifs
df['Stock_Out'] = (df['Quantity'] == 0).astype(int)

# 🏗 **Création des nouvelles features :**
df['prev_day_sales'] = df.groupby('Product line')['Total_Sales'].shift(1)
df['7d_avg_sales'] = df.groupby('Product line')['Total_Sales'].transform(lambda x: x.rolling(7, min_periods=1).mean())

# 🎯 **Sélection des features utiles pour l'apprentissage**
features = ['prev_day_sales', '7d_avg_sales', 'weekday', 'is_weekend', 'is_holiday']
target = 'Stock_Out'

# 🔀 **Séparer en jeu d'entraînement et de test**
X = df[features]
y = df[target]

# Remplacer les NaN par 0 (cas où il n’y a pas d’historique pour un produit)
X.fillna(0, inplace=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 📊 **Standardisation des features**
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 📂 Sauvegarder les données préparées
np.save(r"C:\Users\aymaa\Desktop\my_project\01_Data\X_train.npy", X_train_scaled)
np.save(r"C:\Users\aymaa\Desktop\my_project\01_Data\X_test.npy", X_test_scaled)
np.save(r"C:\Users\aymaa\Desktop\my_project\01_Data\y_train.npy", y_train)
np.save(r"C:\Users\aymaa\Desktop\my_project\01_Data\y_test.npy", y_test)

print("✅ Données de Machine Learning préparées et sauvegardées.")
