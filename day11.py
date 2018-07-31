#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    max = -1
    count = 0
    
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    for x in range(1,5):
        for y in range(1,5):
            top_x = x-1
            bottom_x = x+1
            left_y = y-1
            center_y = y
            right_y = y+1
        
            sum = arr[top_x][left_y] + arr[top_x][center_y] + arr[top_x][right_y] + arr[bottom_x][left_y] + arr[bottom_x][center_y] + arr[bottom_x][right_y] + arr[x][y]
        
            # print(str(x) + "," + str(y)) 
            # print(str(count) + ": " + str(sum) )
            # count += 1
        
            if sum > max:
                max = sum
            
    print(max)