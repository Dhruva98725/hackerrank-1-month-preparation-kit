#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    plus = minus = zero = 0
    for element in arr:
        if element > 0:
            plus += 1
        elif element == 0:
            zero += 1
        else:
            minus += 1
            
    print("{:.6f}".format(plus / len(arr)))
    print("%.6f" % (minus / len(arr)))    
    print("%.6f" % (zero / len(arr)))
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
