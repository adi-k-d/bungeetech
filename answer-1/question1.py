#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


url = 'https://raw.githubusercontent.com/Bungeetech/internship-test2/master/input/question-1/main.csv'


# In[4]:


df1 = pd.read_csv(url)


# In[5]:


df2=df1.groupby((df1.Year//10)*10).sum()


# In[7]:


df2.drop(['Year'], axis=1)


# In[8]:


df2.to_csv('main1.csv',index=False)


# In[ ]:




