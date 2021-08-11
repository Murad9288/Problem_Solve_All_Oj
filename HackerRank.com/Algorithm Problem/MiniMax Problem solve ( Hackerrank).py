'''
arr = list(map(int, input().rstrip().split()))
x = sum(arr)
print((x-(max(arr))),(x-(min(arr))))'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
     x = sum(arr)
     print((x-(max(arr))),(x-(min(arr))))
     
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

