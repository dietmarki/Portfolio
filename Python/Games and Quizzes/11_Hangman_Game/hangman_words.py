#!/usr/bin/env python
# coding: utf-8

# In[5]:


import sqlite3
connection = sqlite3.connect("hangman_database.db")
cur = connection.cursor()

aktiv = True

while aktiv:
    
    user_eingabe = input("Welches Wort soll der Datenbank hinzugefügt werden: (oder EXIT)\n")
    wort = user_eingabe.upper()
    länge_wort = len(user_eingabe)
    user_tupel = (wort,länge_wort)
    
    if wort == "EXIT":
        print("Die aktuelle Datenbank lautet:")
        for db in cur.execute("SELECT * FROM words"):
            print(db[0])
        print("Die Datenbank wird nun geschlossen!")
        connection.close()
        break
        
    elif not user_tupel in cur.execute("SELECT * FROM words"):
        cur.execute("INSERT INTO words VALUES(?,?)", (wort, länge_wort))
        connection.commit()
        print(f"Das Wort {wort} wurde in der Datenbank abgespeichert!")
            
    else:
        print(f"Das Wort {wort} befindet sich schon in der Datenbank!")        
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




