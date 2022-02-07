for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))[:n]
    s = 0
    for i in arr:
        if i>k:
            s += (i-k)
    print(s)
