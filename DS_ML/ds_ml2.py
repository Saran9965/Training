import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

# stratify- balanced value
data=pd.read_csv('Training/DS_ML/app_review.csv')   #Training/DS_ML
data.head()
print(data)

def preprocess_data(data):
    #remove package name as it's not relevant
    data=data.drop('package_name',axis=1)
    #convert text to lowercase
    data['review']=data['review'].str.strip().str.lower()
    return data
data=preprocess_data(data)
print(data.head())

# split training and testing data
x=data['review']    #training data
y=data['polarity']  #label
x,x_test,y,y_test=train_test_split(x,y,stratify=y,test_size=0.25,random_state=0)

# vectorize text reviews to numbers
vec=CountVectorizer(stop_words='english')
x=vec.fit_transform(x).toarray()
x_test=vec.transform(x_test).toarray()

from sklearn.naive_bayes import MultinomialNB
model=MultinomialNB()
model.fit(x,y)
print(model.score(x_test,y_test))

print(model.predict(vec.transform(['love this app simply awasome'])))   #[1] is a positive review  //sentimental analysis

print(model.predict(vec.transform(['its detting stuck alot while using the app']))) #[0] is negative review