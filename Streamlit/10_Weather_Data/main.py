
# um streamlit zu starten, in "anaconda prompt":
    # --> cd "C:\Users\dietm\Documents\Data Science_Didi\10. Woche\Streamlit 2>streamlit run DEMO_main_Kopie.py"
    #  --> "C:\Users\dietm\Documents\Data Science_Didi\10. Woche\Streamlit 2>streamlit run DEMO_main_Kopie.py" + "return"


import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
    # modul, um schaubild darzustellen:
from io import BytesIO

    # unser modul zur kommunikation mit API:
import api
    # unser modul zur verarbeitung der API-daten:
from data import get_daily_data,get_hourly_data

# seite konfigurieren:
st.set_page_config(layout="wide")
sns.set_theme(style="whitegrid")

# header erstellen:
st.header("Unsere WetterApp!")
# erklärung schreiben:
st.write("Hier kannst Du Datum/Temperatur an einem bestimmten Ort sehen.")
# seitliches fenster, abwählbar:
st.sidebar.header("Informationen")
    # checkbox, weitere map wählbar:
map = st.sidebar.checkbox("Wetterkarte anzeigen")
    # stadt auswählen:
cities = st.sidebar.text_input("Welche Städte interessieren dich?",
                               placeholder="hier Städtenamen mit Leerzeichen getrennt eintragen!")
date_start = st.sidebar.date_input("Zeitpunktanfang")
date_end = st.sidebar.date_input("Zeitpunktende")

# festlegen des intervalls: "hourly" oder "täglich"
intervall = st.sidebar.selectbox("Genauigkeit der Daten", ["Stunden","Tage"])

# daten aufrufen:
dataframe = []
# "lat","lon" = längen-/breitengrade als columns
gps = pd.DataFrame(columns=["lat","lon"])

# visualisierung - hauptseite mit 2 spalten: --> daten,karte
col1,col2 = st.columns([2,1])

# mit daten befüllen
with col1:
    if cities:
        for city in cities.split():
            data = api.fetch_data_city(city, date_start, date_end)
            # gps-daten in den dataframe einfügen:
            gps.loc[len(gps) + 1] = [data["latitude"],data["longitude"]]
            
            # intervall festgelegt --> daten befüllen:
            if intervall == "Stunden":
                df = get_hourly_data(data)
            elif intervall == "Tage":
                df = get_daily_data(data)
                
            # dataframe in die leere liste einfügen, stadt für stadt ...
            dataframe.append(df)
            
        # plotten:
        fig,ax1 = plt.subplots(figsize= (6,6))
        
        for d in dataframe:
            d.plot(
                kind="line",
                ax=ax1,
                ylabel="Temperatur",
                xlabel="Datum",
                rot=90,
                fontsize=8
                )
            if intervall == "Stunden":
                ticks = range(0,len(d),24)
            elif intervall == "Tage":
                ticks = range(0,len(d))
                
            #ax1.set_xticks(ticks=ticks,labels=[s[5:10] for s in  dataframe[0].index[ticks]])
        
        # als bild abspeichern:
        buf = BytesIO()
        fig.savefig(buf, format="png")
        st.image(buf)
        
# 2.spalte --> karte
with col2:
    if map:
        st.header("Landkarte")
        st.map(gps)



















