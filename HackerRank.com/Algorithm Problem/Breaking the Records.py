n = int(input())
li = list(map(int,input().split())) [:n]
old_max = li[0]
old_min = li[0]
new_max = []
new_min = []

for i in range(len(li)):
    if li[i] > old_max:
        old_max = li[i]
        new_max.append(old_max)
    if li[i] < old_min:
        old_min = li[i]
        new_min.append(old_min)
print(len(new_max),len(new_min))
