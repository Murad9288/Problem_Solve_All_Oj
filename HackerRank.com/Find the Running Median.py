import bisect
arr = []
for _ in range(int(input())):
    n = int(input())
    bisect.insort(arr,n)
    if len(arr)%2 != 0:
        print(arr[len(arr)//2])
    else:
       print((arr[len(arr)//2]+arr[len(arr)//2-1])/2)
