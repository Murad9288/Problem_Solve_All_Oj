#!/bin/python3
# Sample Input:

# 4
# 1 4 3 2
# Sample Output:

# 2 3 4 1


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    print(*arr[::-1])
