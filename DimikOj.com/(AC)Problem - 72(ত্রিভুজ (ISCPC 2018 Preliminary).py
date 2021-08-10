import math
for _ in range(int(input())):
    a,b,c = list(map(int,input().split()))
    if (a+b >= c and b+c >= a and c+a >= b):
        s =(a+b+c)/2
        A = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("%0.2f"%A)
    else:
        print("Oh, No!")
