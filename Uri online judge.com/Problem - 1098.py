I = 0
a = 1
b = 2
c = 3
d = 0
while I<=2:
    if d == 0:
        print("I=%.0f J=%.0f"%(I,a))
        print("I=%.0f J=%.0f"%(I,b))
        print("I=%.0f J=%.0f"%(I,c))
    else:
        print("I=%.1f J=%.1f"%(I,a))
        print("I=%.1f J=%.1f"%(I,b))
        print("I=%.1f J=%.1f"%(I,c))
    d += 1
    if d == 5:
        d = 0
    I += 0.2
    a += 0.2
    b += 0.2
    c += 0.2
