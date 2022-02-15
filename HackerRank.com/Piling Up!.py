for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    m = arr.index(min(arr))
    left = arr[:m]
    right = arr[m+1:]
    if left == sorted(left, reverse=True) and right == sorted(right):
        print("Yes")
    else:
        print("No")
