import math
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    gcd = arr[0]
    for i in arr[1::]:
        gcd = math.gcd(gcd, i)
    if gcd == 1:
        print("YES")
    else:
        print("NO")
