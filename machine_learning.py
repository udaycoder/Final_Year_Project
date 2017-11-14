from sklearn.tree import DecisionTreeRegressor
import numpy as np
import pandas
from sklearn.feature_selection import SelectKBest,mutual_info_regression
from sklearn import linear_model
import math
from sklearn.metrics import f1_score,precision_score,recall_score,accuracy_score

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

regr = DecisionTreeRegressor(max_depth=2)
#regr=linear_model.LinearRegression()

regr.fit(trainAttributes,trainTarget)

count=0;

predictedList=[]
actualList=[]

for x in range(0,len(testTarget)):
    h=testAttributes.iloc[x]
    h=np.array(h).reshape(1,-1)
    p= int(round(float(regr.predict(h))))
    a= int(round(float(testTarget[x])))
    predictedList.append(p)
    actualList.append(a)
    #print(regr.predict(h)," ",testTarget[x])

print("Accuracy Score: ",accuracy_score(actualList,predictedList))
print("F1_score: ",f1_score(actualList,predictedList,average="macro"))
print("Precision Score: ",precision_score(actualList,predictedList,average="macro"))
print("Recall Score: ",recall_score(actualList,predictedList,average="macro"))
#print(regr.score(newtestX,testTarget))