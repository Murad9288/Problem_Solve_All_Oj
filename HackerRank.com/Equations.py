#!/bin/python3

import os
import sys

# n = N!
# x + y = xy / n
# xn + yn = xy
# xy - xn - yn + n^2 = n^2
# (x-n)(y-n) = n^2
# XY = n^2
# answer is number of factors of N!^2

# Complete the solve function below.
def count(n, p):
    count = 0
    n_copy = n
    while n_copy > 1:
        count += n_copy // p
        n_copy //= p
    return count

def solve(n):
    pr = 1
    isprime = [True] * (n + 1)
    for num in range(2, n + 1):
        if not isprime[num]: 
            continue
        pr = pr * (2 * count(n, num) + 1) % 1000007
        for multiple in range(2 * num, n + 1, num):
            isprime[multiple] = False
    return pr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    result = solve(n)
    fptr.write(str(result) + '\n')
    fptr.close()
