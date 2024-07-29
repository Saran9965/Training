#  py -m pip install pandas     (or)    python -m pip install pandas

# PANDAS 
# import pandas as pd
# lst = ['Geeks', 'For', 'Geeks', 'is', 
#             'portal', 'for', 'Geeks']
# df = pd.DataFrame(lst)
# print(df)

# creating a table using dataframes(row&columns)
# import pandas as pd
# 'A B C D E'.split()
# data=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
# df=pd.DataFrame(data,index='A B C D E'.split(),columns =['W','X','Y','Z'])

# df['S']=df['W']+df['Y']+df['X']+df['Z']     #add columns
# df['G']=[99,98,97,96,95]                    # add rows
# print(df)

# ||ly add a colums & rows
# newind='CA NY WY OR CO'.split()
# df['States']=newind
# print(df)

# df.drop('G',axis=1,inplace=True)  #delete a columns (inplace=True)permantely
# df.drop('E',inplace=True)         #delete a rows (inplace=True)permantely
#print(df)

#print(df['X']) #particular row & columns

# sa=df.loc['A']   # select particular row and columns
# s=df.iloc[1]   #select particular row using index number

# i=df.loc['B','Y']   #using index to particular data
#print(i)

#print(df.loc[['A','B'],['W','Y']]) # box to using index

# c=df[df['Y']>10]['X'] # conditional statement
# c1=df[(df['Y']>12) & (df['Y']>15)]
# c2=df[(df['Y']>12) | (df['Y']>15)]
# print(c1)
# print(c2)

# a=pd.Series([2,4,6],index=[0,1,2])
# b=pd.Series([1,3,5],index=[1,2,3])
# print(a+b)
# data1=[1,2,3],[4,5,6]
# a1=pd.DataFrame(data1,columns=list('AB'))
# print(a1)

# using Numpy
import pandas as pd
import numpy as np
df=pd.DataFrame({'A':[1,2,np.nan],
                 'B':[5,np.nan,np.nan], # np.nan it can contains with null(NaN) doen't contain 0
                 'C':[1,2,3]})
print(df)
df['B']=df['B'].fillna(value=0)# default can assign with 0
print(df)



 https://github.com/Saran9965/Training.git







#student details
# print('STUDENT DETAILS.....')
# import pandas as pd
# '1,2,3'.split()
# data=[['raj',20,'mca','chennai'],['sam',21,'mba','salem'],['tom',22,'msc','trichy']]
# df=pd.DataFrame(data,index='1 2 3'.split(),columns =['name','age','dept','address'])
# print(df)
# df['fname']=['R','S','T']    #add columns
# print(df)

