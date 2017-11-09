from sklearn.tree import DecisionTreeRegressor
import numpy as np
import pandas
from sklearn.feature_selection import SelectKBest,mutual_info_regression

tourist=pandas.read_csv("csvfile.csv")

mapping = {'Yes': 1, 'No': 0 }

columns = tourist.columns.tolist()

target="Rating"
columns=[c for c in columns if c not in["Rating","City"]]

for column in columns:
    tourist=tourist.replace({column: mapping})
    

train= tourist.sample(frac=0.8,random_state=1)
test=  tourist.loc[~tourist.index.isin(train.index)]

trainAttributes=train[columns].astype('float64')
trainTarget=train[target].astype('float64')
testAttributes=test[columns].astype('float64')
testTarget=test[target].astype('float64')

selector = SelectKBest(mutual_info_regression,k=8).fit(trainAttributes,trainTarget)

newtrainX= selector.transform(trainAttributes)

newtestX=  selector.transform(testAttributes)

regr = DecisionTreeRegressor(max_depth=2)

regr.fit(newtrainX,trainTarget)

print(regr.score(newtestX,testTarget))