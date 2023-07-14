import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title("APPLICATION DE Jean MOYENGA")
st.write("Bienvenue dans mon application streamlit")

data = None
url_api = "http://localhost:8000/jeanapi/data"

# Fonction pour appeler l'API et obtenir les données
def get_data_from_api():
    response = requests.get(url_api)
    return pd.DataFrame(response.json())

# Afficher le bouton dans le dashboard
if st.button('Obtenir les données'):
    # Appeler la fonction pour obtenir les données de l'API
    data = get_data_from_api()

# Afficher les données dans le dashboard
if data is not None:
    st.dataframe(data)

if data is not None:
        df = pd.DataFrame(data)  # Utilisation de data pour créer un DataFrame df

    # Calcul du chiffre d'affaires
        chiffre_affaires = df['price'].sum()
        st.write(f"<span style='color:red; font-size:40px;'>Chiffre d'affaires : {chiffre_affaires} € </span>", unsafe_allow_html=True)

    ## Box plot
        fig = px.box(df, x='product_id', y='age')
        fig.update_layout(
            xaxis_title='Produits',
            yaxis_title="Âge",
            title="Âge des clients en fonction des produits")
        st.plotly_chart(fig)

        fig1 = px.bar(df,x='campaign_id', y='price')
        fig1.update_layout(
            xaxis_title='campagne',
            yaxis_title="price",
            title="Les ventes par campagnes")
        st.plotly_chart(fig1)

        fig3 = px.histogram(df, x='gender', y='product_id')
        fig3.update_layout(
             xaxis_title='gender',
             yaxis_title="produits",
             title="Produit par sexe")
        st.plotly_chart(fig3)


