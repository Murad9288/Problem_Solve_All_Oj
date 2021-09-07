n = int(input())
arr = list(map(int,input().strip().split()))
arr.sort()
li = []
for i in range(len(arr)-1):
    li.append(abs(arr[i] - arr[i+1]))
print(min(li))
