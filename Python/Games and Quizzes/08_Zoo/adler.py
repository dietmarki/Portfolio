#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tier import Tier


# In[2]:


class Adler(Tier):  

    def __init__(self, name, sex, age, is_cold_blooded, is_mammal = False, num_foots = 2):
        super().__init__(name, sex, age)
        self.is_cold_blooded = is_cold_blooded
        self.is_mammal = is_mammal
        self.num_foots = num_foots
        
    def eat(self):
        print(f"Adler {self.name} ist ein Fleischfresser.")
    
    def sleep(self):
        print(f"Adler {self.name} schläft.")
        
    def grow(self,years):
        self.age += years
        print(f"Adler {self.name} wurde {years} Jahre älter und ist jetzt {self.age} Jahre alt.")
        
    def typ(self):
        print(f"Der Adler kann fliegen und ist kein Säugetier.")
        


# In[ ]:




