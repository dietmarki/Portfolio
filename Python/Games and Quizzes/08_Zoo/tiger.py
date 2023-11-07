#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tier import Tier


# In[3]:


class Tiger(Tier):  

    def __init__(self, name, sex, age, is_cold_blooded, is_mammal, num_foots = 4):
        super().__init__(name, sex, age)
        self.is_cold_blooded = is_cold_blooded
        self.is_mammal = is_mammal
        self.num_foots = num_foots
        
    def eat(self):
        print(f"Tiger {self.name} ist ein Fleischfresser.")
    
    def sleep(self):
        print(f"Tiger {self.name} schläft.")
        
    def grow(self,years):
        self.age += years
        print(f"Tiger {self.name} wurde {years} Jahre älter und ist jetzt {self.age} Jahre alt.")
        
    def typ(self):
        print(f"Der Tiger zählt zu den gefährlichsten Raubtieren der Welt.")
    

