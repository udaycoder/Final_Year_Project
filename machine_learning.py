from sklearn.tree import DecisionTreeRegressor
import numpy as np
import pandas
from sklearn.feature_selection import SelectKBest,mutual_info_regression
from sklearn import linear_model
import math

tourist=pandas.read_csv("csvfile.csv")

mapping = {'Yes': 1, 'No': 0 }

columns = tourist.columns.tolist()

target="Rating"
columns=[c for c in columns if c not in["Rating","City"]]

for column in columns:
    tourist=tourist.replace({column: mapping})
    

train= tourist.sample(frac=0.8)
test=  tourist.loc[~tourist.index.isin(train.index)]

trainAttributes=train[columns].astype('float64')
trainTarget=train[target].astype('float64')
testAttributes=test[columns].astype('float64')
testTarget=test[target].astype('float64')
testTarget=list(testTarget)

selector = SelectKBest(mutual_info_regression,k=10).fit(trainAttributes,trainTarget)

ids_selected = selector.get_support(indices=True)

selectedcolumns=trainAttributes.columns[ids_selected]

print("The columns used for training are: ")
for x in selectedcolumns:
    print(x)

newtrainX= selector.transform(trainAttributes)

newtestX=  selector.transform(testAttributes)

regr = DecisionTreeRegressor(max_depth=2)
#regr=linear_model.LinearRegression()

regr.fit(newtrainX,trainTarget)

count=0;

for x in range(0,len(testTarget)):
    h=newtestX[x,0:].reshape(1,-1)
    if(int(round(float(regr.predict(h))))==int(round(float(testTarget[x]))))    :
        count+=1
    #print(regr.predict(h)," ",testTarget[x])

print("\nAccuracy: ",(count/len(testTarget))*100,"%")

#print(regr.score(newtestX,testTarget))