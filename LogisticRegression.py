from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression;
from sklearn import model_selection
import numpy as np
import math
from sklearn import preprocessing
data=load_breast_cancer()
x_data=data.data
y_data=data.target


x_train, x_test, y_train, y_test=model_selection.train_test_split(x_data, y_data)


def gradient_descent(x_train, y_train,no_of_iter,learning_rate):
    m=np.zeros(len(x_train[0]));
    for i in range(no_of_iter):
        m=step_gradient(x_train, y_train, learning_rate, m);
        print("itr= ", i, "cost=", end=' ');
        cost(x_train, y_train, m);
   return m;
   
   
   
def cost(x,y,m):
    total_cost=0;
    for i in range(len(x)):
         total_cost+=math.log(1+(math.exp(sum(m*x[i]))))-y[i]*sum(m*x[i]);
    print(total_cost);
    
    
    
    
def step_gradient(x, y, learning_rate, m):
    slope_m=np.zeros(len(x[0]));
    for i in range(len(x)):
        X=x[i];
        Y=y[i];
        
        for j in range(len(X)):
            slope_m[j] += (-1/len(x))*(Y-(1/(1+math.exp(-sum(m*X)))))*X[j];
            
        new_m=m-learning_rate*slope_m;
        return new_m;
       
       
       
       
def run(x_train, y_train):
    no_of_iter=50;
    learning_rate=0.1;
    m=gradient_descent(x_train, y_train,no_of_iter,learning_rate);
    return m
   
   
scaler=preprocessing.StandardScaler()
scaler.fit(x_train)
x_train=scaler.transform(x_train)
m=run(x_train, y_train)
print(m)
       
       
       
testing=x_test
testing=scaler.transform(testing)
pred=[]
for i in testing:
    if 1/(1+math.exp(-sum(m*i)))>0.5:
        pred.append(1)
    else:
        pred.append(0)
      
      
      
      
total=0
correct=0
for i, j in zip(pred, y_test):
    total+=1
    if i==j:
        correct+=1
print('score=', correct/total)

