import math
d= u'\N{DEGREE SIGN}'
AB = int(input())
BC = int(input())
res = math.pow(((AB*AB) + (BC*BC)), 0.5)
num = (BC*BC) + (res*res) - (AB*AB)
den = (2*(BC*res))
angle_C = math.degrees(math.acos(num/den))
print (str(int(round(angle_C))) + d)
