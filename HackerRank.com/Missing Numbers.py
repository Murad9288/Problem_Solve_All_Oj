n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))
missing = set()
for i in arr2:
    if i in arr1:
        arr1.remove(i)
    else:
        missing.add(i)
print(*sorted(list(missing)))
