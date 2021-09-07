n = int(input())
arr = list(map(int, input().rstrip().split()))
N = len(arr)
i = swap = 0
while i < N:
    while arr[i] != i+1:
        arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
        swap += 1
    i += 1

print(swap)
