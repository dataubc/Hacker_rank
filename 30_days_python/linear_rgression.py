import numpy as np

dimensions = input()

F, H = map(int, dimensions.split())

# F  is the number of feature
# H  is the number of houses/rows
#print(F,H)


# reading the lines, splitting to get the numbers and then get the float of the numbers
X = np.array([[float(x) for x in input().split()] for line in range(H)])

# get X and y and also reshape the uy

y = X[:,-1].reshape(H,1)

X = X[:,:-1]

# get the test data

t = int(input())
X_test = np.array([[float(x) for x in input().split()] for line in range(t)])
from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(X,y)

y_predicted = lr.predict(X_test)
y_final = y_predicted.reshape([t,1])
y_final_list = list(y_final.flat)
for price in y_final_list:
    print(round(price,2))
