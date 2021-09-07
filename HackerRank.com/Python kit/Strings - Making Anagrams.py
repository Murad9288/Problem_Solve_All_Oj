a = input().strip()
b = input().strip()
count = dict()
for i in a:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
for j in b:
    if j in count:
        count[j] -= 1
    else:
        count[j] = -1    
sum = 0
for char in count.keys():
    sum += abs(count[char])        
print(sum)
