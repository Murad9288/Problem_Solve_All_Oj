for t in range(int(input())):
    s = input()
    c_u = 0
    c_l = 0
    c_d = 0
    for i in range(len(s)):
        if s[i].isupper():
            c_u += 1
        elif s[i].islower():
            c_l += 1
        else:
            c_d += 1
    if c_d == len(s):
        print("Case %d: %d"%(t+1,c_d-1))
    elif c_u == len(s) or c_l == len(s):
        print("Case %d: %d"%(t+1,0-1))
    elif c_u>c_l:
        print("Case %d: %d"%(t+1,len(s)-c_u-1))
    else:
        print("Case %d: %d"%(t+1,len(s)-c_l-1))
