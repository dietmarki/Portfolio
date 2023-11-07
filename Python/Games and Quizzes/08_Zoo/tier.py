#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Tier:
    
    def __init__(self, name, sex, age):
        self.name = name
        self.sex  = sex
        self.age  = age

    def eat(self):
        print(f"{self.name} isst.")
    
    def sleep(self):
        print(f"{self.name} schläft.")
        
    def grow(self,years):
        self.age += years
        print(f"{self.name} wurde {years} Jahre älter und ist jetzt {self.age} Jahre alt.")

