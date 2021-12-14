n = int(input())
arr = list(map(int,input().split()))
res = [0]*100
for i in arr:
    res[i] += 1
print(*res)
