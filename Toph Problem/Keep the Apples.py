import math
n,m = map(int,input().split())
arr = list(map(int,input().split()))[:n]
c = 0
for i in arr:
    c += i
print(math.ceil(c/m))
