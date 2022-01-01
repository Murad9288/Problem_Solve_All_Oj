for _ in range(int(input())):
        n = int(input())
    arr = list(map(int,input().split())) [:n]
    c = []
    for i in sorted(arr):
        if arr[0] != i :
            c.append(i)
    print(*c)
