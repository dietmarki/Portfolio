
import streamlit as st



def app():
    
    st.header("Motivation")

    st.write("""
    Mit `streamlit` ist es möglich schnell und einfach Web Apps in Python zu erstellen. 
    In dieser Seiten zeigen wir anhand Daten von **Airbnb** einen Teil der Funktionalität. 
    Über das Navigationspanel links kannst du zu anderen Tutorials springen.
    Schaue dir parallel zu der Darstellung im Browser noch den dazugehörigen Python-Code an. Du wirst festellen, dass es recht selbsterklärend ist!
    Um `streamlit` benutzen zu können, reicht es die Bibliothek zu importieren:""")
    st.code("import streamlit as st")
    st.write("""Bevor wir jedoch mit den konkreten Daten von **Airbnb** experimentieren, wollen wir als erstes einige *Widgets* (Bauelemente) 
    von `streamlit` kennenlernen.      """)
    