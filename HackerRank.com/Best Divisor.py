n = int(input())
arr = []
for i in range(1,n+1):
    if n%i == 0:
        arr.append(i)
li = []
max = 0
for j in arr:
    sum = 0
    for k in str(j):
        sum += int(k)
    if sum > max:
        max = sum
        li.append(j)
print(li.pop())
