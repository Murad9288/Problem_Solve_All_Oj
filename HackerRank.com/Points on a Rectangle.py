#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY coordinates as parameter.
#

def solve(coordinates):
    d = dict(coordinates)
    y = d.values()
    x = d.keys()

    min_x = min(x)
    max_x = max(x)
    min_y = min(y)
    max_y = max(y)

    ret = "YES"
    for arr in coordinates:
        if (arr[0] > min_x) & (arr[0] < max_x) & (arr[1] > min_y) & (arr[1] < max_y):
            ret = "NO"
            break
    return ret
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        coordinates = []

        for _ in range(n):
            coordinates.append(list(map(int, input().rstrip().split())))

        print(solve(coordinates))
