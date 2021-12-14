arr = []
for _ in range(int(input())):
    arr.append(list(map(int,input().split())))
s = 0
c = 0
l = len(arr)-1
for i in range(len(arr)):
    s += arr[i][i]
    c += arr[i][l]
    l -= 1
print(abs(s-c))
