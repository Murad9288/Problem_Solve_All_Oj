import math
for _ in range(int(input())):
    a,b,x,y = map(int,input().split())
    if math.gcd(a,b) == math.gcd(x,y):
        print("YES")
    else:
        print("NO")
