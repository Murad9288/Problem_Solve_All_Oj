import math
a,b,c = map(float,input().split())
d = (b**2)-(4*a*c)
if d<0 or a == 0:
    print("Impossivel calcular")
else:
    d = math.sqrt(d)
    res_1 = (-b+d)/(2*a)
    res_2 = (-b-d)/(2*a)
    print("R1 = %0.5f"%res_1)
    print("R2 = %0.5f"%res_2)
