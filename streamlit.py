
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le dataset
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# Charger les données
st.title("Exploration Interactive du Dataset Beans and Pods")
st.sidebar.header("Options")
file_path = st.sidebar.text_input("Entrez le chemin du fichier CSV", "data/BeansDataSet.csv")

try:
    data = load_data(file_path)
    st.write("### Aperçu des données")
    st.write(data.head())
    
    # Informations sur les données
    st.write("### Informations sur le Dataset")
    st.write(data.info(verbose=True))
    
    # Statistiques descriptives
    st.write("### Statistiques descriptives")
    st.write(data.describe())
    
    # Visualisation
    st.write("## Visualisations")
    selected_columns = st.multiselect("Choisissez les colonnes à visualiser", data.columns)
    if selected_columns:
        st.write("### Matrice de dispersion")
        sns.pairplot(data[selected_columns])
        st.pyplot(plt)
        
        st.write("### Histogrammes")
        for col in selected_columns:
            st.write(f"Histogramme pour {col}")
            plt.figure(figsize=(10, 4))
            sns.histplot(data[col], kde=True)
            st.pyplot(plt)
except Exception as e:
    st.error(f"Erreur lors du chargement ou de l'analyse des données : {e}")
