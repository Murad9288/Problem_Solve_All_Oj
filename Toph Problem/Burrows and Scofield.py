s = str(input())
s2 = str(input())
d = "123456789"
c = 0
c2 = 0
for i in s:
    if i in d:
        c += int(i)
for j in s2:
    if j in d:
        c2 += int(j)
print('''"%d"'''%(c+c2))
