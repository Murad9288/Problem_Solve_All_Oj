for t in range(int(input())):
    n = int(input())
    l = sorted(list(map(int,input().split())))

    prine = 0
    for i in range(n):
        r = n-(i)
        rr = l[i]
        if r*rr > prine:
            prine = r*rr

    print("Case %d: %d"%(t+1,prine))
