#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    
    max_one_count = 0
    one_count = 0

    while n != 0:
        factor = n // 2
        remainder = int(n%2)
        n = factor
        if remainder == 1: #if remainder is 1, implies binary count
            one_count += 1
            max_one_count = max(max_one_count, one_count)
        else:
            one_count = 0

    print(max_one_count) 

# https://github.com/ehouarn-perret/EhouarnPerret.Python.HackerRank/blob/master/0%20-%20Tutorials/30%20Days%20of%20Code/Day%2010%20-%20Binary%20Numbers.py