# Simple Input - Output:
'''
4
1 4 3 2
2 3 4 1   #  Output
'''
n = int(input())
a = list(map(int,input().split()))
a.reverse()
print(*a)
