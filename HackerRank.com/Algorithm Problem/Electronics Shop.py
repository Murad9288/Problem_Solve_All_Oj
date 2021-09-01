s,n,m = map(int,input().strip().split())
k = list(map(int,input().strip().split()))
p = list(map(int,input().strip().split()))

r = -1

for i in k:
    for j in p:
        val = i + j
        if val <= s:
            r = max(val, r)

print (r)
