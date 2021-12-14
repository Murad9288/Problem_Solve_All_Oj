n = int(input())
arr = list(map(int,input().split())) [:n]
s = sum(set(arr))
l = sum(arr)
print((s*2)-l)
