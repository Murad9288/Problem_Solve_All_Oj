for _ in range(int(input())):
    n = int(input())
    arr = list(map(float,input().split()))[:n]
    c = 1
    for i in arr:
        c *= i
    c = 1-c
    print("%.5f"%c)
