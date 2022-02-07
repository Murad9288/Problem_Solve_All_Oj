for t in range(int(input())):
    m = k = s = 0
    for i in range(1,int(input())+1):
        a,b = map(int,input().split())
        s -= b
        if i>=2:
            k += 1
            if s == 0:
                m = max(m,k)
                k = 0
        s += a
    print("Case %d: %d"%(t+1,m))
