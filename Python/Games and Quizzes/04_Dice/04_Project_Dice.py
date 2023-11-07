#!/usr/bin/env python
# coding: utf-8

# In[17]:


#Simuliere N Würfe eines (fairen) Würfels

#Speichere diese Würfe in einer geeigneten Datenstruktur ( eine Liste bietet sich an)

# Berechne den Mittelwert dieser Würfe

#Wie nahe sind wir am theoretischen Erwarungswert von 3.5?

#Was ändert sich wenn wir N groß bzw. klein wählen?
  
from random import randint

def wurfliste():
    
    n_würfe = int(input("Wie viele Würfe sollen simuliert werden? "))
    print("Simuliere ",n_würfe, " Würfe....")
    liste = []
    for i in range(1,(n_würfe + 1)):
        liste.append(randint(1,6))
        
    return liste

def mittelwert():
    
    liste = wurfliste()
    summe = 0
    for a in liste:
        summe += a
        
    m_wert = summe / len(liste)
    
    print("Der Mittelwert der Würfe ist ", m_wert, "\nDer theoretische Wert ist 3.5")
        
aktive = True

while aktive:
    
    mittelwert()
    beenden = input("Für beenden (quit), sonst irgendwas!")
    if beenden == "quit":
        print("Berechnung ist beendet.")
        break
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




