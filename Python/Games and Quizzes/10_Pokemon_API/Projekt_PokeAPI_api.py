# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 17:12:56 2023

@author: dietm
"""

import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon"

def fetch_data(name):

    # url bauen:
    url = f"{BASE_URL}/{name}"
        
    params = {"contentType":"json"}
        
    data = requests.get(url,params)
    
    #data = 

    #return data        
    return data.json()

