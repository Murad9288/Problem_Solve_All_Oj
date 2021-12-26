li =[]
l = input()

for i in range(12):
    li.append([])
    for j in range(12):
        x = float(input())
        li[i].append(x)

s = 0
count = 0
col = 11
for i in range(1,11):
    for j in range(col,12):
        s += li[i][j]
        
        count += 1
    if i < 5:
        col -= 1
    if i > 5:
        col += 1
    
    

mid = s / count

if l == "S":
    print("%.1f"%s)
else:
    print("%.1f"%mid)
