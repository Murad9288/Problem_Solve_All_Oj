n = int(input())
m = int(input())
x = 0
for _ in range(m):
    a = int(input())
    x += a
s = n*(n+1)//2
print(s-x)
