import streamlit as st

# funktionen der eigenen dateien importieren:
from data_preparation_webscraping import scrape_author
from machine_learning_model import analyze

# streamlit-layout festlegen:
st.set_page_config(layout="wide")

# title mit link zur website:
st.header("[Projekt Gutenberg](https://www.projekt-gutenberg.org/)")

# 2 columns:
col1,col2 = st.columns(2)

# alle daten, die gespeichert werden --> session-state:
if "vect" not in st.session_state:
    st.session_state.vect = None
if "model" not in st.session_state:
    st.session_state.model = None
if "data" not in st.session_state:
    st.session_state.data = {}
    
# sidebar erstellen:
autor = st.sidebar.text_input("Welche/r Autor/in interessiert dich?",value="Kafka",help="Der Nachname ist ausreichend.").upper()

st.sidebar.markdown("""Durch die Verwendung der [session_state](https://docs.streamlit.io/library/api-reference/session-state) 
                    werden die Daten eines Autors nur **einmal** gescrapt. 
                    Bei nochmaliger Abfrage werden automatisch die schon existierenden Daten geladen.""")

# buttons erstellen:
if st.sidebar.button("Starte Scraping...",help="Drücke zum Scrapen"):
    
    if autor not in st.session_state.data.keys():
        data = scrape_author(autor)
        
        #Abfrage        
        if data == None:
            st.error("Abfrage ist fehlerhaft, sorry!")            
        else:
            st.session_state.data[autor.upper()] = data
    else:
        print("Auto/in ist bereits extrahiert worden!")
        
if st.sidebar.button("Lösche Daten...",help="Löscht alles",disabled=len(st.session_state.data.keys())==0):
    st.session_state.data = {}
    
# die 2 columns erstellen:
with col1:
    
    if autor in st.session_state.data.keys():
        # unterüberschrift und text:
        st.subheader("Biographie")
        st.write(st.session_state.data[autor.upper()]["info_bio"])
        # bild erstellen:
        if st.session_state.data[autor.upper()]["image_url"]:
            st.image(st.session_state.data[autor.upper()]["image_url"])
        # dataframe erstellen --> alle Sätze:
        st.dataframe(st.session_state.data[autor.upper()]["data"],width=600)
        # buchtitel:
        st.subheader("Bücher")
        # buchtitel:
        for b in st.session_state.data[autor.upper()]["books"]:
            # ausgeben des tupels mit 1.titel und 2.url-link:
            st.markdown(f"[{b[0]}]({b[1]})")
            
# spalte für data science:
with col2:
    
    # auswahlfenster für die autoren:
    selection = st.multiselect("Autoren",st.session_state.data.keys())
    # analyse button:
    analyse = st.button("Analysiere die Autoren",help="Analysiert Autoren")
    
    # funktion vom button:
    if analyse and selection != 0:
        m = {}
        
        for sel in selection:
            m[sel] = st.session_state.data[sel]
            
        if m != {}:
            # von funtkion model(trainieren) und vect(vectorizer) holen:
            st.session_state.model, st.session_state.vect = analyze(m)
    
    # textfeld für eingabe zur analyse:
    text = st.text_input("Wer hat es (wahrscheinlich) geschrieben?")
    # ausgabe der wahrscheinlichkeit:
    if st.session_state.model != None and st.session_state.vect != None:
        propas = st.session_state.model.predict_proba(st.session_state.vect.transform([text]))
        # schleife über die autoren:
        for i in range(len(st.session_state.model.classes_)):
            st.markdown(f"**{st.session_state.model.classes_[i]}**: {propas[0][i] * 100:.2f} %")


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
