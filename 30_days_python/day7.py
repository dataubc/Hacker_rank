import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().split()))
    rever = arr[::-1]
    for count, ele in enumerate(rever):
        print(ele, end=' ')
