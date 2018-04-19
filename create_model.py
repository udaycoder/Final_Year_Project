from sklearn.tree import DecisionTreeRegressor
import numpy as np
import pandas
#from sklearn.feature_selection import SelectKBest
from sklearn import linear_model
import pickle
from sklearn.metrics import f1_score,precision_score,recall_score,accuracy_score,mean_squared_error,confusion_matrix,r2_score
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
import math
import matplotlib.pyplot as plt
import seaborn as sn

tourist=pandas.read_csv("csvfile.csv")

columns = tourist.columns.tolist()  

train= tourist.sample(frac=0.8,random_state=1)
test=  tourist.loc[~tourist.index.isin(train.index)]

target="Rating"
columns=[c for c in columns if c not in["Rating","City"]]  

trainAttributes=train[columns].astype('float64').apply(np.floor)
trainTarget=train[target].astype('float64').apply(np.floor)
testAttributes=test[columns].astype('float64').apply(np.floor)
testTarget=test[target].astype('float64').apply(np.floor)

count1=0
count2=0
count3=0
count4=0
count5=0

for x in trainTarget:
    if x==1:
       count1+=1
    if x==2:
        count2+=1
    if x==3:
        count3+=1
    if x==4:
        count4+=1

for x in testTarget:
    if x==1:
       count1+=1
    if x==2:
        count2+=1
    if x==3:
        count3+=1
    if x==4:
        count4+=1

testTarget=list(testTarget)

regr = DecisionTreeRegressor(max_depth=2)
lregr=linear_model.LinearRegression()
svm_clf = svm.SVC( kernel='rbf')
rndf_clf = RandomForestClassifier(max_depth=2, random_state=0)
gnb = GaussianNB()
mlpC = MLPClassifier(hidden_layer_sizes= 4 ) 
mlpR = MLPRegressor(hidden_layer_sizes= 4 )

mlpC.fit(trainAttributes,trainTarget)

# =============================================================================
filename = 'MachineLearningModel.pkl'
pickle.dump(regr, open(filename, 'wb'))
# =============================================================================

count=0;

predictedList=[]
actualList=[]

w, h = 4, 4;
Matrix = [[0 for x in range(w)] for y in range(h)]

print()
print("City\t\tActual\t\tPredicted")

unmodifiedpredictedList = []
unmodifiedactualList = []

for x in range(0,len(testTarget)):
    h=testAttributes.iloc[x]
    h=np.array(h).reshape(1,-1)
    p= int(math.floor(float(mlpC.predict(h))))
    a= int(math.floor(float(testTarget[x])))
# =============================================================================
#     p= float(rndf.predict(h))
#     a= float(testTarget[x])
# =============================================================================
    print(test['City'].iloc[x],"\t",testTarget[x],"\t",mlpC.predict(h))
    Matrix[p-1][a-1] += 1 
    predictedList.append(p)
    actualList.append(a)
    unmodifiedpredictedList.append(mlpC.predict(h))
    unmodifiedactualList.append(testTarget[x])
    #print(regr.predict(h)," ",testTarget[x])

print("R2 Score ", r2_score(actualList,predictedList))
print("Accuracy Score: ",accuracy_score(actualList,predictedList))
print("Mean Squared Error: ",mean_squared_error(actualList,predictedList))
print("F1_score: ",f1_score(actualList,predictedList,average="macro"))
print("Precision Score: ",precision_score(actualList,predictedList,average="macro"))
print("Recall Score: ",recall_score(actualList,predictedList,average="macro"))
# =============================================================================
print("Confusion Matrix: ")
for x in Matrix:
     print(x)
# =============================================================================

print("Number of 1",count1)
print("Number of 2",count2)
print("Number of 3",count3)
print("Number of 4",count4)

length = len(unmodifiedactualList)

for i in range(0,length):
    if unmodifiedactualList[i]>4 and unmodifiedactualList[i]<=5:
        plt.scatter(unmodifiedactualList[i],unmodifiedpredictedList[i],color="green")
    if unmodifiedactualList[i]>3 and unmodifiedactualList[i]<=4:
        plt.scatter(unmodifiedactualList[i],unmodifiedpredictedList[i],color="blue")
    if unmodifiedactualList[i]<=3:
        plt.scatter(unmodifiedactualList[i],unmodifiedpredictedList[i],color="red")
        
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.legend()
plt.savefig("actualVpredicted_scatterplot.png")
plt.show()

df_cm = pandas.DataFrame(Matrix, index = [i for i in "1234"],
                  columns = [i for i in "1234"])
plt.figure(figsize = (10,7))
conf_heat = sn.heatmap(df_cm, annot=True)
conf_heat.set_yticklabels(rotation=0,labels= [i for i in "4321"])
conf_heat.set_ylabel("Actual values")
conf_heat.set_xlabel("Predicted values")
heatfig = conf_heat.get_figure()
heatfig.savefig("confusionMatrix_heatMap.png")