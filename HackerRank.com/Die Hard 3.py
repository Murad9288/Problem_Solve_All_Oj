import math
for _ in range(int(input())):
    a,b,c = list(map(int,input().split()))
    g = math.gcd(a,b)
    if c<=max(a,b) and c%g==0:
        print("YES")
    else:
        print("NO")
