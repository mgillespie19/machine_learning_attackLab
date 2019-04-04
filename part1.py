#ignore complex numbers going into the matrix

import sklearn
import numpy as np
import csv

f = open("Lab8_feature_data.csv")

data = [row for row in csv.reader(f)]
x = np.delete(data, np.s_[72:74], axis=1)
y = np.delete(data, np.s_[0:73], axis=1)

for i in range(0, len(data)):
    for j in range(0, len(data[i]) - 2):
        x[i][j] = data[i][j].replace('(','').replace(')','')


# PROOF Y IS WORKING
# for key in y:
#     print(key[0])

# PROOF X IS WORKING
# for row in x:
#     print("---------NEW ROW--------")
#     for cell in row:
#         print(cell)
