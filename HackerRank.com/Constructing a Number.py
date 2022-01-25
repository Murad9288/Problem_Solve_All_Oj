for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    if sum(arr)%3 == 0:
        print("YES")
    else:
        print("NO")
