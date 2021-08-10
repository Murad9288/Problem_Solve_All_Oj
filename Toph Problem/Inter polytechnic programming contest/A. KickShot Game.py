a,b = list(map(int,input().split()))
l = []
for i in range(a):
    li = list(map(int,input().split()))
    r = sorted(li)
    a = r[::-1]
    d = a[0:2]
    c = sum(d)
    l.append(c)
print(sum(l))
