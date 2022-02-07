for t in range(int(input())):
    a,b,c = map(str,input().split())
    if b == "U" and c == "MBSTU":
        print("Case #%d: YES"%(t+1))
    elif b == "Y" and c == "2017":
        print("Case #%d: YES" % (t + 1))
    elif b == "C" and c == "IDPC":
        print("Case #%d: YES" % (t + 1))
    elif b == "D" and c == "CSE":
        print("Case #%d: YES" % (t + 1))
    else:
        print("Case #%d: NO" % (t + 1))
