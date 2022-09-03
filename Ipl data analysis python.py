#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_csv(r"C:\Users\hp\Documents\IPL_Matches_2008_2022.csv")


# In[3]:


data.head()


# In[4]:


data.tail()


# In[5]:


data.info()


# In[6]:


data.isnull().sum


# In[24]:


sns.countplot(data['Season'])
plt.xticks(rotation=90,fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('Season', fontsize=10)
plt.ylabel('Count', fontsize=10)
plt.title('Total matches played each Season', fontsize=10, fontweight='bold')


# In[14]:


WinningTeam=data['WinningTeam'].value_counts()
WinningTeam.reset_index()


# In[15]:


City=data['City'].value_counts()
City.reset_index()
                    


# # top 5 player of the match
# 
# 

# In[17]:


Player_of_Match=data['Player_of_Match'].value_counts()[0:5]
Player_of_Match.reset_index()


# In[37]:


plt.pie(Player_of_Match.values, labels=Player_of_Match.index,labeldistance=1.2, autopct='%1.2f%%', shadow=True, startangle=90)
plt.title('Most player of the match in IPL',fontsize=10)
plt.show()


# In[47]:


TossDecision=data['TossDecision'].value_counts()
TossDecision.reset_index()


# In[ ]:




