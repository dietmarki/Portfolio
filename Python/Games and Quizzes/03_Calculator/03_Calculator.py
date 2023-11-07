#!/usr/bin/env python
# coding: utf-8

# In[31]:


def weitermachen():
    weitermachen = input("Willst du weitermachen? (['y'/'n']Ja/Nein) ")
    if weitermachen == "y":
        return taschenrechner()
        
def begrüßen():
    print("Guten Tag!\nIch bin der beste Taschenrechner!\nIch kann +,-,*,/,// und % berechnen!\n")

def addition(x,y):
    print("Das Ergebnis der Addition von ",x," + ",y," lautet: ",x + y)

def subtraktion(x,y):
    print("Das Ergebnis der Subtraktion von ",x," - ",y," lautet: ",x - y)

def multiplikation(x,y):
    print("Das Ergebnis der Multiplikation von ",x," * ",y," lautet: ",x * y)

def division(x,y):
    print("Das Ergebnis der Division von ",x," / ",y," lautet: ",x / y)

def division_ganz(x,y):
    print("Das Ergebnis der Division-Ganz von ",x," // ",y," lautet: ",x // y)

def modulo(x,y):
    print("Das Ergebnis von Modulo von ",x," % ",y," lautet: ",x % y)

def taschenrechner():
    
    zahl01 = input("Tippe eine Zahl ein...")
    x = int(zahl01)
    nutzer_operator = input("Was willst du mit dieser Zahl tun? ")
    zahl02 = input("Tippe eine zweite Zahl ein...")
    y = int(zahl02)
    
    if nutzer_operator == "+":
        addition(x,y)
        weitermachen()

    elif nutzer_operator == "-":
        subtraktion(x,y)
        weitermachen()
            
    elif nutzer_operator == "*":
        multiplikation(x,y)
        weitermachen()
            
    elif nutzer_operator == "/":
        division(x,y)
        weitermachen()

    elif nutzer_operator == "//":
        division_ganz(x,y)
        weitermachen()
            
    elif nutzer_operator == "%":
        modulo(x,y)
        weitermachen()

begrüßen()
taschenrechner()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




