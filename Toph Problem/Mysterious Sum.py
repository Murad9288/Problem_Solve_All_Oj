for t in range(int(input())):
    a,b = map(int,input().split())
    x = a+b
    y = abs(a-b)
    s = ""
    for i in x,y:
        s += str(i)
    print("Case %d: %d"%(t+1,int(s)))
