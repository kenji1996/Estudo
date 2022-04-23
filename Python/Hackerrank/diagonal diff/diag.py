#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    diag1, diag2,size_array = 0,0,len(arr)-1
    
    for i in range(0,len(arr),1):
        diag1 += arr[i][i]
        
    for i in range(size_array,-1,-1):
        diag2 += arr[size_array - i][i]
        
    return abs(diag1 - diag2)
        

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)

