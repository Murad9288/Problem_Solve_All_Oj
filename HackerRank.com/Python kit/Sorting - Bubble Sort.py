n = int(input())
arr = list(map(int,input().strip().split()))
swaps = 0
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swaps += 1
print("Array is sorted in %d swaps."%swaps)
print("First Element: %d"%arr[0])
print("Last Element: %d"%arr[-1])
