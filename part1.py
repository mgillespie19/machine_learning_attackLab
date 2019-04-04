#ignore complex numbers going into the matrix

import sklearn
import numpy as np
import csv

f = open("Lab8_feature_data.csv")

data = [row for row in csv.reader(f)]

for row in data:
    print("--------NEW ROW--------")
    for cell in row:
        scrubbed_cell = cell.replace('(','').replace(')','')
        print( scrubbed_cell )
