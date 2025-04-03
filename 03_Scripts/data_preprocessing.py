import pandas as pd
import numpy as np

# Charger les données
df = pd.read_csv(r'C:\Users\aymaa\Desktop\my_project\01_Data\supermarket_sales.csv')

# 🔹 Convertir les dates
df['Date'] = pd.to_datetime(df['Date'])

# 🔹 Features temporelles
df['day_of_week'] = df['Date'].dt.dayofweek
df['month'] = df['Date'].dt.month

# 🔹 Moyennes mobiles pour lisser la demande
df['rolling_mean_7'] = df.groupby('Product line')['Quantity'].transform(lambda x: x.rolling(7, min_periods=1).mean())
df['rolling_mean_14'] = df.groupby('Product line')['Quantity'].transform(lambda x: x.rolling(14, min_periods=1).mean())

# 🔹 Variabilité de la demande
df['rolling_std_7'] = df.groupby('Product line')['Quantity'].transform(lambda x: x.rolling(7, min_periods=1).std())

# 🔹 Variation de ventes par rapport à la semaine précédente
df['weekly_change'] = df.groupby('Product line')['Quantity'].pct_change(periods=7)

# 🔹 Prédiction cible (décalage des ventes pour prévoir J+7)
df['future_demand_7'] = df.groupby('Product line')['Quantity'].shift(-7)

# 🔹 Approximation du stock actuel
df['stock_estime'] = df.groupby('Product line')['Quantity'].cumsum()
df['reapprovisionnement'] = np.where(df['stock_estime'] < df['rolling_mean_7'] * 2, df['rolling_mean_7'] * 5, 0)
df['stock_estime'] += df['reapprovisionnement']

# 🔹 Seuil de stock critique
df['stock_threshold'] = df['rolling_mean_7'] * 7 + (1.5 * df['rolling_std_7'])

# 🔹 Supprimer les features redondantes
columns_to_drop = [
    'Invoice ID', 'Tax 5%', 'cogs', 'Total', 'Date', 'Time',
    'Payment', 'gross margin percentage', 'gross income'
]
df.drop(columns=columns_to_drop, inplace=True)

# 📂 Sauvegarde des données prétraitées
df.to_csv(r"C:\Users\aymaa\Desktop\my_project\01_Data\supermarket_sales_cleaned.csv", index=False)

print("✅ Données prétraitées et sauvegardées.")
