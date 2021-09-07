n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
total = 0
count = 0
for i in arr:
    total += i
    if total <= m:
        count += 1
print(total)
print(count)
