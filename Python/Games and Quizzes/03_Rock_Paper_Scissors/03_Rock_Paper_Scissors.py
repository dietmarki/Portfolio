#!/usr/bin/env python
# coding: utf-8

# In[6]:


from random import randint

def computer():
    a = randint(1,3)
    return a

def spielen():
    spieler = input("Was möchtest du auswählen?\nSchere(1)\nStein(2)\nPapier(3)\nBeenden(4)\n")
    if spieler == 4:
        print("Spiel wird beendet.")
        aktiv = False
    else:
        return int(spieler)

aktiv = True

spiel_punkte = 0
comp_punkte = 0

while aktiv:
    
    spieler = spielen()
    a = computer()
    
    if spieler == a:
        if spieler == 1:
            print("Du hast Schere gewählt.\nDer Computer hat Schere gewählt.")
            print("Unentschieden!!")
            print("Zwischenstand:\nPunkte [Comp]:",comp_punkte," Punkte[Du]:",spiel_punkte)
        elif spieler == 2:
            print("Du hast Stein gewählt.\nDer Computer hat Stein gewählt.")
            print("Unentschieden!!")
            print("Zwischenstand:\nPunkte [Comp]:",comp_punkte," Punkte[Du]:",spiel_punkte)
        elif spieler == 3:
            print("Du hast Papier gewählt.\nDer Computer hat Papier gewählt.")
            print("Unentschieden!!")
            print("Zwischenstand:\nPunkte [Comp]:",comp_punkte," Punkte[Du]:",spiel_punkte)
                                               #1/Schere   2/Stein    3/Papier
    elif spieler == 1:
        if a == 2:
            print("Du hast Schere gewählt.\nDer Computer hat Stein gewählt.")
            print("Du hast verloren!")
            print("Zwischenstand:")
            print("Punkte [Comp]:",comp_punkte + 1," Punkte[Du]:",spiel_punkte)
            comp_punkte += 1
        elif a == 3:
            print("Du hast Schere gewählt.\nDer Computer hat Papier gewählt.")
            print("Du hast gewonnen!")
            print("Zwischenstand:\nPunkte [Comp]:",comp_punkte," Punkte[Du]:",spiel_punkte + 1)
            spiel_punkte += 1
    elif spieler == 2:
        if a == 1:
            print("Du hast Stein gewählt.\nDer Computer hat Schere gewählt.")
            print("Du hast gewonnen!")
            print("Zwischenstand:\nPunkte [Comp]: ",comp_punkte,"Punkte[Du]: ",spiel_punkte + 1)
            spiel_punkte += 1
        elif a == 3:
            print("Du hast Stein gewählt.\nDer Computer hat Papier gewählt.")
            print("Du hast verloren!")
            print("Zwischenstand:\nPunkte [Comp]: ",comp_punkte + 1,"Punkte[Du]: ",spiel_punkte)
            comp_punkte += 1
    elif spieler == 3:
        if a == 1:
            print("Du hast Papier gewählt.\nDer Computer hat Schere gewählt.")
            print("Du hast verloren!")
            print("Zwischenstand:\nPunkte [Comp]: ",comp_punkte + 1,"Punkte[Du]: ",spiel_punkte)
            comp_punkte += 1
        elif a == 2:
            print("Du hast Papier gewählt.\nDer Computer hat Stein gewählt.")
            print("Du hast gewonnen!")
            print("Zwischenstand:\nPunkte [Comp]: ",comp_punkte,"Punkte[Du]: ",spiel_punkte + 1)
            spiel_punkte += 1
    elif spieler == 4:
        aktiv = False        
            


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




