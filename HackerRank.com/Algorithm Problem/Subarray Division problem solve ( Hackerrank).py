# Simple input - output:
'''
5
1 2 1 3 2
3 2
2 # output
6
1 1 1 1 1 1
3 2
0  # output
'''
n = int(input())
a = list(map(int,input().split()))
b,m = map(int,input().split())
re = 0
for i in range(len(a)):
    if sum(a[i:i + m]) == b:
        re += 1
print(re)
