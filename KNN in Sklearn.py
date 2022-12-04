#!/usr/bin/env python
# coding: utf-8

# In[12]:


from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt


# In[8]:


dataset=datasets.load_breast_cancer();
dataset.target


# In[9]:


X_train,X_test,Y_train,Y_test=train_test_split(dataset.data,dataset.target,test_size=0.2)


# In[10]:


clf=KNeighborsClassifier();
clf.fit(X_train,Y_train);


# In[11]:


clf.score(X_test,Y_test)


# In[16]:


for i in range(1,26,2):
    clf=KNeighborsClassifier(n_neighbors=i);
    score=cross_val_score(clf,X_train,Y_train);
    print(i,score.mean());


# In[19]:


x_axis=[];
y_axis=[];

for i in range(1,26,2):
    clf=KNeighborsClassifier(n_neighbors=i);
    score=cross_val_score(clf,X_train,Y_train);
    x_axis.append(i);
    y_axis.append(score.mean());
plt.plot(x_axis,y_axis);
plt.show()


# In[ ]:





# In[ ]:




