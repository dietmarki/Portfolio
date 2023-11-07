#!/usr/bin/env python
# coding: utf-8

# In[13]:


from random import randint
a = randint(1,100)

gamer = input("Errate die richtige Zahl des Computers zwischen 1 und 100! ")

aktiv = True
durchgang = 0

while aktiv:
    
    durchgang += 1
    
    if int(gamer) < a:
        print("Zahl zu niedrig!")
        gamer = input("Rate nochmal!")        
    elif int(gamer) > a:
        print("Zahl zu hoch!")
        gamer = input("Rate nochmal!")
    else:
        print("Richtig gerraten! Du hast ",durchgang, "Versuche benötigt!")
        nächstesSpiel = input("Ein weiteres Spiel? [y/n] ")
        
        if nächstesSpiel == "n":
            aktiv = False
            print("Das Spiel ist beendet.")
            
        else:
            gamer = input("Neues Spiel, gib eine Zahl ein! ")
            durchgang = 0
            a = randint(1,100)        



# ##### 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




