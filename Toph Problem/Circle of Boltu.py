for t in range(int(input())):
    n = int(input())
    x = []
    y = []
    for _ in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    d = 0
    m = -10**5
    for i in range(n):
        for j in range(i+1,n):
            d = (x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j])
            if d>m:
                m = d
    print("Case %d: %d"%(t+1,m))
