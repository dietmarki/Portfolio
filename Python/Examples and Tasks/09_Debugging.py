#!/usr/bin/env python
# coding: utf-8

# In[2]:


import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def input_email():
    '''
    Fragt den User nach seiner Emailadresse.

        Parameters:

        Returns:
            email(str)
    '''
    user_email = input("Gib bitte deine Emailadresse ein!")
    return user_email

def input_age():
    '''
    Fragt den User nach seinem Alter.

        Parameters:

        Returns:
            age(int)
    '''
    user_age = input("Gib bitte dein Alter ein!")
    return user_age

aktive = True

while aktive:
    
    try:
        user_input = input("Drücke '?', um Hilfe zu bekommen\nDrücke 'q'. um die App zu verlassen.\nDrücke 'w', um weiterzumachen.\n")
        assert user_input == "?" or user_input == "q" or user_input == "w"
        
    except:
        logging.error("Bitte gib einen korrekten Input an!")    
    
    
    if user_input == "q":
        logging.debug("Die Schleife wurde beendet.")
        aktive = False
        
    elif user_input == "?":
        print(input_email.__doc__)
        print(input_age.__doc__)
        
    elif user_input == "w":
        try:
            user_email = input_email()
            logging.info("Funktion 'input_email' wurde aufgerufen.")
            assert "@" in user_email and "." in user_email and len(user_email) > 5
            logging.info(f"Eingegebene Email ist {user_email}")
        except AssertionError:
            logging.error("Bitte gib eine korrekte Email an!")
            user_email = input_email()
        try:
            user_age = input_age()
            logging.info("Funktion 'input_age' wurde aufgerufen.")
            assert int(user_age) >= 10 and int(user_age) < 100
            logging.info(f"Eingegebenes Alter ist {user_age}")
        except AssertionError:
            logging.error("Bitte gib ein korrektes Alter an!")
            user_age = input_age()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




