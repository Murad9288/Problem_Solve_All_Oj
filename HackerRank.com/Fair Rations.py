n = int(input())
arr = list(map(int,input().split()))
c = 0
if sum(arr)%2 != 0:
    print("NO")
else:
    for i in range(len(arr)-1):
        if arr[i]%2 != 0:
            arr[i+1] += 1
            c += 2
print(c)
