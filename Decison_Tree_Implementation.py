#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.tree import export_graphviz
from IPython.display import Image  
import pydotplus


# In[2]:


iris=datasets.load_iris()
x_train, x_test, y_train, y_test=train_test_split(iris.data, iris.target)


# In[3]:


clf=DecisionTreeClassifier()
clf.fit(x_train,y_train)


# In[4]:


y_train_pred=clf.predict(x_train)
y_test_pred=clf.predict(x_test)


# In[7]:


dot_data=export_graphviz(clf,out_file=None,feature_names=iris.feature_names,class_names=iris.target_names)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf('iris.pdf')


# In[5]:


confusion_matrix(y_train,y_train_pred)


# In[6]:


confusion_matrix(y_test,y_test_pred)

