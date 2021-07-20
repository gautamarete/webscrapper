#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns #necessary modules for web scraping
get_ipython().run_line_magic('matplotlib', 'inline')
from urllib.request import urlopen #to open urls
from bs4 import BeautifulSoup


# In[6]:


url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url) #to get the html of the page


# In[7]:


soup = BeautifulSoup(html, 'lxml') #to parse the html
type(soup)


# In[8]:


#get the title of the page
title = soup.title
print(title)


# In[9]:


text = soup.get_text()
print(soup.text)


# In[10]:


soup.find_all('a')


# In[11]:


all_links = soup.find_all('a')
for link in all_links:
    print(link.get("href")) #to get the href method


# In[12]:


rows = soup.find_all('tr')
print(rows[:10])


# In[13]:


for row in rows:
    row_td = row.find_all('td')
print(row_td) #convert that list into dataframe
type(row_td) 


# In[14]:


str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells, 'lxml').get_text()
print(cleantext) #text cleaning


# In[16]:


import re

list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)  #using for loop
print(clean2)
type(clean2)


# In[17]:


df = pd.DataFrame(list_rows)
df.head(10)  #convert into dataframe


# In[18]:


df1 = df[0].str.split(',', expand = True)
df1.head(10)  #splitting with ,


# In[19]:


df1[0] = df1[0].str.strip('[')
df1.head(10)  #stripping with '['


# In[20]:


col_tables = soup.find_all('th')


# In[22]:


all_head = []
col_str = str(col_tables)
cleantext2 = BeautifulSoup(col_str, 'lxml').get_text()
all_head.append(cleantext2)
print(all_head)  


# In[24]:


df2 = pd.DataFrame(all_head)
df2.head() #creating different dfs


# In[25]:


df3 = df2[0].str.split(',',expand=True)
df3.head()


# In[26]:


frames = [df3, df1]
df4 = pd.concat(frames)
df4.head(10)


# In[27]:


df5 = df4.rename(columns = df4.iloc[0])
df5.head()


# In[28]:


df5.info()
df5.shape  #shape given to data columns


# In[29]:


df6 = df5.dropna(axis = 0, how = 'any')


# In[30]:


df7 = df6.drop(df6.index[0])
df7.head()


# In[34]:


df7.rename(columns = {'[Place' : 'Place'},inplace = True)
df7.rename(columns = {' Team]' : 'Team'},inplace = True)
df7.head()  #fixing df


# In[35]:


df7['Team'] = df7['Team'].str.strip(']')
df7.head() #stipped df7


# In[ ]:





# In[ ]:




