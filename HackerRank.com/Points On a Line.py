n = int(input())
c = []
d = []
for _ in range(n):
    a,b = map(int,input().split())
    c.append(a)
    d.append(b)
if len(set(c)) == 1 or len(set(d)) == 1:
    print("YES")
else:
    print("NO")
