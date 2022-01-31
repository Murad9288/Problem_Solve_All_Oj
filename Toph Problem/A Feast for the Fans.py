for _ in range(int(input())):
    st = input().split()
    s = st[0]
    d = int(st[1])
    n = 0
    if s == "January":
        n = 0
    elif s == "February":
        n = 31
    elif s == "March":
        n = 59
    elif s == "April":
        n = 90
    elif s == "May":
        n = 120
    elif s == "June":
        n = 151
    elif s == "July":
        n = 181
    elif s == "August":
        n = 212
    elif s == "September":
        n = 243
    elif s == "October":
        n = 273
    elif s == "November":
        n = 304
    else:
        n = 334
    n += d
    if n>67:
        n -= (n//67)*67
    if n == 0:
        n = 67
    s = n//10
    if n%10 != 0:
        s += 1
    e = n%10
    if e == 0:
        if s == 7:
            e = 7
        else:
            e = 10
    if e > 9:
        print("S0%dE%d" % (s,e))
    else:
        print("S0%dE0%d"%(s,e))
