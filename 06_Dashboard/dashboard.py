import streamlit as st
import pandas as pd
import plotly.express as px

# Chargement des données avec correction du chemin
df = pd.read_csv(r"C:/Users/aymaa/Desktop/my_project/01_Data/supermarket_sales.csv", encoding="utf-8")

# Vérification des colonnes et renommage si nécessaire
df.columns = df.columns.str.strip()  # Supprime les espaces dans les noms de colonnes
if "date" in df.columns:
    df.rename(columns={"date": "Date"}, inplace=True)

# Conversion des dates
df["Date"] = pd.to_datetime(df["Date"])

st.title("📊 Tableau de bord des ventes du supermarché")

# Sélection de la succursale
branch = st.selectbox("Sélectionnez une succursale :", df["Branch"].unique())

# Filtrer les données
filtered_df = df[df["Branch"] == branch]

# Affichage des indicateurs clés
total_sales = filtered_df["Total"].sum()
avg_sales = filtered_df["Total"].mean()

st.metric("💰 Ventes totales", f"${total_sales:,.2f}")
st.metric("📉 Vente moyenne par transaction", f"${avg_sales:,.2f}")

# Graphique des ventes par date
fig = px.line(filtered_df, x="Date", y="Total", title="📈 Évolution des ventes", markers=True)
st.plotly_chart(fig)

# Graphique des ventes par catégorie de produit
fig = px.bar(filtered_df, x="Product line", y="Total", title="🛒 Ventes par catégorie de produit", 
             color="Product line", text_auto=True)
st.plotly_chart(fig)
