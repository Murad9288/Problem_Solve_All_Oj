n = int(input())
arr = list(map(int,input().split()))[:n]
a = []
for i in arr:
    if i%2 == 0:
        a.append("0")
    else:
        a.append("1")
print(*a,sep=" ")
