#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas


# In[2]:


"c:\users\enking"


# In[19]:


get_ipython().system('pip install openpyxl')


# In[6]:





# In[7]:


denzil = pd.read_excel('Market_return_data.xlsx',index_col = 0)


# In[14]:


denzil


# In[1]:


get_ipython().system('pip install sklearn')


# In[8]:


from sklearn.preprocessing import OrdinalEncoder
oe = OrdinalEncoder()
feature_target = oe.fit_transform(denzil)


# In[9]:


feature_target


# In[11]:


denzil.Return.value_counts()


# In[12]:


##total entropy
- ((6/10)*np.log2(6/10) + (4/10)*np.log2(4/10))


# In[16]:


#data Set 1 entropy
- ((1/4)*np.log2(1/4) + (3/4)*np.log2(3/4))


# In[17]:


#data Set 2 entropy
- ((5/6)*np.log2(5/6) + (1/6)*np.log2(1/6))


# In[21]:


#1st Data Set split entropy
(4/10)*0.811


# In[22]:


#2nd Data Set Split entropy
(6/10)*0.65


# In[23]:


#submition of entropy after split

0.3244+0.39


# In[24]:


##information gain = Total entropy - Submition of entrpy after split

0.97-0.71

