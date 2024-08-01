# KNN (K-nearest neighbors)

import pandas as pd
import numpy as np
data_set=pd.read_csv('Training/DS_ML/user_Data.csv')
x=data_set.iloc[:,[2,3]].values
y=data_set.iloc[:,4].values
print(x[:10])

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x, y, test_size = 0.25)

from sklearn.preprocessing import StandardScaler
st_x=StandardScaler()
x_train=st_x.fit_transform(x_train)
x_test=st_x.transform(x_test)

from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5,metrics='minkowski',p=2)
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)
print(y_pred)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
print(cm)
from sklearn.metrics import accuracy_score
print("ACCURACY:",accuracy_score(y_test,y_pred))

