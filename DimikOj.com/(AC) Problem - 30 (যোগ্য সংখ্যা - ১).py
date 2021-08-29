#1st rules:

import math
for _ in range(int(input())):
    n = int(input())
    s, sum = int(math.sqrt(n)), 1
    for i in range(2,s+1):
        if n%i == 0:
            sum += (n//i) + i
        if sum > n:
            break
    if sum == n:
        print("YES, %d is a perfect number!"%n)
    else:
        print("NO, %d is not a perfect number!"%n)
        
# Second rules:
'''
for _ in range(int(input())):
    n = int(input())
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum += i
    if sum == n:
        print("YES, %d is a perfect number!"%n)
    else:
        print("NO, %d is not a perfect number!"%n)

'''
