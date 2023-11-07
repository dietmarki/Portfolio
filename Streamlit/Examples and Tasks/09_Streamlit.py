import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Hausaufgabe")

st.header("Aufgabe 1")

st.info("""Erzeuge zwei Slider mit denen man jeweils eine Zahl zwischen 0 und 100 einstellen kann. Unterhalb der zwei Slider 
soll eine Textzeile stehen, welche die Summe dieser beiden Zahlen ausgibt.""")

# Code

# -----------------------------------------
# SLIDER
# -----------------------------------------

st.subheader("Aufgabe 1")

st.code("number01 = st.slider('Wähle eine Nummer:', 0, 100)")
number01 = st.slider("Wähle eine Nummer:", 0, 100,key= "tum")

st.code("number02 = st.slider('Wähle eine Nummer:', 0, 100)")
number02 = st.slider("Wähle eine Nummer:", 0, 100,key= "tam")

number03 = number02 + number01
st.write(f"> Das ist die Summe aus den von dir gewählten Zahlen **Nummer {number03}**!")

# Code


#Code
st.header("Aufgabe 2")

btn = st.button("Drück mich, bitte!")
if btn:
    st.info("99 Luftballons für dich!")
    st.success("Toll gemacht!")
    st.balloons()
    

#Code




st.header("Aufgabe 3")
st.info("Folgendes zufälliges Pandas `DataFrame` sei gegeben. Lass dir die Werte mit `line_chart()` plotten")

df = pd.DataFrame(data = np.random.randn(10,2),columns=["X","Y"])
st.write("DataFrame:")
st.write(df)

st.line_chart(df)

#Code 

st.header("Aufgabe 4")

st.info("Erzeuge eine Matplotlib-Figure mit einem Scatterplot mit den folgenden Daten.")

fig = plt.figure()
x=[0,3,4,5,3,6,9]
y=[-1,3,3,4,5,6,10]

plt.scatter(x,y,c="g",s=120,alpha=0.5)
st.pyplot(fig)

st.write(pd.DataFrame(data = zip(x,y),columns=["X","Y"], ))

st.info("Zur Erinnerung: Mit plt.scatter(X,Y) können wir die Werte aus `X` und `Y` in einem Scatterplot darstellen.")
#Code



st.header("Aufgabe 5")
st.write("""Schaue dir das [`text_input`](https://docs.streamlit.io/library/api-reference/widgets/st.text_input)-Widget an.
Lass den/die Anwender/in seinen Vor- und Nachnamen eingeben. Begrüsse ihn/sie daraufhin mit einem persönlichen Text""")
begrüßung = st.text_input(label="Gib mir bitte mal dein Vor- und Nachnamen ein!")
if begrüßung:
    st.info(f"Hallo {begrüßung}, wie geht's dir so?")

#Code


st.header("Aufgabe 6")
st.write("""Schau dir das [`selectbox`](https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)-Widget an.
Lass den Nutzer über diese Box auswählen, ob er mit Vor- oder Nachnamen begrüßt werden will. Gib je nach Auswahl eine passende Begrüßung aus."""
 )
#st.text_input(label="Gib mir bitte mal dein Vor- und Nachnamen ein!")

name_gesamt = begrüßung.split()
vorname = name_gesamt[0]
nachname = name_gesamt[1]

option = st.selectbox(label="Wollen Sie mit Vor- oder Nachnamen begrüßt werden?",options=('Vorname', 'Nachname'),)

if option == 'Vorname':
    st.info(f"Hallo {vorname}, wie geht's Dir so?")
    
else:
    st.info(f"Hallo Herr/Frau {nachname}, wie geht es Ihnen so?")

#Code

