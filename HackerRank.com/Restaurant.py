import math
for _ in range(int(input())):
    a,b = map(int,input().split())
    print((a*b)//(math.gcd(a,b)**2))
