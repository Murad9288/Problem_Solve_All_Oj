n = int(input())
arr = list(map(int,input().split()))
for i in set(arr):
    arr.remove(i)
    if i not in arr:
        print(i)
        break
