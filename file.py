import numpy as np
from matplotlib import pyplot as plt 
import csv

with open('iris.data', 'r') as f:
    reader = csv.reader(f)
    csv_data = list(reader)
data = np.array(csv_data)
names = np.array(data[:, 4])
data = np.array(data[:, :4], dtype=float)

#HISTOGRAM
# for var_id in range(4):
    # plt.figure(var_id)
    # plt.hist(data[:, var_id], bins=20)
    # plt.show()

for var_id in range(4):
    val = data[:,var_id]
    m = np.mean(val)
    std = np.std(val)
    data[:, var_id] -= m
    data[:, var_id] /= std

def cov(i, j):
    n = len(data)
    return np.sum(data[:, i] * data[:, j]) * (1/n-1)

mat = []
for i in range(4):
    cur = []
    for j in range(4):
        cur.append(cov(i,j))
    mat.append(cur)
print(mat)
print(np.cov(np.transpose(data)))
