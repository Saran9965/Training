import pandas as pd
import numpy as np
data=pd.read_csv('datas/user_Data.csv')
#print(data)
data['Gender']=data['Gender'].map({'Male':0,'Female':1}).astype(int)    #change to convert male=0 & female=1
x=data.iloc[:,[2,3]].values # index using tables :userid=0,gender=1,age=2,e.salary=3,purchase=4
y=data.iloc[:,4].values
print(data)
print(y)