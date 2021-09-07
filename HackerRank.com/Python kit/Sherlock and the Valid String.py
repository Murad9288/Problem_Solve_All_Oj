s = str(input())
L = []
count = []
for i in s:
    if i not in L:
        L.append(i)
for j in L:
    c = s.count(j)
    count.append(c)
#Print (countList)
key = count[0]
flag = 0
for k in count:
    if(key != k):
        flag += 1
if(flag > 1):
    print("NO")
else:
    print("YES")
