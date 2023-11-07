# um streamlit zu starten, in "anaconda prompt":
    # --> cd "C:\Users\dietm\Documents\Data Science_Didi\10. Woche\Streamlit 2>streamlit run DEMO_main_Kopie.py"
    #  --> "C:\Users\dietm\Documents\Data Science_Didi\10. Woche\Streamlit 2>streamlit run DEMO_main_Kopie.py" + "return"

# bibliothek für API-requests:
import requests

# basiszugriff auf URL:
BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
key = "EFB5P8LRGTWURL3AG7CUDED7C"

# fehler-klassen definieren:
class MaximumRequestsDone(Exception):
    pass
class UndefinedLocation(Exception):
    pass
class WrongAPIKey(Exception):
    pass
class WrongDatum(Exception):
    pass

# funktion die über API eine anfrage stellt:
def fetch_data_city(city,start,end):
    
    # falls die seite nicht gefunden wird --> try/catch-block:
    try:
        
        # url bauen:
        url = f"{BASE_URL}/{city}/{start}/{end}"
        
        params = {"key":key,
                  "unitGroup":"metric",
                  "contentType":"json"}
        
        res = requests.get(url, params)
        
        return res.json()
        
    except ValueError as e:
        
        print(res.text)
        if "maximum number" in res.text:
            raise MaximumRequestsDone
        if "invalid location found" in res.text:
            raise UndefinedLocation
        if "API key" in res.text:
            raise WrongAPIKey
        if "cannot be before" in res.text:
            raise WrongDatum
        
    finally:
        pass
    
