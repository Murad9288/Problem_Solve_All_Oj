#Sample Input:
'''
STDIN                       Function
-----                       --------
9                           Example: n = 9
10 20 20 10 10 30 50 10 20  #Example: ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
'''
#Sample Output:
'''
3
'''

import sys

n = input()
socks = input().strip().split()
pairs = 0
S = set(socks)

for element in S:
    pairs += socks.count(element) // 2
print(pairs)
