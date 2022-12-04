#!/usr/bin/env python
# coding: utf-8

# In[22]:


from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from collections import Counter;


# In[33]:


dataset=datasets.load_breast_cancer();
X_train,X_test,Y_train,Y_test=train_test_split(dataset.data,dataset.target,test_size=0.2,random_state=0);


# In[17]:


def train(X,Y):
    return;
# here we are not doing anything in training we can classify the classes in training


# In[28]:


def predict_one(X_train,Y_train,X_test,K):
    distances=[];
    for i in range(len(X_train)):
        distance=((X_train[i,:]-X_test)**2).sum();
        distances.append([distance,i]);
    distance=sorted(distances);
    
    target=[];
    
    for i in range(K):
        index_of_predicting_class=distance[i][1];
        target.append(Y_train[index_of_predicting_class]);
    return Counter(target).most_common(1)[0][0];


# In[24]:


def predict(X_train,Y_train,X_tests_data,K):
    predictions=[];
    for x_test in X_tests_data:
        predict=predict_one(X_train,Y_train,x_test,K);
        predictions.append(predict)
    return predictions;


# In[29]:


# lets assume k to be 7 we can find optimal k using cross validation 
Y_predict=predict(X_train,Y_train,X_test,7);
print(accuracy_score(Y_test,Y_predict));


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




