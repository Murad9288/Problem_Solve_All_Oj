n = int(input())
print(*(list(map(int,input().split()))[:n])[::-1])
