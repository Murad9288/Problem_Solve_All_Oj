
import math
for _ in range(int(input())):
    n = int(input())
    a = n**3*((9*n) - 3)
    b = 6*(n**2)
    c = math.floor(a/b)
    print(c-(n**2)+n)
