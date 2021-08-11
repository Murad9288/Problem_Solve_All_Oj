li = []
count = 0
for i in range(6):
    n = float(input())
    if(n>=0):
        li.append(n)
        count += 1
print("%d valores positivos"%count)
print("%.1f"%(sum(li)/count))
