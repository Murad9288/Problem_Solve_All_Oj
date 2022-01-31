import math
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    res = []
    a = arr[0]
    for i in arr:
        res.append((a*i)//math.gcd(a,i))
        a = i
    res.append(arr[-1])
    print(*res)
