#!/bin/python3

import math
import os
import random
import re
import sys


# Like the robots of Asimov, all recursive algorithms must obey three important laws:
#
# A recursive algorithm must have a base case.
# A recursive algorithm must change its state and move toward the base case.
# A recursive algorithm must call itself, recursively.

# Complete the factorial function below.
def factorial(n):
    f = n

    # base case
    if n - 1 <= 1:
        return f
    # changing state
    else:
        # calling itself
        f = n * factorial(n - 1)
        return f


# similarly for sum we can do it this way

# def listsum(numList):
#    if len(numList) == 1:
#         return numList[0]
#    else:
#         return numList[0] + listsum(numList[1:])

#print(listsum([1,3,5,7,9]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()


