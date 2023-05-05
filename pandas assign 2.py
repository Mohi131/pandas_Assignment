#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd


# In[7]:


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'


# In[221]:


df = pd.read_csv(url, sep ="|", index_col='user_id')
df


# In[222]:


df


# In[ ]:





# # See the first 10 and last 10

# In[105]:


print(df.head(10))
print(df.tail(10))


# # what is the number of observation in the dataset?

# In[106]:


print("Number of Observations :", df.shape[0])


# In[16]:


print("Number of columns :", df.shape[1])


# # print the name of all columns.

# In[20]:


print(df.columns)


# # what is the data type of each column?

# In[223]:


df.info()


# # Print only the occupation column

# In[110]:


df['occupation']



# # different occupation are in this dataset?

# In[132]:


df['occupation'].nunique()



# # most frequent occupation

# In[143]:


df['occupation'].mode()


# # DataFrame Info

# In[34]:


df.info()


# # Describe all the columns

# In[157]:


print(df['zip_code'].describe())
print(df['gender'].describe())
print(df['occupation'].describe())
print(df['age'].describe())


# In[ ]:





# # Summarize only the occupation column

# In[129]:


c= df['occupation'].value_counts()
c


# # mean age of users

# In[102]:


df['age'].mean()


# # what is the age with  least occurrence 

# In[230]:


sd = df['age']
d =sd.value_counts()
least_occ = d.index[-5]
print(least_occ)


# In[ ]:





# In[ ]:




