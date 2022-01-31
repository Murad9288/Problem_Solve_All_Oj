for i in range(int(input())):
    x, y, z, n = map(int,input().split())
    if z-y == y-x:
        print("Case %d: %d"%(i+1,x+(z-y)*(n-1)))
    else:
        print("Case %d: Error"%(i+1))
