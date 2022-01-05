n = int(input())
arr = list(map(int,input().split()))[:n]
largest = 0
for i in range(len(arr)):
    c = 0
    for j in range(i,-1,-1):
        if arr[j] >= arr[i]:
            c += 1
        else:
            break
    for k in range(i+1,len(arr)):
        if arr[k] >= arr[i]:
            c += 1
        else:
            break
    a = arr[i] * c
    if a > largest:
        largest = a
print(largest)
