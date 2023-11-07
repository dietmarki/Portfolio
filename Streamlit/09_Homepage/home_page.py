

#Importiere Streamlit
from matplotlib import widgets
import streamlit as st

# Importiere die Seiten/Module
import tutorial_page
import daten_page
import reviews_page
import hosts_page
import fazit
import map_page
import widgets

# ------------------------------------------
# -----------------Preamble-----------------
# ------------------------------------------

st.title("[Streamlit](https://streamlit.io/) Demo Projekt")  # Erzeugt eine Titel für die App

#st.info("Wähle eine Seite im Navi links.")    # Erzeugt eine Infobox

st.info("""
Das ist ein kurzes Python Projekt, um die Möglichkeiten von Streamlit vorzustellen.
Für weitere Infos, sei auf die [Dokumentation](https://docs.streamlit.io/library/get-started) verwiesen.
""")


#    Wir nutzen einen Export der **Airbnb** Daten aus ).

pages = {
    "1. Streamlit": tutorial_page,
    "2. Widgets": widgets,
    "2. Daten": daten_page,
    "3. Map": map_page,
    "4. Hosts": hosts_page,
    "5. Reviews": reviews_page,
    "6. Fazit": fazit,
}

st.sidebar.title("Seiten")
select = st.sidebar.radio("Gehe zu Seite:", list(pages.keys()))
pages[select].app()   # Startet die Seite
