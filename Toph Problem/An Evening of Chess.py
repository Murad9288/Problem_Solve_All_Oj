for t in range(int(input())):
    a,b = map(str,input().split())
    if a[-1]>b[-1]:
        print("Case %d: Chandler"%(t+1))
    elif a[-1] == b[-1]:
        print("Case %d: Draw"%(t+1))
    else:
        print("Case %d: Steve"%(t+1))
