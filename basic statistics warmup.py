import numpy as np
from scipy import stats

n = int(input())
list_array = input().split()
listed_array = []
for i in list_array :
    listed_array.append(int(i))
m = np.mean(listed_array)
print(round(m,1))
m = np.median(listed_array)
print(round(m,1))
print(stats.mode(listed_array)[0][0])
m = np.std(listed_array)
print(round(m,1))
