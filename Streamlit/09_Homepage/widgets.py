import streamlit as st
from math import sin
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def app():



    st.header("Widgets")
    st.write("""    
    `streamlit` besteht aus verschiedenen [Widgets](https://docs.streamlit.io/library/api-reference/widgets). 
    Widgets sind vorgefertigte Bauelemente (z.b. Buttons, Slider, etc) aus denen eine App bestehen kann.
    Im folgenden wollen wir auf einige Widgets eingehen.

    """)

    st.subheader("Text anzeigen")

    st.write("""[Text](https://docs.streamlit.io/library/api-reference/text) können wir einfach darstellen, über den Befehl `write(text)`. Z.B. erzeugt folgender Code """)
    st.code("st.write('Hallo Welt')")
    st.write("diese Ausgabe:")
    st.write('Hallo Welt')

    st.write("Auch Infoboxen sind einfach zu erzeugen. Dies geht mit dem Befehl `info()`.")

    st.info("Voila! Eine Infobox!")

    st.write("""Es stehen unterschiedliche Textformate zur Verfügung. Wer z.b. Erfahrung mit `Latex` besitzt, kann diese Funktionalität benutzen, 
    und so z.b. schöne Formeln darstellen:""")

    st.latex(r"\sum_{k=0}^{\infty} \frac{(-1)^k}{2k+1} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - ... = \frac{\pi}{4} ")

    st.write("Überschriften können mit `header()` ooder `subheader()` erzeugt werden. Z.b.")
    st.code("st.subheader('Slider')")

    # -----------------------------------------
    # SLIDER
    # -----------------------------------------

    st.subheader("Slider")

    st.write("""`streamlit` stellt einige Widgets zur Verfügung, mit denen auf Eingaben interaktiv und direkt reagiert werden kann. 
    Eine Überblick findest du [hier](https://docs.streamlit.io/library/api-reference/widgets). Im folgenden wird auf eine kleine Auswahl eingegangen.""")

    st.write("""Mit der Zeile unten kann man ganz einfach ein Slider erstellen. Ein Slider ermöglicht die Auswahl eines Wertes
    aus einem Intervall.""")
    
    st.code("number = st.slider('Wähle eine Nummer:', 0, 100)")

    st.write("Danach kann man die Zahl in einer Variablen speichern und mit Python bearbeiten.")

    number = st.slider("Wähle eine Nummer:", 0, 10)
    
    st.write(f"> Du hast die **Nummer {number}** ausgewählt!")

    st.info("Wir sehen, dass sich der obige Text automatisch ändert, wenn wir den Slider bewegen. Wir müssen dafür die Seite nicht neu laden!")

    # -----------------------------------------
    # CALENDAR
    # -----------------------------------------

    st.subheader("Calendar")

    st.write("Manchmal ist es nützlich den Nutzer ein Datum auswählen zu lassen.")
    st.code("date = st.date_input('Wähle ein Datum aus:'')")

    date = st.date_input("Wähle ein Datum aus:")

    days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sontag"]
    st.write(f"> Wow! Der {date.day}.{date.month}.{date.year} ist ein toller Tag. Es wird ein **{days[date.weekday()]}**.")

    # -----------------------------------------
    # BALLOONS
    # -----------------------------------------

    st.subheader("Buttons")

    st.write(""" Buttons werden benötigt, wenn es die Möglichkeit geben soll, etwas anzuklicken.
    Der Code hierfür ist auch selbsterklärend: """)
    st.code("""btn1 = st.button("Drück mich!")\nif btn1:     # Wenn der Button geklickt wird\n\tst.write(f"Der Button wurde geklickt!") """)
    


    btn1 = st.button("Drück mich!")
    if btn1:     # Wenn der Button geklickt wird
        st.write(f"Der Button wurde geklickt!")

    st.write("Man kann auch diverse Sachen mit einem Button machen. Hier ist ein Beispiel.")
    btn = st.button("Drück mich auch!")
    if btn:
        st.balloons()

    st.subheader("Plots")

    st.write("""Wir können über den Befehl `pyplot()` ein Schaubilder (*figure*),
    welches mit `matplotib` erzeugt wurde, darstellen. Im Beispiel unten wird eine *figure* erstellt, ein Plot gezeichnet und über `pyplot(fig)` angezeigt.""")  

    st.code("""fig = plt.figure()
x = np.linspace(0,6,100)
y = [sin(i) for i in x]
plt.plot(x,y)
st.pyplot(fig)    """)

    fig = plt.figure()

    x = np.linspace(0,6,100)
    y = [sin(i) for i in x]
    plt.plot(x,y)
    st.pyplot(fig)


    st.header("Line Chart")
    st.write("""Streamlit ist fest verzahnt mit `pandas`. Wir können auf einfache Art ein `DataFrame` von Pandas plotten.
    Der folgende Code erzeugt das unten stehende Schaubild. Es wird ein zufälliges Dataframe erstellt und angezeigt.""")

    st.code("""data_frame =  pd.DataFrame(np.random.randn(40,4), columns=["A","B","C","D"])\nst.line_char(data=data_frame)   """)

    data_frame =  pd.DataFrame(np.random.randn(40,4), columns=["A","B","C","D"])

    st.line_chart(data =data_frame)

    st.info("""Es ist möglich, sich interaktiv *im* Schaubild zu bewegen. 
    Man kann z.b. in das Schaubild zoomen oder die Achsen verschieben! Das ist mit den *statischen* Schaubildern von `matplotlib` **nicht** möglich.
    Über den Button rechts oberhalb des Schaubilds können wir in Fullscreen wechseln.""")


    st.write("Wir haben nun einige Widgets kennengelernt und wollen nun `streamlit` praktisch anwenden. Dazu werden wir realle Daten von **Airbnb** untersuchen.")