#matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt     #pip install matplotlib
from sklearn.cluster import KMeans 
x=-2*np.random.rand(100,2)
print(x)
x1=1+2*np.random.rand(50,2)
print(x1)
x[50:100,:]=x1
print(x)
plt.scatter(x[:,0],x[:,1],50,c='b')
print(plt.show)

Kmean=KMeans(n_clusters=2)
Kmean.fit(x)
Kmean.cluster_centers_
plt.scatter(x[:,0],x[:,1],s=50,c='b')                   # s=size, c=color
plt.scatter(-0.97357564,-1.1674846,s=200,c='g',marker='s')
plt.scatter(1.97137568,1.9741809,s=200,c='r',marker='s')
plt.show()
# print(plt.shoW())
# Kmean.labels_