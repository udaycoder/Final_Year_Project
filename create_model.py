from sklearn.tree import DecisionTreeRegressor
import numpy as np
import pandas
from sklearn.feature_selection import SelectKBest
from sklearn import linear_model
import pickle
from sklearn.metrics import f1_score,precision_score,recall_score,accuracy_score,mean_squared_error,confusion_matrix,r2_score
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
import math

tourist=pandas.read_csv("csvfile.csv")

columns = tourist.columns.tolist()

target="Rating"
columns=[c for c in columns if c not in["Rating","City"]]
    

train= tourist.sample(frac=0.8,random_state=1)
test=  tourist.loc[~tourist.index.isin(train.index)]

trainAttributes=train[columns].astype('float64').apply(np.floor)
trainTarget=train[target].astype('float64').apply(np.floor)
testAttributes=test[columns].astype('float64').apply(np.floor)
testTarget=test[target].astype('float64').apply(np.floor)
testTarget=list(testTarget)

regr = DecisionTreeRegressor(max_depth=2)
lregr=linear_model.LinearRegression()
svm_clf = svm.SVC( kernel='rbf')
rndf_clf = RandomForestClassifier(max_depth=2, random_state=0)

svm_clf.fit(trainAttributes,trainTarget)

filename = 'MachineLearningModel.pkl'
pickle.dump(regr, open(filename, 'wb'))

count=0;

predictedList=[]
actualList=[]

w, h = 5, 5;
Matrix = [[0 for x in range(w)] for y in range(h)]

print()
print("Actual\tPredicted")

for x in range(0,len(testTarget)):
    h=testAttributes.iloc[x]
    h=np.array(h).reshape(1,-1)
    p= int(math.floor(float(svm_clf.predict(h))))
    a= int(math.floor(float(testTarget[x])))
# =============================================================================
#     p= float(regr.predict(h))
#     a= float(testTarget[x])
# =============================================================================
    print(a,"\t",p)
    Matrix[a-1][p-1] += 1 
    predictedList.append(p)
    actualList.append(a)
    #print(regr.predict(h)," ",testTarget[x])

#print("r2 score: ",r2_score(actualList,predictedList))
print("Accuracy Score: ",accuracy_score(actualList,predictedList))
print("Mean Squared Error: ",mean_squared_error(actualList,predictedList))
print("F1_score: ",f1_score(actualList,predictedList,average="macro"))
print("Precision Score: ",precision_score(actualList,predictedList,average="macro"))
print("Recall Score: ",recall_score(actualList,predictedList,average="macro"))

print("Confusion Matrix: ")
for x in Matrix:
     print(x)

#print(regr.score(newtestX,testTarget))