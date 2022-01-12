#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn import datasets
boston=datasets.load_boston()
x=boston.data
y=boston.target


# In[63]:


x.shape


# In[66]:


import pandas as pd
df=pd.DataFrame(x)
df.columns=boston.feature_names
for i in range (0,14):
    df[i]=df[df.columns[i]]**2;
# df["crim_crim"]=df.CRIM **2;
x2=df.values;


# In[67]:


df.describe()
x2.shape


# In[68]:


from sklearn import model_selection
x_train,x_test,y_train,y_test = model_selection.train_test_split(x,y , random_state=0)
x2_train,x2_test,y2_train,y2_test = model_selection.train_test_split(x2,y ,random_state=0)


# In[70]:


from sklearn.linear_model import LinearRegression
alg1= LinearRegression()
alg2= LinearRegression()


# In[71]:


alg1.fit(x_train,y_train)
alg2.fit(x2_train,y2_train)


# In[74]:


y_predict=alg1.predict(x_test)
train_score = alg1.score(x_train,y_train)
test_score = alg1.score(x_test,y_test)
print("Train Score",train_score);
print("Test Score",test_score);

y2_predict=alg2.predict(x2_test)
train2_score = alg2.score(x2_train,y2_train)
test2_score = alg2.score(x2_test,y2_test)
print("Train2 Score",train2_score);
print("Test2 Score",test2_score);


# In[78]:


import matplotlib.pyplot as plt
plt.scatter(y2_test,y2_predict);
plt.plot(y2_test,y2_predict)
plt.show();


# In[ ]:




