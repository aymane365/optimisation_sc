import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 🔹 Charger les features sélectionnées
df = pd.read_csv(r"C:\Users\aymaa\Desktop\my_project\01_Data\selected_features.csv")

# 🔹 Séparer les features et la cible
X = df.drop(columns=['Quantity'])
y = df['Quantity']

# 🔹 Split en train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🔹 Entraînement du modèle
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 🔹 Prédictions
y_pred = model.predict(X_test)

# 🔹 Évaluation des performances
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"📊 Erreur Absolue Moyenne (MAE) : {mae:.2f}")
print(f"📊 Erreur Quadratique Moyenne (RMSE) : {rmse:.2f}")

# 🔹 Visualisation des résultats
plt.figure(figsize=(10, 5))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot([y.min(), y.max()], [y.min(), y.max()], '--', color='red')  # Ligne parfaite
plt.xlabel("Valeurs Réelles")
plt.ylabel("Prédictions")
plt.title("Prédictions vs Réalité")
plt.show()

# 🔹 Sauvegarde du modèle (si besoin pour une API plus tard)
import joblib
joblib.dump(model, r"C:\Users\aymaa\Desktop\my_project\04_Models\demand_forecast_model.pkl")
