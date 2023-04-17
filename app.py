import streamlit as st
import pandas as pd

# Titre de l'application
st.title("Application Streamlit avec Pandas")

# Téléchargement du fichier CSV
csv_file = st.file_uploader("Téléchargez un fichier CSV", type="csv")

if csv_file is not None:
    # Lecture du fichier CSV avec Pandas
    data = pd.read_csv(csv_file)

    # Affichage des données
    st.write("Aperçu des données :")
    st.write(data.head())

    # Affichage des statistiques descriptives
    st.write("Statistiques descriptives :")
    st.write(data.describe())

    # Sélection des colonnes à afficher
    columns_to_display = st.multiselect(
        "Choisissez les colonnes à afficher :", data.columns)

    # Affichage des données filtrées
    if columns_to_display:
        st.write("Données filtrées :")
        st.write(data[columns_to_display])
