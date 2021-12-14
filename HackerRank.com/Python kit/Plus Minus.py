k = int(input())
arr = list(map(int,input().split())) [:k]
p = 0
n = 0
z = 0
for i in arr:
    if i>0:
        p += 1
    elif i == 0:
        z += 1
    else:
        n += 1
print("%.6f"%(p/k))
print("%.6f"%(n/k))
print("%.6f"%(z/k))
