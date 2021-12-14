arr = []
for _ in range(int(input())):
    arr.append(int(input()))
n = int(input())
for i in range(len(arr)):
    if arr[i] == n:
        print("YES")
        break
else:
    print("NO")
