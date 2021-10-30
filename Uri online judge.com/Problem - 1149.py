li = list(map(int, input().split()))
n = 'I'
m = 0
c = 0
for i in li:
    if n == 'I':
        n = i
    else:
        if i > 0:
            m = i
            break
for i in range(m):
    c += n
    n += 1
print("%d"%c)
