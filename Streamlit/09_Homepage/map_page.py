
import streamlit as st
import pandas as pd
import plotly.express as px

def app():

    df = pd.read_csv('listings.csv')

    st.header("Visualisierung der Daten")

    st.write("Wir wollen die Analyse der Daten von AirBnB fortsetzen. Dazu müssen wir die Daten wieder laden und in einem `DataFrame` speichern.")

    st.code("df = pd.read_csv('listings.csv')")
    
    st.write("""Wir wollen nun die Wohnungen nach einem Preis filtern. Dazu erstellen wir ein Slider-Widget, 
    in welchem wir ein Intervall für die Preise angeben können. Wenn wir dieses Intervall ändern, 
    werden in der folgenden Karte nur die Wohnungen in diesem Preissegment angezeigt.""")
    
    # Slider
    values = st.slider("Preisintervall", float(df.price.min()), float(df.price.clip(upper=1000.).max()), (50., 300.))

    st.write("Dazu stellen wir eine Anfrage an die Daten im `DataFrame`:")


    # Query
    query = f"{values[0]}<price<{values[1]}"
    selection_df = df.query(query)
    st.code(f"""query={query}\nselection_df = df.query(query)
    """)
    st.write("Dies filtert aus dem gesamten Datensatz `df` automatisch diejenigen im eingegebenen Preisintervall.")
    # ------------------------------------------
    # --------------------Map Viz---------------
    # ------------------------------------------

    st.subheader("Daten auf der Karte")
    st.map(selection_df[["latitude", "longitude"]].dropna())
    st.markdown(f"Es werden {df.query(query).shape[0]} Datenpunkte mit einem Preis von {values[0]} bis {values[1]} angezeigt.")

    st.markdown("Wir sehen, dass es sehr einfach ist mit `streamlit` *interaktive* Apps zu schreiben!")


    # ------------------------------------------
    # ----------------Price Viz-----------------
    # ------------------------------------------

    st.subheader("Preisverteilung")
    st.write("""Für das oben angegebene Preisintervall wollen wir uns die Verteilung der Wohnungen anzeigen lassen. 
          Dafür benutzen wir [`st.plotly_chart`](https://streamlit.io/docs/api.html#streamlit.plotly_chart).""")
    
    f = px.histogram(df.query(f"price.between{values}"), x='price', nbins=15, title="Preisverteilung der Wohnungen")
    f.update_yaxes(title="Anzahl Wohnungen")
    f.update_xaxes(title="Preis")
    st.plotly_chart(f)

    # ------------------------------------------
    # ----------------Tabelle Viz---------------
    # ------------------------------------------

    st.subheader("Daten in der Tabelle")
    st.markdown("Die gleichen Daten können auch wie gewohnt in einer Tabelle angezeigt werden.")
    
    st.write(df.query(query).sort_values("price", ascending=False))
    
