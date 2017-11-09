from sklearn.tree import DecisionTreeRegressor
import numpy as np
import pandas

tourist=pandas.read_csv("csvfile.csv")

mapping = {'Yes': 1, 'No': 0 }

columns = tourist.columns.tolist()

target="Rating"
columns=[c for c in columns if c not in["Rating","City"]]

for column in columns:
    tourist=tourist.replace({column: mapping})

train= tourist.sample(frac=0.8,random_state=1)
test=  tourist.loc[~tourist.index.isin(train.index)]

regr = DecisionTreeRegressor(max_depth=2)

regr.fit(train[columns],train[target])

print(regr.score(test[columns],test[target]))