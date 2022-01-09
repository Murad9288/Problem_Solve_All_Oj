for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    c = 1
    for i in arr:
        c *= i
    print(c%1234567)
