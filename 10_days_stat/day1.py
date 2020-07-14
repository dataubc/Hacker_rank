import numpy as np
from scipy import stats

N = int(input())

list_n = list(map(int,input().strip().split()))
numbers = np.array(list_n)

print(np.mean(list_n))
print(np.median(list_n))
print(stats.mode(list_n)[0][0])
