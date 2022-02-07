for t in range(int(input())):
    p,k,d = map(int,input().split())
    sum = p+k
    sum2 = p+d
    while sum2 <= sum:
        sum2 += d
    print("Case %d: %d"%(t+1,sum2))
