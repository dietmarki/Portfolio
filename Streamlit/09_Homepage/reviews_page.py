from webbrowser import get
import streamlit as st
import pandas as pd
import plotly.express as px

def app():

    df = pd.read_csv('listings.csv')

    st.header("Anzahl von Bewertungen")

    st.write("Gib ein min und max Wert als Filter für die Anzahl der Bewertungen eines listings.")
    minimum = st.number_input("Minimum", min_value=0, value=500)
    maximum = st.number_input("Maximum", min_value=0, value=1000)
    if minimum > maximum:
        st.error("Das Maximum soll größer sein als das minimum. Bitte versuch es nochmal!")
    else:

        review_data = df.query(f"{minimum}<=number_of_reviews<={maximum}").sort_values("number_of_reviews", ascending=False)[["name", "number_of_reviews", "neighbourhood", "price"]]
        st.dataframe( review_data)

    st.write(f"Das {review_data.iloc[0][0]} ist das beliebteste mit {review_data.iloc[0].number_of_reviews} Bewertungen und befindet sich in {review_data.iloc[0].neighbourhood} mit einem Preis von {review_data.iloc[0].price}.")
    
    st.write(f"Der niedrigste Preis für diese range von Bewertungen ist {review_data.min().price} für das listing  {review_data.min()[0]} in  {review_data.min().neighbourhood}.")