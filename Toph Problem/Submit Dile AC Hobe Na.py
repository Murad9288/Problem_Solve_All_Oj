n = int(input())
arr = list(map(int,input().split()))[:n]
arr2 = list(map(int,input().split()))[:n]
c = 0
for i in arr:
    for j in arr2:
        if j == i:
            c += 1
print(c)
