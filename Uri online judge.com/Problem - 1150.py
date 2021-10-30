n = int(input())
c = 0
while True:
    c = int(input())
    if c > n:
        break
res = n
a = 1
while res < c:
    res += n + a
    a += 1
print(a)
