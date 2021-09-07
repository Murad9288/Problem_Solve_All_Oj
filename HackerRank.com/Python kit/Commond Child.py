# First Rules:

'''

s1 = input()
s2 = input()
sub = []
for i in s1:
    sub.append(0)
for j in s2:
    max_ = 0
    for k in range(len(s1)):
        tmp = sub[k]
        if j == s1[k]:
            sub[k] = max_ + 1
        if sub[k] > 0 and tmp > 0:
            max_ = max(tmp,max_)
print(max(sub))

'''
# 2nd Rules:

'''
#I think that the following is a pretty solution to the problem in python3, with spatial complexity of O(n).

def commonChild(s1, s2):
    subsequences = [0 for _ in s1]
    for c in s2:
        max_length = 0
        for i in range(len(s1)):
            tmp = subsequences[i]
            if c == s1[i]:
                subsequences[i] = max_length + 1
            if subsequences[i] > 0 and tmp > 0:
                max_length = max(tmp, max_length)
    return max(subsequences)

s1 = input()
s2 = input()
result = commonChild(s1, s2)
print(result)
'''

# 3rd Rules:
# Accepted:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    sub = [0 for i in s1]
    for j in s2:
        max_ = 0
        for k in range(len(s1)):
            tmp = sub[k]
            if j == s1[k]:
                sub[k] = max_ + 1
            if sub[k] > 0 and tmp > 0:
                max_ = max(tmp,max_)
    return max(sub)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
