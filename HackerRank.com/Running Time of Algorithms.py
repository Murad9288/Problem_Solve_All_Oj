n = int(input())
arr = list(map(int,input().split())) [:n]
c = 0
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if arr[i]>arr[j]:
            c += 1
print(c)
