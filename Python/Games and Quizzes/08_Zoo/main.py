#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tier import Tier


# In[2]:


from tiger import Tiger


# In[3]:


tigerlein = Tiger("Tigerlein", "männlich", 12, "Ja", "Säugetier")


# In[4]:


tigerlein.typ()


# In[5]:


from gorilla import Gorilla


# In[6]:


cheetah = Gorilla("Cheetah", "männlich", 12, "Ja", "Säugetier")


# In[7]:


cheetah.klettern()


# In[8]:


from elefant import Elefant


# In[9]:


dumbo = Elefant("Dumbo", "weiblich", 43, "Ja", "Säugetier")


# In[10]:


dumbo.typ()


# In[11]:


from adler import Adler


# In[13]:


woopi = Adler("Woopi", "weiblich", 7, "Ja", "kein Säugetier")


# In[14]:


woopi.grow(3)


# In[ ]:




