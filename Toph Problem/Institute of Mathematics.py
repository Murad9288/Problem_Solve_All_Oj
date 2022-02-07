for _ in range(int(input())):
    n = int(input())
    arr = list(map(str,input().lower().split()))[:n]
    print(*arr,sep="")
