#!/usr/bin/env python
# coding: utf-8

# In[1]:


def text_eingabe():
    user_text = input("Bitte Text eingeben (oder quit): ").lower()
    return user_text

def zahl_eingabe():
    user_zahl = int(input("Um wieviel Zeichen soll der Text veschlüsselt werden? "))
    return user_zahl

def buchstaben_klein():
    
    buchstaben_kl = ""
    for b in range(97,123):
        buchstaben_kl += chr(b)
    return buchstaben_kl
    
aktive = True

while aktive:
    
    user_text = text_eingabe()
    if user_text == "quit":
        print("Das Verschlüsseln ist beendet!")
        break
    user_zahl = zahl_eingabe()
    buchstaben_kl = buchstaben_klein()
    no_text = ""
    
    for a in user_text:
        if a == " ":
            no_text += " "
            continue
        if a not in buchstaben_kl:
            no_text += a
            continue
            
        for c in range(len(buchstaben_kl)):
            if a == buchstaben_kl[c]:
                if c + user_zahl >= len(buchstaben_kl):
                    no_text += buchstaben_kl[c + user_zahl - len(buchstaben_kl)]
                else:
                    no_text += buchstaben_kl[c + user_zahl]
                    
    print("Text verschlüsselt: ",no_text)
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




