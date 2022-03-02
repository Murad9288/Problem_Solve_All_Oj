import math
for _ in range(int(input())):
    d,k = map(int,input().split())
    c = 0
    r = math.ceil(d**.5)
    for i in range(0,r):
        x = (d-i**2)**.5
        if x == int(x):
            c += 4
    if k>=c:
        print("possible")
    else:
        print("impossible")
