from sklearn.tree import DecisionTreeRegressor
import numpy as np
import pandas

regr = DecisionTreeRegressor(max_depth=2)

regr.fit(train_attributes,train_target)

print(regr.score(test_attributes,test_target))