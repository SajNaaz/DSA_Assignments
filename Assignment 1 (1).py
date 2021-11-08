#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[9]:


pwd


# In[10]:


dt=pd.read_excel("iris.xls")


# In[11]:


dt


# In[12]:


dt.info()


# In[ ]:


# 2)Display the columns in the dataset.


# In[15]:


dt.columns


# In[ ]:


# 3. Calculate the mean of each column of the dataset.


# In[16]:


dt.describe()


# In[ ]:


# Or


# In[17]:


dt.mean()


# In[ ]:


# 4. Check for the null values present in the dataset.


# In[18]:


dt.isnull() #other option to find null "iris_data.isna()"


# In[22]:


#Total null values count in each columns
dt.isna().sum()


# In[ ]:


# 5. Perform meaningful visualizations using the dataset. Bring at least 3 visualizations.


# In[ ]:


# Since there is no missing values, visualisation can be done


# In[25]:


dt['Classification'].value_counts() # So,50 observation available for each


# In[26]:


#Using Swarm Plot
sns.swarmplot(x = 'Classification', y = 'SW', data = dt)


# In[27]:


sns.swarmplot(x = 'Classification', y = 'SL', data = dt)


# In[36]:


import warnings
warnings.filterwarnings("ignore") 


# In[37]:


sns.swarmplot(x = 'Classification', y = 'PW', data = dt)


# In[38]:


sns.swarmplot(x = 'Classification', y = 'PL', data = dt)


# In[31]:


# Histogram Method
dt[['SL','SW','PL','PW']].plot.hist()


# In[ ]:


# Kernel Base Density plot 


# In[33]:


dt[['SL','SW','PL','PW']].plot.kde() #probability distribution of various values


# In[ ]:




