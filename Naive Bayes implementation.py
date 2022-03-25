#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np


# In[21]:


def fit(X_train,Y_train):
    result={}
    class_values=set(Y_train);
    for current_class in class_values:
        result[current_class]={}
        result["total_data"]=len(Y_train)
        current_class_row=(Y_train==current_class)
        X_train_current=X_train[current_class_row] 
        Y_train_current=Y_train[current_class_row]
        num_features=X_train.shape[1]
        result[current_class]["total_count"]=len(Y_train_current)
        for j in range(1,num_features+1):
            result[current_class][j]={}
            all_possible_val=set(X_train[:,j-1]);
            for current_val in all_possible_val:
                  result[current_class][j][current_val]=(X_train_current[:,j-1] == current_val).sum()
    return result


# In[13]:


def predict(dictionary,X_test):
    y_predict=[];
    for i in X_test:
        x_class=predictClass(dictionary,i)
        y_predict.append(x_class)
    return y_predict


# In[24]:


def predictClass(dictnary,x):
    classes=dictnary.keys()
    best_p=-1000;
    best_class=-1
    first_run=True
    for current_class in classes:
        if(current_class=="total_data"):
            continue;
        p=probability(dictnary,x,current_class)
        if(first_run or p>best_p):
            best_p=p
            best_class=current_class
        first_run=False
    return best_class


# In[26]:


def probability(dictnary,x,current_class):
    output=np.log(dictnary[current_class]["total_count"])-np.log(dictnary["total_data"])
    num_features=len(dictionary[current_class].keys())-1;
    for i in range(1,num_features+1):
        xj=x[i-1]
        count_num_with_xj=dictnary[current_class][i][xj]+1
        count_deno=dictnary[current_class]["total_count"] + len(dictnary[current_class][i].keys())
        current_probab=np.log(count_num_with_xj)-np.log(count_deno)
        output=output + current_probab;
    return output
    


# In[16]:


def makeLabelled(column):
    second_limit = column.mean()
    first_limit = 0.5 * second_limit
    third_limit = 1.5*second_limit
    for i in range (0,len(column)):
        if (column[i] < first_limit):
            column[i] = 0
        elif (column[i] < second_limit):
            column[i] = 1
        elif(column[i] < third_limit):
            column[i] = 2
        else:
            column[i] = 3
    return column


# In[17]:


from sklearn import datasets
iris = datasets.load_iris()
X = iris.data
Y = iris.target


# In[18]:


for i in range(0,X.shape[-1]):
    X[:,i] = makeLabelled(X[:,i])


# In[33]:


from sklearn import model_selection
X_train,X_test,Y_train,Y_test = model_selection.train_test_split(X,Y,test_size=0.25)


# In[34]:


dictionary = fit(X_train,Y_train)


# In[35]:


Y_pred = predict(dictionary,X_test)


# In[36]:


from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(Y_test,Y_pred))
print(confusion_matrix(Y_test,Y_pred))

