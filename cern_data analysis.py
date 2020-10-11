#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os


# # reading Data from textfile and converting to pickle format

# In[2]:


address="F:/old destop/thesis/cern data analysis/"
filelist = ['File1.txt',"File2.txt","File3.txt","File4.txt","File5.txt","File6.txt"]
filelist=[address+i for i in filelist]
df= pd.concat([pd.read_table(item,delim_whitespace=True,names=("Meter_ID","Date_time","Consumption(Khw)")) for item in (filelist[:1])])
# df.to_pickle("F:/old destop/thesis/cern data analysis data.pkl")


# # reading pickle Data

# In[ ]:


df=pd.read_pickle("F:/old destop/thesis/cern data analysis/data.pkl")
dd.info()
# df=dd.head(10000)
# dd.head()


# # Convert Date-Time to proper format

# In[ ]:


from datetime import datetime

def convertToDatetime(date):
    date_int=int(date[:3])
    time_int=int(date[3:5])
    timestamp = 1230796800 + (date_int - 195) * 86400 + time_int * 1800
    return datetime.fromtimestamp(timestamp)

df['Date'] = df.apply(lambda row: str(convertToDatetime(str(row['Date_time'])).date()), axis = 1)

df['time'] = df.apply(lambda row: str(convertToDatetime(str(row['Date_time'])).time()), axis = 1)
df.drop("Data_time",axis=1,inplace=True)

df.info()
df.head()


# # setting meter_id & date as index 

# In[ ]:


test=df.pivot_table('Consumption(Khw)',index=['Meter_ID','Date'],columns='time')
test.head()

