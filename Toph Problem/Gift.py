n = int(input())
arr = list(map(int,input().split()))[:n]
sum = 0
for i in range(n):
    sum += arr[i]&1
print(sum) if sum<n else print("-1")


