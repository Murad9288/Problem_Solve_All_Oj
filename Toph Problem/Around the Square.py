import math
try:
    while True:
        a,r1,r2,r3,r4 = list(map(int,input().split()))
        print("%.3f"%(a*a-((r1*r1+r2*r2+r3*r3+r4*r4)*math.acos(-1.0)*0.25)))
except EOFError:
    pass
