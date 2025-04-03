# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Chargement des données avec correction du chemin
# df = pd.read_csv(r"C:/Users/aymaa/Desktop/my_project/01_Data/supermarket_sales.csv", encoding="utf-8")

# # Vérification des colonnes et renommage si nécessaire
# df.columns = df.columns.str.strip()  # Supprime les espaces dans les noms de colonnes
# if "date" in df.columns:
#     df.rename(columns={"date": "Date"}, inplace=True)

# # Conversion des dates
# df["Date"] = pd.to_datetime(df["Date"])

# st.title("📊 Tableau de bord des ventes du supermarché")

# # Sélection de la succursale
# branch = st.selectbox("Sélectionnez une succursale :", df["Branch"].unique())

# # Filtrer les données
# filtered_df = df[df["Branch"] == branch]

# # Affichage des indicateurs clés
# total_sales = filtered_df["Total"].sum()
# avg_sales = filtered_df["Total"].mean()

# st.metric("💰 Ventes totales", f"${total_sales:,.2f}")
# st.metric("📉 Vente moyenne par transaction", f"${avg_sales:,.2f}")

# # Graphique des ventes par date
# fig = px.line(filtered_df, x="Date", y="Total", title="📈 Évolution des ventes", markers=True)
# st.plotly_chart(fig)

# # Graphique des ventes par catégorie de produit
# fig = px.bar(filtered_df, x="Product line", y="Total", title="🛒 Ventes par catégorie de produit", 
#              color="Product line", text_auto=True)
# st.plotly_chart(fig)


import streamlit as st
import pandas as pd
import plotly.express as px

# Chargement des données
df = pd.read_csv(r"C:/Users/aymaa/Desktop/my_project/01_Data/supermarket_sales.csv", encoding="utf-8")
df['Date'] = pd.to_datetime(df['Date'])

# # Appliquer le CSS
# with open("style.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Titre principal
st.title("📊 Supermarket Sales Dashboard")

# Sélection de la période
st.sidebar.header("🔍 Filtres")
date_range = st.sidebar.date_input("Sélectionnez une période", [df['Date'].min(), df['Date'].max()])
df_filtered = df[(df['Date'] >= pd.to_datetime(date_range[0])) & (df['Date'] <= pd.to_datetime(date_range[1]))]

# KPIs
total_sales = df_filtered["Total"].sum()
avg_sales = df_filtered["Total"].mean()
transactions = len(df_filtered)

col1, col2, col3 = st.columns(3)
col1.metric("💰 Ventes totales", f"${total_sales:,.2f}")
col2.metric("🛍 Transactions", transactions)
col3.metric("🏷 Vente moyenne", f"${avg_sales:,.2f}")

# Trier les données par date pour s'assurer du bon ordre
df_filtered = df_filtered.sort_values(by="Date")

# Graphique d'évolution des ventes
fig = px.line(df_filtered, x="Date", y="Total", title="📈 Évolution des ventes", line_shape="spline")
st.plotly_chart(fig, use_container_width=True)

# Ventes par catégorie de produit
fig = px.bar(df_filtered, x="Product line", y="Total", title="🛒 Ventes par catégorie", color="Product line")
st.plotly_chart(fig, use_container_width=True)

# Affichage conditionnel des données
if st.sidebar.checkbox("📄 Afficher les données brutes"):
    st.write(df_filtered)
