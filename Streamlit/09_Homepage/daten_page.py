
import streamlit as st
import pandas as pd



def app():
    
    st.header("Daten visualisieren")

    st.write("""
    Diese Seite dient als Hilfe, um zu verstehen wie man Daten mit `streamlit` visualisiert. 
    Dazu wollen wir die Daten aus der Datei `listings.csv` aus dem Kursbereich darstellen. Dies sind Daten von [Inside Airbnb]("http://insideairbnb.com/get-the-data.html").
    Wie wir es schon aus ML kennen, erstellen wir 
    einfach ein DataFrame mit Pandas aus einer CSV Datei. Dadurch kann man
    die Daten dann mit andere Pythonmodule, wie `matplotlib`, `seaborn`, u.a. bearbeiten und visualisieren. 
    """)

    st.subheader("CSV importieren")

    st.markdown("Zuerst laden wir die Daten aus der CSV Datei mit:")

    st.code("df = pd.read_csv('listings.csv')")

    df = pd.read_csv('listings.csv')

    st.subheader("DataFrame")

    st.markdown("Die Daten im Dateframe `df` kann man ganz leicht als Tabelle zeigen lassen mit:")
    st.code("st.dataframe(df)")

    st.markdown("""
    Bevor wir mit den Daten arbeiten, wollen wir diese zuerst verstehen und betrachten welche Größen existieren. 
    Dadurch können wir überlegen, was eine sinnvolle Visualisierungen ist. 
    
    Die von `streamlit` dargestellte Tabelle unten kann man sortieren, wenn man auf einem Spaltentitel klickt.
    """)

    st.dataframe(df)

    # ------------------------------------------

    st.subheader("Spalte einblenden")
    
    st.write(f"""
    Wir sehen, dass es {df.shape[1]} Spalten in `df` gibt. Hiervon wollen wir jedoch nicht alle darstellen, sondern nur eine Auswahl. Um Spalten einzublenden und eine
    übersichtliche Tabelle zu erstellen, bietet Streamlit das [multiselect](https://streamlit.io/docs/api.html#streamlit.multiselect) Widget.
    """)
    
    cols = st.multiselect(f"Spalten auswälen:", df.columns.tolist(), default=["name", "neighbourhood", "price"])
    st.dataframe(df[cols])

