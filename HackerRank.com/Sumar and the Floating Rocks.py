from math import gcd
for _ in range(int(input())):
    x1,y1,x2,y2 = map(int,input().split())
    print(max(gcd(x1-x2,y1-y2),1) - 1)
