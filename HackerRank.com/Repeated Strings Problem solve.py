# Simple Input:
'''
aba
10
'''
# Simple output:
'''
7
'''

s = input()
n = int(input().strip())
c = s.count('a')
division = n // len(s)
if n % len(s) == 0:
    c = c*division
else:
    m = n % len(s)
    c = c*division + s[:m].count('a')
print(c)
