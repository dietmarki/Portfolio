# um streamlit zu starten, in "anaconda prompt":
    # --> cd "C:\Users\dietm\Documents\Data Science_Didi\10. Woche\Streamlit 2>streamlit run DEMO_main_Kopie.py"
    #  --> "C:\Users\dietm\Documents\Data Science_Didi\10. Woche\Streamlit 2>streamlit run DEMO_main_Kopie.py" + "return"

# für json-daten --> auf "https://weather.visualcrossing.com" daten bereitstellen über
# "weather API" und den betreffenden ort eingeben

# bibliothek importieren:
import pandas as pd

# tägliche wetterdaten:
def get_daily_data(data):
    
    # checken, ob daten verarbeitbar sind:
    if not isinstance(data, dict):
        print("Hier ist etwas schiefgelaufen!")
        return None
    
    # dataframe bauen aus den vorhandenen daten (tage,temperatur):
    indices = []
    temp = []
    
           # über die keys des dictionarys von data iterieren:
    for d in data["days"]:
        indices.append(d["datetime"])
        temp.append(d["temp"])
        
    df = pd.DataFrame(data = {f"{data['address']}": temp}, index = indices)
    
    return df

# stündliche wetterdaten:
def get_hourly_data(data):
    
    # checken, ob daten verarbeitbar sind:
    if not isinstance(data, dict):
        print("Hier ist etwas schiefgelaufen!")
        return None
    
    indices = []
    temp = []
    
    for d in data["days"]:
        for h in d["hours"]:
            indices.append(f"{d['datetime']} {h['datetime']}")
            temp.append(h["temp"])
            
    df = pd.DataFrame(data = {f"{data['address']}": temp}, index = indices)
    
    return df
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    