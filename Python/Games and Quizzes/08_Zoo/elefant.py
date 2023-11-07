#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tier import Tier


# In[ ]:


class Elefant(Tier):  

    def __init__(self, name, sex, age, is_cold_blooded, is_mammal, num_foots = 4):
        super().__init__(name, sex, age)
        self.is_cold_blooded = is_cold_blooded
        self.is_mammal = is_mammal
        self.num_foots = num_foots
        
    def eat(self):
        print(f"Elefant {self.name} ist ein Pflanzenfresser.")
    
    def sleep(self):
        print(f"Elefant {self.name} schläft.")
        
    def grow(self,years):
        self.age += years
        print(f"Elefant {self.name} wurde {years} Jahre älter und ist jetzt {self.age} Jahre alt.")
        
    def typ(self):
        print(f"Der Elefant hat einen langen Rüssel und ein sehr gutes Gedächtnis.")
    

