for t in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    c = 0
    for i in arr:
        if i<0:
            i *= -1
        c = max(c,i)
    print("Case %d: %d"%(t+1,c))
