#ignore complex numbers going into the matrix

import sklearn
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import csv

f = open("Lab8_feature_data.csv")
f.readline()

data = [row for row in csv.reader(f)]
for i in range(0, len(data)):
    for j in range(0, len(data[i])):
        data[i][j] = data[i][j].replace('(','').replace(')','')
        data[i][j] = np.complex(data[i][j]).real

data = preprocessing.scale(data)

x = np.delete(data, np.s_[71:73], axis=1)
y = np.delete(data, np.s_[0:73], axis=1)

x_test = x[23552:29539]
x_train = x[0:23552]
y_test = y[23552:29539]
y_train = y[0:23552]

print(y_test)

# linreg = RandomForestRegressor(oob_score=True)
#
# linreg.fit(x_train, y_train)
# y_pred = linreg.predict(x_test)
# print(y_pred)

# PROOF Y IS WORKING
# for key in y:
#     print(key[0])

# PROOF X IS WORKING
# for row in x:
#     print("---------NEW ROW--------")
#     for cell in row:
#         print(cell)
