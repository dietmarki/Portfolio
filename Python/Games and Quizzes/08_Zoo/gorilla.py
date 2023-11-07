#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tier import Tier


# In[ ]:


class Gorilla(Tier):  

    def __init__(self, name, sex, age, is_cold_blooded, is_mammal, num_foots = 4):
        super().__init__(name, sex, age)
        self.is_cold_blooded = is_cold_blooded
        self.is_mammal = is_mammal
        self.num_foots = num_foots
        
    def eat(self):
        print(f"Gorilla {self.name} ernährt sich von Früchten.")
    
    def sleep(self):
        print(f"Gorilla {self.name} schläft.")
        
    def grow(self,years):
        self.age += years
        print(f"Gorilla {self.name} wurde {years} Jahre älter und ist jetzt {self.age} Jahre alt.")
        
    def klettern(self):
        print(f"Gorilla {self.name} klettert auf Bäume, um Früchte zu sammeln.")
    

