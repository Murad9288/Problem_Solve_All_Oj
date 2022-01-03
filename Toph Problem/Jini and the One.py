n = int(input())
c = []
for i in range(1,n+1):
    s = str(i)
    for j in s:
        if j in "1":
            c.append(s)
print(len(set(c)))
