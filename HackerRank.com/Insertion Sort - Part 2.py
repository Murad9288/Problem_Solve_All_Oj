n = int(input())
arr = list(map(int,input().split())) [:n]
for i in range(1,len(arr)):
    right = arr[i]
    j = i-1
    while j>=0 and arr[j]>right:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = right
    print(*arr)
