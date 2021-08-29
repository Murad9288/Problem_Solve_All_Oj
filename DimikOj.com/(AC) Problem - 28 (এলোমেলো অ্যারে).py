n = int(input())
li = []
for i in range(1,n+1):
    a = int(input())
    li.append(a)
if sorted(li) == li:
    print("YES")
else:
    print("NO")
