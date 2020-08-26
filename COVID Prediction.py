#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Install a pip package in the current Jupyter kernel
import sys
get_ipython().system(u'{sys.executable} -m pip install numpy')
get_ipython().system(u'{sys.executable} -m pip install seaborn')
get_ipython().system(u'{sys.executable} -m pip install pandas')


# In[10]:


pip uninstall scipy


# In[11]:


pip install scipy


# In[ ]:





# In[15]:


import pandas as pd
import numpy as ny
import seaborn as sns


# In[133]:


from matplotlib import dates
import datetime


# In[84]:


import matplotlib.pyplot as plt


# In[37]:


raw_data = pd.read_csv('train.csv', low_memory=False)


# In[38]:


raw_data


# In[39]:


submission = pd.read_csv('submission.csv', low_memory=False)


# In[41]:


submission


# In[66]:


train_data = raw_data.sort_values(['Country_Region','County','Province_State','Date'])


# In[43]:


train_data


# In[67]:


train_data['Province_State'].fillna('', inplace=True)


# In[125]:


train_df = train_data


# In[127]:


train_data


# In[126]:


train_df['Date'] = pd.to_datetime(train_df['Date'])
train_df = train_df[train_df['Date']<'2020-05-11']


# In[103]:


train_df = train_df.sort_values(['Country_Region','Province_State','Date'])


# In[120]:


train_df= train_df.groupby(['Date','Country_Region', 'Province_State','Target']).sum('TargetValue')


# In[128]:


cases_df = train_df[train_df['Target'] =='ConfirmedCases']
fatalities_df = train_df[train_df['Target'] =='Fatalities']


# In[130]:


cases_df
fatalities_df


# In[138]:


def plot_trend_by_date(df,value ='ConfirmedCases',title=None, mode='subplot'):
    ax = plt.gca()
    xaxis = df['Date'].tolist()
    if value == 'ConfirmedCases':
        case_df = df[df['Target'] =='ConfirmedCases']
        yaxis = case_df['TargetValue']
    else:
        fatalities_df = df[df['Target'] =='Fatalities']
        yaxis = fatalities_df['TargetValue']
        
    xaxis = dates.date2num(xaxis)
    hfmt = dates.DateFormatter('%m\n%d')
    ax.xaxis.set_major_formatter(hfmt)

    plt.xlabel('Date')
    if value == 'ConfirmedCases':
        plt.ylabel('ConfirmedCases')
    else:
        plt.ylabel('Fatalities')
    plt.title(title)
    plt.plot(xaxis, yaxis)
    plt.tight_layout()

    plt.show()


# In[141]:


for country in train_df['Country_Region'].unique():
    country_pd_train = train_df[train_df['Country_Region']==country]
    if country_pd_train['Province_State'].isna().unique()==True:
        plt_title = country+' ConfirmedCase'
        plot_trend_by_date(country_pd_train,value = 'ConfirmedCases',title = plt_title)
    else:
        state_count = len(country_pd_train['Province_State'].unique())
        row = state_count//4+1
        column = 4
        fig =plt.figure(figsize = (4*6.4,row*4.8))
        index = 1
        for state in country_pd_train['Province_State'].unique():
            state_pd = country_pd_train[country_pd_train['Province_State']==state]
            plt_title = country+'  '+state+' ConfirmedCases'
            ax = fig.add_subplot(row,column,index)
            cases_pd = state_pd[state_pd['Target']=='ConfirmedCases']
            xaxis = cases_pd['Date'].tolist()
            yaxis = cases_pd['TargetValue']
            xaxis = dates.date2num(xaxis)
            hfmt = dates.DateFormatter('%m\n%d')
            ax.xaxis.set_major_formatter(hfmt)

            plt.xlabel('Date')
            plt.ylabel('ConfirmedCases')
            plt.title(plt_title)
            ax.plot(xaxis, yaxis)
            index += 1
        plt.show() 
            #plot_trend_by_date(state_pd,value = 'ConfirmedCases',title = plt_title)


# In[142]:


for country in train['Country_Region'].unique():
    country_pd_train = train[train['Country_Region']==country]
    if country_pd_train['Province_State'].isna().unique()==True:
        plt_title = country+' Fatalities'
        plot_trend_by_date(country_pd_train,value = 'Fatalities',title = plt_title)
    else:
        state_count = len(country_pd_train['Province_State'].unique())
        row = state_count//4+1
        column = 4
        fig =plt.figure(figsize = (4*6.4,row*4.8))
        index = 1
        for state in country_pd_train['Province_State'].unique():
            state_pd = country_pd_train[country_pd_train['Province_State']==state]
            plt_title = country+'  '+state+' Fatalities'
            ax = fig.add_subplot(row,column,index)
            fatalities_pd = state_pd[state_pd['Target']=='Fatalities']
            xaxis = fatalities_pd['Date'].tolist()
            yaxis = fatalities_pd['TargetValue']
            xaxis = dates.date2num(xaxis)
            hfmt = dates.DateFormatter('%m\n%d')
            ax.xaxis.set_major_formatter(hfmt)

            plt.xlabel('Date')
            plt.ylabel('Fatalities')
            plt.title(plt_title)
            ax.plot(xaxis, yaxis)
            index += 1
        plt.show() 
            #plot_trend_by_date(state_pd,value = 'ConfirmedCases',title = plt_title)


# In[80]:


plt.plot(x=f_country['Date'],y=f_country['TargetValue'], color=f_country['Target'])
plt.title('COVID Trend in China', fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('TargetValue', fontsize=14)
plt.grid(True)
plt.show()


# In[82]:


plt.plot(x=f_country['Country_Region'],y=f_country['TargetValue'], color=f_country['Target'])


# In[ ]:





# In[ ]:




