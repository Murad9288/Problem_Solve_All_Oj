#First step: Use for fucntion.
#Accepted:

# simple input:
'''
5 3
1 2 100
2 5 100
3 4 100
'''
# simple output:
'''
200
'''
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    array = [0] * (n + 1)
    
    for query in queries: 
        a = query[0] - 1
        b = query[1]
        k = query[2]
        array[a] += k
        array[b] -= k
        
    max_value = 0
    running_count = 0
    for i in array:
        running_count += i
        if running_count > max_value:
            max_value = running_count
            
    return max_value
if __name__ == '__main__':
    n,m = map(int,input().strip().split())
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)

'''
# Second Step. Not function use:
# Accepted:

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
queries = []
for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))
array = [0]* (n+1) # array mainpulation structure..
for query in queries:
    a = query[0]-1
    b = query[1]
    k = query[2]
    array[a] += k
    array[b] -= k
max_val = 0f
running_count = 0
for i in array:
    running_count += i
    if running_count > max_val:
        max_val = running_count
print(max_val)




