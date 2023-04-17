import streamlit as st
import pandas as pd


def custom_css(css):
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


css = '''
    .title {
        border: 2px solid #4f8bf9;
        padding: 10px;
        border-radius: 5px;
        background-color: #e9f2ff;
        color: #4f8bf9;
        font-weight: bold;
        text-align: center;
    }
    .section-title {
        color: #4f8bf9;
        font-weight: bold;
    }
'''

custom_css(css)

st.markdown('<div class="title">Application Streamlit avec Pandas et CSS personnalisé</div>', unsafe_allow_html=True)

csv_file = st.file_uploader("Téléchargez un fichier CSV", type="csv")

if csv_file is not None:
    data = pd.read_csv(csv_file)

    st.markdown('<div class="section-title">Aperçu des données :</div>', unsafe_allow_html=True)
    st.write(data.head())

    st.markdown('<div class="section-title">Statistiques descriptives :</div>', unsafe_allow_html=True)
    st.write(data.describe())

    columns_to_display = st.multiselect("Choisissez les colonnes à afficher :", data.columns)

    if columns_to_display:
        st.markdown('<div class="section-title">Données filtrées :</div>', unsafe_allow_html=True)
        st.write(data[columns_to_display])
