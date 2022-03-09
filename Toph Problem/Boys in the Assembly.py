n,m = map(int,input().split())
arr = list(map(int,input().split()))[:n]
m %= n
print(arr[m],arr[m-1])
