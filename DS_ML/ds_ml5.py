#matplotlib

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt     #pip install matplotlib
# from sklearn.cluster import KMeans 
# x=-2*np.random.rand(100,2)
# print(x)
# x1=1+2*np.random.rand(50,2)
# print(x1)
# x[50:100,:]=x1
# print(x)
# plt.scatter(x[:,0],x[:,1],50,c='b')
# print(plt.show)

# Kmean=KMeans(n_clusters=2)
# Kmean.fit(x)
# Kmean.cluster_centers_
# plt.scatter(x[:,0],x[:,1],s=50,c='b')                   # s=size, c=color
# plt.scatter(-0.97357564,-1.1674846,s=200,c='g',marker='s')
# plt.scatter(1.97137568,1.9741809,s=200,c='r',marker='s')
# plt.show()





# hierarchical cluster  

# import numpy as np
# x=np.array([[5,3],
# [10,15],
# [15,12],
# [24,10],
# [30,30],
# [85,70],
# [71,80],
# [60,78],
# [70,55],
# [80,91],])
# import matplotlib.pyplot as plt
# labels=range(1,11)
# plt.figure(figsize=(10,7))
# plt.subplots_adjust(bottom=0.1)
# plt.scatter(x[:,0],x[:,1],label='True position')
# for label,x,y in zip(labels,x[:,0],x[:,1]):
#     plt.annotate(
#         label,xy=(x,y),xytext=(-3,3),
#         textcoords='offset points',ha='right',va='bottom')
# plt.show()




# scipy -scientific python

from  scipy.cluster.hierarchy import dendrogram,linkage
from matplotlib import pyplot as plt
x=([[5,3],
[10,15],
[15,12],
[24,10],
[30,30],
[85,70],
[71,80],
[60,78],
[70,55],
[80,91],])
linked=linkage(x,'single')
labellist=range(1,11)
plt.figure(figsize=(10,7))
dendrogram(linked,orientation='top',labels=labellist,distance_sort='descending',show_leaf_counts=True)
plt.show()

