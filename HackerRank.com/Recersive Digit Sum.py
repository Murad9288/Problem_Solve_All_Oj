#!/bin/python3

import math
import os
import random
import re
import sys


def superDigit(n, k):
        
    if k == len(n) == 1:
        return int(n)

    c = 0
    for i in n:
        c += int(i)

    return superDigit(str(c*k),1)

if __name__ == '__main__':
    
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    print(result)
