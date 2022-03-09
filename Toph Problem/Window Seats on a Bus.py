for t in range(int(input())):
    L,W,D = map(float,input().split())
    print("Case %d: %.2f"%(t+1,((W-D)/2)*L))
