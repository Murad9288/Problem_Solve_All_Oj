for _ in range(int(input())):
    s = str(input()).upper()
    a = s.count("U")
    b = s.count("C")
    c = s.count("P")
    if b>1 and a>0 and c>0:
        print(min(a,b//2,c))
    else:
        print(0)
