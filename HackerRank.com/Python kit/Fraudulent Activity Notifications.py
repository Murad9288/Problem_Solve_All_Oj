#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def get_limit(f,d):
    count = 0 
    m1,m2 = (d//2,d//2+1)
    m = []
    for i,j in enumerate(f):
        count+=j
        if not m and m1<=count:
            m.append(i)
        if m2<=count:
            m.append(i)
            break
    if d%2:
         return m[-1]*2 
    else:
        return sum(m)

def activityNotifications(e, n, d):
    f = [0]*201
    count = 0
    for i in e[:d]:
        f[i] += 1
    for i,v in enumerate(e[d:]):
        limit = get_limit(f,d)
        if v>=limit:
            count += 1
        f[v] += 1
        f[e[i]] -= 1

    return count
n,d = map(int,input().split())
e = list(map(int,input().split()))
print(activityNotifications(e, n, d))
