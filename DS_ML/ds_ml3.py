# Random forest

from sklearn import datasets
iris=datasets.load_iris()   # iris is a dataset

import pandas as pd
data=pd.DataFrame({
    'sepal length':iris.data[:,0],
    'sepal width':iris.data[:,1],
    'petal length':iris.data[:,2],
    'petal width':iris.data[:,3],
    'species':iris.target
})
data.head()

from sklearn.model_selection import train_test_split
x=data[['sepal length','sepal width','petal length','petal width']]
y=data['species'] #labels
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

from sklearn.ensemble import RandomForestClassifier
clf=RandomForestClassifier(n_estimators=100)
clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)

from sklearn import metrics
print('ACCURACY',metrics.accuracy_score(y_test,y_pred))