# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 17:12:33 2023

@author: dietm
"""

from Projekt_PokeAPI_api import fetch_data
import streamlit as st
import seaborn as sns

# seite konfigurieren:
st.set_page_config(layout="wide")
sns.set_theme(style="whitegrid")



    # Daten visualisieren
st.header(" Informationen ")


st.sidebar.header("Pokemon")
    # Input des Users
name = st.sidebar.text_input("Name des Pokemons")

st.sidebar.subheader("Serverantwort:")

f"Name de Pokemons: {name}"

    # Daten von der API abfragen
data = fetch_data(name)

st.sidebar.write(data)

st.image(data["sprites"]["versions"]["generation-i"]["red-blue"]["front_default"])

st.subheader("Fähigkeiten:")

st.write("1. ",data["abilities"][0]["ability"]["name"])
st.write("2. ",data["abilities"][1]["ability"]["name"])  

st.subheader("Eigenschaften:")


col1,col2 = st.columns([1,2])

with col1:
    st.write(f"Gewicht: ")
    st.write(data["weight"])
    
with col2:
    st.write(f"Größe: ")
    st.write(data["height"])























#. . .
#. . .