import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())

    if N % 2 != 0:
        print('Weird')
    else:
        if 5 >= N >= 2:
            print('Not Weird')
        elif 20 >= N >= 6:
            print('Weird')
        else:
            print('Not Weird')
