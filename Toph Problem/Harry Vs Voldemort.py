for t in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))[:n]
    arr.sort()
    sum = 0
    f = False
    for i in range(n-1,-1,-1):
        sum += arr[i]
        if sum>=k:
            f = True
            print("Case %d: %d" % (t + 1, n-i))
            break
    if not f:
        print("Case %d: Dobby is sorry for master Harry"%(t + 1))
