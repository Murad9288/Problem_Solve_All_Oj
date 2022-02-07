import math
for _ in range(int(input())):
    a,b = map(int,input().split())
    if math.gcd(a,b) == 1:
        print("yes")
    else:
        print("no")
