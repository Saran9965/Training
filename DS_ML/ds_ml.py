import pandas as pd
import numpy as np
data=pd.read_csv('Training/DS_ML/user_Data.csv')
#print(data)
data['Gender']=data['Gender'].map({'Male':0,'Female':1}).astype(int)    #change to convert male=0 & female=1
x=data.iloc[:,[2,3]].values # index using tables :userid=0,gender=1,age=2,e.salary=3,purchase=4
y=data.iloc[:,4].values
#print(data)
#print(y)

# Using Scikit learn
from sklearn.model_selection import train_test_split 
xtrain,xtest,ytrain,ytest=train_test_split(x, y, test_size = 0.25)
#print(xtrain)

from sklearn.preprocessing import StandardScaler        #standardscaler is a numeric values
sc_x= StandardScaler()
xtrain= sc_x.fit_transform(xtrain)
xtest = sc_x.transform(xtest)
print(xtrain[0:10, :])
print(xtest[0:10,:])
                           
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(xtrain, ytrain)

import pickle
with open('logistic_model.pkl','wb') as files:   # wb - write binary
    pickle.dump(classifier, files)
with open('logistic_model.pkl','rb') as f:
    classifier = pickle.load(f)
y=classifier.predict(xtest)
print(y)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(ytest, y)                   # confusion matrix
print("Confusion Matrix : \n" ,cm)

from sklearn.metrics import accuracy_score
print("Accurany : ", accuracy_score(ytest,y))      #accurate score


# support vector machines

# import pandas as pd
# import numpy as np
# data=pd.read_csv('Training/DS_ML/user_Data.csv')
# x=data.iloc[:,[2,3]].values # index using tables :userid=0,gender=1,age=2,e.salary=3,purchase=4
# y=data.iloc[:,4].values

# from sklearn.model_selection import train_test_split 
# xtrain,xtest,ytrain,ytest=train_test_split(x, y, test_size = 0.25)
# print(xtrain)

# from sklearn.preprocessing import StandardScaler        #standardscaler is a numeric values
# sc_x= StandardScaler()
# xtrain= sc_x.fit_transform(xtrain)
# xtest = sc_x.transform(xtest)
# print(xtrain[0:10, :])
# print(xtest[0:10,:])

# from sklearn.linear_model import LogisticRegression
# classifier = LogisticRegression(random_state=0)
# classifier.fit(xtrain, ytrain)
