# bibliotheken importieren
import streamlit as st
import pandas as pd

# vektorisierung des textes --> numerische werte
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
# text_klassifzierung
from sklearn.naive_bayes import MultinomialNB

# daten auswerten:
def analyze(data):
    
    df = pd.DataFrame()
    
    for i in data.values():
        df = pd.concat([df,i["data"]],ignore_index=True)
        
    # nullwerte löschen:    
    df = df.dropna()
    
    # modell initialisieren:
    vect = CountVectorizer()
    
    # so wie die features: X
    wordsCountArray = vect.fit_transform(df["Satz"])
    
    # df["Autor"] so wie die labels: y
    X_train, X_test, y_train, y_test = train_test_split(wordsCountArray, df["Autor"], test_size=0.2, random_state=0)
    
    # algorithmus initialisieren:
    model = MultinomialNB()
    
    # modell trainieren:
    model.fit(X_train,y_train)
    
    # verwendete autoren:
    autoren = data.keys()
    
    s = f"Modell trainiert für Autoren:\n\n"
    
    for j in autoren:
        s += f"\t{j}\n"
        
    # ausgabe sätze insgesamt:
    s += f"Mit {X_train.shape[0]} Sätzen.\n\n"
    # modellgenauigkeit:
    s += f"Modellgenauigkeit: {model.score(X_test,y_test) *100:.2f}%"
    
    # langen string s in streamlit einbauen:
    st.markdown(s)
    
    return model,vect

