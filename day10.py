#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    
    # n = 7
    
    binary = list()
     
    
    #convert n into binary
    while n>0:
        remainder = n%2
        n = int(n/2)
        # print(n)
        binary.insert(0,int(remainder))
        # binary.append(remainder)
        # print("remainder: " + str(remainder) + " n: " + str(n))
    
    #find longest chain of 1
    
    # chain = 1
    zeropos = list()
    onepost = list()
    binstr = str()
    
    for _ in range(len(binary)):
        # if i can get the position of 0 in the binary list, I can know what's the max chain of 1
        if binary[_] == 1:
            onepost.append(_)
        binstr += str(binary[_])            
        # print(binary[_], end="")
    #given binary list length and position of zero
    
    # print(onepost)
    for x in range()
    
    # maxchain = max(len(x) for x in binstr[2:].split('0')) 
    # print(maxchain)
    
    # print(chain)