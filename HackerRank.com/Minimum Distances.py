n = int(input())
arr = list(map(int,input().split())) [:n]
li = []
for i in range(n-1):
    for j in range(i+1,n):
        if arr[i] == arr[j]:
            res = j-i
            li.append(res)
            break
if li:
    print(min(li))
else:
    print(-1)
