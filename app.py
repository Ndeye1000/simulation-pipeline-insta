import streamlit as st
import pandas as pd

st.title("Fichier obtenu apres traitement")

df = pd.read_csv("donnees_propres.csv")

st.write(df)