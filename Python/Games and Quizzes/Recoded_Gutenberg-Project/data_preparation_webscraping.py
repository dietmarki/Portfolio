# bibliotheken importieren
import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
# html code richtig zu encoden:
from bs4.dammit import EncodingDetector 

# hauptfunktion ruft die autoren auf,
# weitere funktionen sind dann darin
BASE_URL = "https://www.projekt-gutenberg.org/"

# fehlermeldungen sollen unterdrückt werden:
#@st.cache_data()

# liste an buchtitel und url scrapen
def _find_books(books):
    
    tag = books.find("div",{"class":"archived"})
    if tag == None:
        return []
    
    book_url = []
    
    for l in tag.find_all("li"):
        tag = l.find("a",href=True)
        book_title = tag.string
        # tag um 6 zeichen kürzen ("../../kant/naturg/naturg.html"):
        url = f"{BASE_URL}/{tag['href'][6:]}"
        # url nur bis zum letzten "/", weil titel sonst doppelt!
        # führt so zum inhaltsverzeichnis:
        url = url[:url.rfind("/")]
        
        book_url.append((book_title,url))

    return book_url

# funktion zum abrufen der biographie:
def _find_info_bio(author_site):
    
    try:
        # find_all liefert ein "resultset" (=liste mit unterschiedlichen elementen,text,p,a,...)
        s = author_site.find_all("p")[1].text
        return s

    except:
        return None

def _find_image_url(author_site):
    
    try:
        return f"{BASE_URL}autoren/{author_site.find('img',src=True,title=True)['src'][3:]}"

    except:
        return None

# correction funktion:
def _correction(string):
    
    if len(string) < 4:
        return None
    else:
        return string

# text der untertitel scrapen --> _find_text:
def _find_text(books):
    
    text = ""
    
    for paragr in books.find_all("p"):
        if paragr.string:
            text = text + paragr.text
            
    return text

# funktion autor scrapen:
def scrape_author(author):
    
    # seite nach autor aufrufen:
    url = f"{BASE_URL}autoren/namen/{author.lower()}.html"
    print(f"Scrape den Autor: {author.upper()}\n Link: {url}")
    
    # html-sript von einem autor:
    res = requests.get(url)
    
    # fehler bei seite aufrufen --> abfangen:
    if res.status_code != 200:
        print(f"Autor {author} wurde nicht gefunden!")
        return None
    
    try:
        print(f"Autor {author} wurde gefunden!")
        # html-script mit bs4 --> übersichtlicher ("lxml" = encoder) und bs4_encoder ("from_encoding="):
        author_site = BeautifulSoup(res.content,"lxml",from_encoding=EncodingDetector.find_declared_encoding(res.content,is_html=True))
    
    except Exception:
        print("Error während dem Decoden")
        return None
    
    # dict mit allen infos über autor, funktionen (privat: "_..._"):
    infos = {"data"     : None,
             "books"    : _find_books(author_site),
             "info_bio" : _find_info_bio(author_site),
             "image_url": _find_image_url(author_site)
            }
    
    # dataframe von allem erstellen:
    df_all = pd.DataFrame()
    
    for title,url in infos["books"]:
        # hervorheben mit markdown (variable --> [{..}], url --> ({..})):
        st.markdown(f"[{title}]({url})")
        print(f"Scrape Buch: '{title}' [{url}]")
        
        # aktuellen dataframe:
        df_temp = _scrape_book(url)
        
        # aktuellen dataframe gesamt mit durchgehenden index:
        df_all = pd.concat([df_all,df_temp],ignore_index=True)
        
    # autor-spalte erstellen:
    df_all["Autor"] = author.upper()
    
    # daten in das dict einfügen:
    infos["data"] = df_all
    
    print(f"Gefundene Sätze: {df_all.shape}")
    
    return infos

# liste an untertiteln scrapen (_scrape_book und _correction):
def _scrape_book(url):
    
    res = requests.get(url)
    book_site = BeautifulSoup(res.content,"lxml",from_encoding=EncodingDetector.find_declared_encoding(res.content,is_html=True))
    
    # unterkapitel über die "li" im html-quellcode:
    subchapters = book_site.find_all("li")
    print(f"\tAnzahl Unterkapitel: {len(subchapters)}")

    # in den link hineingehen, wo texte sich befinden:
    subchapters_links = []
  
    for sub in subchapters:
        link = sub.find("a", href=True)
        subchapters_links.append(url + "/" + link["href"])
    
    # dataframe erstellen --> struktur für die einzelnen sätze:
    df = pd.DataFrame(columns=["Satz"])
    
    # progressbar erstellen (scraping-prozess-fortschritt anzeigen), startet bei 0:
    progressbar = st.progress(0)
    
    for index,temp_url in enumerate(subchapters_links):
        progressbar.progress((index+1)/len(subchapters_links))
        # neues zuweisen der aktuellen url:
        res = requests.get(temp_url)
        books = BeautifulSoup(res.content,"lxml",from_encoding=EncodingDetector.find_declared_encoding(res.content,is_html=True))
        data = _find_text(books)
        
        #einzelne sätze:
        for satz in data.split("."):
            # loc --> jede zeile einfügen (iloc--> jede spalte!)
            df.loc[len(df)] = satz
            
    #progressbar schliessen:
    progressbar.empty()
    
    # correction anwenden, nullwerte löschen:
    df["Satz"] = df["Satz"].map(_correction).dropna()
    
    return df    

