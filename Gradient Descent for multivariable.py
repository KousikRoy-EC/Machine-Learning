#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import model_selection
training=np.loadtxt('train.csv', delimiter=',')
testing=np.loadtxt('test.csv', delimiter=',')


# In[2]:


def stepgd(x,y,learning_rate,m):
    slope_m=np.zeros(len(x[0]))
    for i in range(len(x)):
        X=x[i]
        Y=y[i]
        for j in range(len(X)):
            slope_m += (-2/len(x))*(Y-sum(m*X))*X[j]
        new_m=m-(learning_rate*slope_m)
    return new_m


# In[3]:


def gd(x,y,no_of_iter,learning_rate):
    m=np.zeros(len(x[0]))
    for i in range(no_of_iter):
        m=stepgd(x,y,learning_rate,m)
        print("cost of iteration ",i," is ",cost(m,x,y))
    return m


# In[12]:


def cost(m,x,y):
    total_cost=0
    for i in range(len(x)):
        total_cost+=(1/len(x))*((y[i]-sum(m*x[i]))**2)
    return total_cost


# In[37]:


def gradient(x,y):
    no_of_iter=500
    learning_rate=0.0005
    x=np.append(x,np.ones(len(x)).reshape(-1, 1), axis=1)
    m=gd(x,y,no_of_iter,learning_rate)
    return m


# In[38]:


x=training[:, :-1]
y=training[:, -1]
m=gradient(x, y)


# In[40]:


plt.plot(m)
print("The value of coeff m is  : ",m)


# In[ ]:





# In[ ]:




