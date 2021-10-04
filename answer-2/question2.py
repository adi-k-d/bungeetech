#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


url = 'https://raw.githubusercontent.com/Bungeetech/internship-test2/master/input/question-2/main.csv'


# In[3]:


df1 = pd.read_csv(url)


# In[4]:


print(df1.groupby('occupation').agg({'age':['min','max']}))


# In[ ]:





# In[5]:


df1.to_csv('main2.csv',index=False)


# In[ ]:




