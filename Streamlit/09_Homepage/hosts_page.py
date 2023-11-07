from webbrowser import get
from numpy import column_stack, datetime_as_string
import streamlit as st
import pandas as pd
import plotly.express as px

def app():

    df = pd.read_csv('listings.csv')


    st.header("Anzahl der Gastgeber")
    
    st.write("""Wir wollen nun die Gastgeber (*Hosts*) im Datensatz näher betrachten. Besonders wollen wir die Frage beantworten, **wer** die meisten Wohnungen 
    zum mieten anbietet.
    """)


    st.write(" Mit der Pandas Methode `value_counts()` der Spalte `host_id` kann man leicht ein Ranking erstellen.")
    st.code("listing_count = df.host_id.value_counts()")

    listing_count = df.host_id.value_counts()
    df_listing = pd.DataFrame(data={"host_id":listing_count.index, "sum": listing_count})
    hosts = df[["host_id", "host_name"]].drop_duplicates()
    join = pd.merge(hosts, df_listing, on='host_id', how='right')

    st.write("Das gibt uns folgend Liste zurück:")
    st.write(join)
    #st.write(f"Es gibt im Datensatz {df.host_id.shape[0]} listings, die von {len(df.host_id.unique())} unteriedlichen Hosts sind.")

    top_host_1 = df.query(f'host_id=={listing_count.index[0]}')
    

    st.write(f"Wir sehene, dass es {df_listing.shape[0]} Gastgeber gibt. Von diesen Gastgebern vermietet **{top_host_1.iloc[0].host_name}** die meisten Wohnungen.")

