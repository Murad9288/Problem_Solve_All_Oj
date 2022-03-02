n,k = map(int,input().split())
arr = list(map(int,input().split()))[:n]
if sum(arr)>k:
    print("Yes")
else:
    print("No")
