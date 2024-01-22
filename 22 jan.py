#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing the required libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# In[2]:


sns.get_dataset_names()


# In[3]:


# loading dataset 
df= sns.load_dataset("iris")


# In[4]:


df


# In[5]:


df.species.unique()


# In[6]:


df.species.value_counts()


# In[7]:


df.head()


# In[8]:


# Line plots are effective for showing the relationship between two variables and how one variable changes in response to the other.
sns.lineplot(x='sepal_length', y='sepal_width', data=df, ci=None) #Confidence interval
plt.show()


# In[9]:


### Line plot 
sns.lineplot(x='sepal_length', y='sepal_width', data=df,hue='species', ci=None)
plt.show()


# In[10]:


# continuous and categorical feature
sns.lineplot(x='sepal_width', y='species', data=df, hue='species', ci=None)
plt.show()


# In[11]:


## Scatter plot( Scatter plots are useful for visualizing the distribution and correlation of data points.)
sns.scatterplot(x='sepal_length',y='sepal_width',data=df, hue='species')
plt.title("Scatter plot")
plt.show()


# In[12]:


df.head()


# In[13]:


## Bar plot (categorical estimate plot)
##A barplot is basically used to aggregate the categorical data according to some methods and by default its the mean. 
##It can also be understood as a visualization of the group by action. 
#To use this plot we choose a categorical column for 
##the x axis and a numerical column for the y axis and we see that it 
# creates a plot taking a mean per categorical column. 

sns.barplot(x='species', y='sepal_length', data=df)
plt.show()


# In[14]:


## Count Plot  value_count()
##A countplot basically counts the categories and returns a 
# count of their occurrences. 
sns.countplot(x='species', data=df)
plt.show()


# In[15]:


df


# In[16]:


## Box plot
##A boxplot is sometimes known as the box and whisker plot.It shows the 
#distribution of the quantitative data 
## that represents the comparisons between variables. boxplot shows the 
#quartiles of the dataset while the whiskers extend to
## show the rest of the distribution i.e. the dots indicating the 
#presence  of outliers.
sns.boxplot(x='sepal_width',data=df)
plt.show()


# In[17]:


sns.boxplot(x='species', y='sepal_width', data=df)
plt.show()
# Checking outliers in each category with respect to sepal width.


# In[ ]:




