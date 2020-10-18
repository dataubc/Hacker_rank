import numpy as np

features_number, observation_number = map(int,input().strip().split())

print(features_number, observation_number)


'method 1'



features_number, observation_number = map(int,input().strip().split())

array = np.array([input().strip().split() for _ in range(observation_number)], float)

print(array)

'method 2'

X = np.array([[float(x) for x in input().strip().split()] for line in range(observation_number)])

y = X[:,-1].reshape(observation_number,1)

X = X[:,:-1]


####