#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np


# In[7]:


url = 'https://raw.githubusercontent.com/Bungeetech/internship-test2/master/input/question-3/main.csv'


# In[8]:


df1 = pd.read_csv(url)


# In[9]:


df2=(df1.sort_values(by=['Red Cards','Yellow Cards'],ascending=False))


# In[10]:


b=df2[['Team','Red Cards','Yellow Cards']]
b


# In[11]:


b.to_csv('main3.csv',index=False)


# In[ ]:




