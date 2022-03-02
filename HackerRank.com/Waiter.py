#!/bin/python3

import math
import os
import random
import re
import sys

def waiter(stack, q):
    # Write your code here
    p = []

    def isprime(n):
        for j in range(2, n):
            if n % j == 0:
                return('no')
        return('yes')
    for i in range(2, 10000):
        if (isprime(i)=='yes'):
            p.append(i)
    b = []
    a = []
    ans = []
    for i in range(q):
        while(stack):
            poped = stack.pop()
            if poped % p[i] == 0:
                b.append(poped)
            else:
                a.append(poped)
        while(b):
            ele = b.pop()
            ans.append(ele)
        stack = a
        a = []
    while(stack):
        ans.append(stack.pop())
    return(ans)   

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    number = list(map(int, input().rstrip().split()))
    result = waiter(number, q)
    for e in result:
        print(e)
