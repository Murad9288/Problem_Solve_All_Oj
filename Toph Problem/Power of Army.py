for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    print(max(arr)-min(arr))
