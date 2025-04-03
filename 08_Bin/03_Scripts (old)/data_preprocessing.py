import pandas as pd
# from ummalqura import UummalquraDate

# 📂 Charger le dataset
df = pd.read_csv(r'C:\Users\aymaa\Desktop\my_project\01_Data\supermarket_sales.csv')

# 🔍 Voir les premières lignes
# df.head(5)

# 📊 Vérifier les types de données et les valeurs manquantes
# df.info()

# 📋 Vérifier les valeurs manquantes
df.isnull().sum()

# 💡 Si besoin, remplir les valeurs manquantes ou supprimer les lignes
df.fillna(0, inplace=True)  # Exemple pour remplir les NaN par 0

# 📅 Convertir les dates au bon format
df['Date'] = pd.to_datetime(df['Date'])

# 🔍 Vérifier les doublons et les supprimer
df.drop_duplicates(inplace=True)

# 🗓 Ajouter des features temporelles
df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day
df['weekday'] = df['Date'].dt.weekday
df['is_weekend'] = df['weekday'].isin([5, 6]).astype(int)

# 🏖 Ajouter des informations liées à la saisonnalité (vacances)
# Liste des jours fériés du Myanmar en 2019
holiday_dates = [
    '2019-01-01',  # Nouvel An
    '2019-03-13',  # Journée de l'Indépendance
    '2019-04-17',  # Thingyan (Nouvel An birman)
    '2019-05-01',  # Fête du Travail
    '2019-07-19',  # Martyrs' Day
    '2019-10-10',  # Full Moon Day of Thadingyut (Fête de la lumière)
    '2019-12-25'   # Noël
]

# Convertir les dates de vacances en format datetime.date pour la comparaison
holiday_dates = pd.to_datetime(holiday_dates).date

# Ajouter une colonne 'is_holiday' : 1 si jour férié, 0 sinon
df['is_holiday'] = df['Date'].apply(lambda x: 1 if x.date() in holiday_dates else 0)

# # 🌙 Convertir les dates grégoriennes en dates Hijri (Islamic Calendar)
# df['hijri_date'] = df['Date'].apply(lambda x: UummalquraDate(x.year, x.month, x.day).to_hijri())

# # 🌙 Extraire l'année et le mois hijri
# df['hijri_year'] = df['hijri_date'].apply(lambda x: x.year)
# df['hijri_month'] = df['hijri_date'].apply(lambda x: x.month)

# 🏷️ Catégoriser les produits en calculant le total des ventes et une moyenne mobile sur 7 jours
df['Total_Sales'] = df['Quantity'] * df['Unit price']
df['Rolling_Mean_7'] = df.groupby('Product line')['Total_Sales'].transform(lambda x: x.rolling(7, min_periods=1).mean())

# 📂 Sauvegarder les données transformées dans un fichier propre
df.to_csv(r"C:\Users\aymaa\Desktop\my_project\01_Data\supermarket_sales_cleaned.csv", index=False)

print("✅ Données préparées et enregistrées.")
