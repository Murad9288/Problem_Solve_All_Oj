a = set(input().split())
n = int(input())
c = set()
for i in range(n):
    c.update(input().split())
print(c.issubset(a))
