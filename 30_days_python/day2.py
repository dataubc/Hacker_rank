import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):

    total_cost = meal_cost + meal_cost*(tip_percent/100) + meal_cost*(tax_percent/100)
    print('totol cost of the meal is ',round(total_cost))

if __name__ == '__main__':
    meal_cost = float(input('What is the meal cost\n'))

    tip_percent = int(input('whats the tip percentage\n'))

    tax_percent = int(input('whats the tax percent\n'))

    solve(meal_cost, tip_percent, tax_percent)