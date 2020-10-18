#!/usr/bin/env python3

import numpy as np
from sklearn import linear_model

def read_ints():
    return [int(x) for x in input().split(" ")]

def read_floats():
    return [float(x) for x in input().split(" ")]

def polynomial_features(x, order):
    x = np.asarray(x).T[np.newaxis]
    n = x.shape[1]
    power_matrix = np.tile(np.arange(order + 1), (n, 1)).T[..., np.newaxis]
    X = np.power(x, power_matrix)
    I = np.indices((order + 1, ) * n).reshape((n, (order + 1) ** n)).T
    F = np.product(np.diagonal(X[I], 0, 1, 2), axis=2)
    return F.T

def make_features(X):
    return polynomial_features(X, 3)

def main():
    line0 = read_ints()
    num_features, num_samples = line0[0], line0[1]
    dataset = np.array([read_floats() for i in range(num_samples)])

    #train_set_size = 0.85*num_samples
    X = dataset[:,:num_features]
    X = make_features(X)
    y = dataset[:,-1]
#    X_train = X[:train_set_size,:]
#    X_test = X[train_set_size:,:]
#    y_train = y[:train_set_size]
#    y_test = y[train_set_size:]
    pred_set_size = read_ints()[0]
    pred_set = np.array([read_floats() for i in range(pred_set_size)])
    pred_set = make_features(pred_set)
    regr = linear_model.BayesianRidge()
    regr.fit(X, y)

    predicted = regr.predict(pred_set)

    for price in predicted:
        print("%.2f" % price)

if __name__ == "__main__":
    main()