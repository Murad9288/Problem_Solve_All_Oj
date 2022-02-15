l = list(map(int,input().split()))
n = l[0]
m = l[1]
arr = list(map(int,input().split()))
a = set(map(int,input().split()))
b = set(map(int,input().split()))
d = {}
h = 0
for i in arr:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i]=1
for j in d.items():
    if j[0] in a:
        h = h + j[1]
    elif j[0] in b:
        h = h - j[1]
print(h)
