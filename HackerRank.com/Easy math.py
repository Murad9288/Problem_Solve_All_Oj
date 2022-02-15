#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER x as parameter.
#

def getnum(n):
  cnt_2  = 0
  cnt_5  = 0
  
  m = n
  while m % 2 == 0:
    m    //= 2
    cnt_2 += 1
  
  while m % 5 == 0:
    m    //= 5
    cnt_5 += 1
  
  pow_10 = max(cnt_2 - 2, cnt_5)
  
  num1 = 10 ** pow_10 * 4
  num2 = 1
  rem  = 1
  while rem % m:
    num2 += 1
    rem   = (rem * 10 + 1) % m
    
  return num1 * (10 ** num2 -1) // 9


def solve(n):
  num = str(getnum(n))
  a   = num.count('4')
  b   = num.count('0')
  return 2 * a + b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        x = int(input().strip())

        result = solve(x)

        fptr.write(str(result) + '\n')

    fptr.close()
