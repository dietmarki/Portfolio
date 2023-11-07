# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 12:20:59 2023

@author: dietm
"""

import streamlit as st
from random import randint

st.subheader("Zufallszahlen erzeugen")

#st.code("number01 = st.slider('Wähle das Minimum für die Zufallszahl:', 0, 10)")
mini = st.slider("Wähle eine Minimum:", 0, 10,key= "tim")

#st.code("number02 = st.slider('Wähle das Maximum für die Zufallszahl:', 2, 20)")
maxi = st.slider("Wähle eine Maximum:", 2, 20,key= "tam")

#st.code("number02 = st.slider('Wie viele Zufallszahlen sollen ausgegeben werden:', 1, 12)")
anz = st.slider("Wähle eine Anzahl:", 1, 12,key= "tum")

btn1 = st.button("Gib mir die Zufallszahlen!")
if btn1:     # Wenn der Button geklickt wird
    for i in range(1,anz + 1):
        st.write("• ", randint(mini, maxi),":sunglasses:")