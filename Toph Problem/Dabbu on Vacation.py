import math
for t in range(int(input())):
    a,b,c = map(float,input().split())
    r1 = a/2
    v1 = 4/3*math.pi*r1*r1*r1
    res = r1-(a-b)
    r2 = r1*r1-res*res
    v2 = math.pi*r2*c
    if abs(v1-v2) <= 0.01:
        print("Case %d: Yes"%(t+1))
    else:
        print("Case %d: No"%(t+1))
