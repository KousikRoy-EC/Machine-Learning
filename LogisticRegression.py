{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 234,
   "id": "2b9ddf81",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.datasets import load_breast_cancer\n",
    "from sklearn.linear_model import LogisticRegression;\n",
    "from sklearn import model_selection\n",
    "import numpy as np\n",
    "import math\n",
    "from sklearn import preprocessing\n",
    "data=load_breast_cancer()\n",
    "x_data=data.data\n",
    "y_data=data.target\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 235,
   "id": "fd40e829",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train, x_test, y_train, y_test=model_selection.train_test_split(x_data, y_data)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 236,
   "id": "856518c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "def gradient_descent(x_train, y_train,no_of_iter,learning_rate):\n",
    "    m=np.zeros(len(x_train[0]));\n",
    "    for i in range(no_of_iter):\n",
    "        m=step_gradient(x_train, y_train, learning_rate, m);\n",
    "        print(\"itr= \", i, \"cost=\", end=' ');\n",
    "        cost(x_train, y_train, m);\n",
    "    return m;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 237,
   "id": "367abf9f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def cost(x,y,m):\n",
    "    total_cost=0;\n",
    "    for i in range(len(x)):\n",
    "         total_cost+=math.log(1+(math.exp(sum(m*x[i]))))-y[i]*sum(m*x[i]);\n",
    "    print(total_cost);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 238,
   "id": "62055154",
   "metadata": {},
   "outputs": [],
   "source": [
    "def step_gradient(x, y, learning_rate, m):\n",
    "    slope_m=np.zeros(len(x[0]));\n",
    "    for i in range(len(x)):\n",
    "        X=x[i];\n",
    "        Y=y[i];\n",
    "        \n",
    "        for j in range(len(X)):\n",
    "            slope_m[j] += (-1/len(x))*(Y-(1/(1+math.exp(-sum(m*X)))))*X[j];\n",
    "            \n",
    "        new_m=m-learning_rate*slope_m;\n",
    "        return new_m;\n",
    "\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 251,
   "id": "7fde4218",
   "metadata": {},
   "outputs": [],
   "source": [
    "testing=x_test\n",
    "testing=scaler.transform(testing)\n",
    "pred=[]\n",
    "for i in testing:\n",
    "    if 1/(1+math.exp(-sum(m*i)))>0.5:\n",
    "        pred.append(1)\n",
    "    else:\n",
    "        pred.append(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 252,
   "id": "f92f346e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "score= 0.38461538461538464\n"
     ]
    }
   ],
   "source": [
    "total=0\n",
    "correct=0\n",
    "for i, j in zip(pred, y_test):\n",
    "    total+=1\n",
    "    if i==j:\n",
    "        correct+=1\n",
    "print('score=', correct/total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 249,
   "id": "744c37cf",
   "metadata": {},
   "outputs": [],
   "source": [
    "def run(x_train, y_train):\n",
    "    no_of_iter=50;\n",
    "    learning_rate=0.1;\n",
    "    m=gradient_descent(x_train, y_train,no_of_iter,learning_rate);\n",
    "    return m"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 250,
   "id": "f260c94c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "itr=  0 cost= 294.8525079276767\n",
      "itr=  1 cost= 294.4265671463692\n",
      "itr=  2 cost= 294.0028636011895\n",
      "itr=  3 cost= 293.5813843559621\n",
      "itr=  4 cost= 293.162116512652\n",
      "itr=  5 cost= 292.7450472122253\n",
      "itr=  6 cost= 292.3301636354982\n",
      "itr=  7 cost= 291.91745300395314\n",
      "itr=  8 cost= 291.50690258053817\n",
      "itr=  9 cost= 291.0984996704419\n",
      "itr=  10 cost= 290.6922316218476\n",
      "itr=  11 cost= 290.2880858266627\n",
      "itr=  12 cost= 289.8860497212308\n",
      "itr=  13 cost= 289.48611078702\n",
      "itr=  14 cost= 289.0882565512878\n",
      "itr=  15 cost= 288.69247458773094\n",
      "itr=  16 cost= 288.2987525171092\n",
      "itr=  17 cost= 287.9070780078514\n",
      "itr=  18 cost= 287.5174387766407\n",
      "itr=  19 cost= 287.1298225889795\n",
      "itr=  20 cost= 286.7442172597374\n",
      "itr=  21 cost= 286.36061065367437\n",
      "itr=  22 cost= 285.97899068595046\n",
      "itr=  23 cost= 285.59934532261434\n",
      "itr=  24 cost= 285.22166258107325\n",
      "itr=  25 cost= 284.84593053054186\n",
      "itr=  26 cost= 284.4721372924819\n",
      "itr=  27 cost= 284.10027104101255\n",
      "itr=  28 cost= 283.73032000331204\n",
      "itr=  29 cost= 283.3622724599973\n",
      "itr=  30 cost= 282.99611674549027\n",
      "itr=  31 cost= 282.6318412483645\n",
      "itr=  32 cost= 282.26943441167487\n",
      "itr=  33 cost= 281.9088847332771\n",
      "itr=  34 cost= 281.55018076612225\n",
      "itr=  35 cost= 281.1933111185446\n",
      "itr=  36 cost= 280.83826445452763\n",
      "itr=  37 cost= 280.48502949395976\n",
      "itr=  38 cost= 280.1335950128694\n",
      "itr=  39 cost= 279.7839498436545\n",
      "itr=  40 cost= 279.43608287528775\n",
      "itr=  41 cost= 279.08998305351633\n",
      "itr=  42 cost= 278.74563938104137\n",
      "itr=  43 cost= 278.4030409176895\n",
      "itr=  44 cost= 278.06217678056794\n",
      "itr=  45 cost= 277.7230361442053\n",
      "itr=  46 cost= 277.38560824068577\n",
      "itr=  47 cost= 277.0498823597644\n",
      "itr=  48 cost= 276.71584784897277\n",
      "itr=  49 cost= 276.383494113715\n",
      "[-0.00589945  0.00377665 -0.00617232 -0.00527051 -0.00410391 -0.01172016\n",
      " -0.00548109 -0.00812451 -0.00679576 -0.00355947 -0.01146041  0.00652882\n",
      " -0.00958188 -0.01189533 -0.00176218 -0.0110836  -0.0026399  -0.00773316\n",
      " -0.00375564 -0.00693043 -0.00687038  0.00570806 -0.00697542 -0.00700322\n",
      " -0.00387332 -0.01201069 -0.00314321 -0.00802291 -0.00776599 -0.00935303]\n"
     ]
    }
   ],
   "source": [
    "scaler=preprocessing.StandardScaler()\n",
    "scaler.fit(x_train)\n",
    "x_train=scaler.transform(x_train)\n",
    "m=run(x_train, y_train)\n",
    "print(m)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
